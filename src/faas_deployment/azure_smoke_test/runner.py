"""Azure Functions smoke test runner."""
import json
import logging
import re
import time
from dataclasses import dataclass
from typing import Dict, List, Optional
from urllib.parse import urlparse

import requests

from .adapter import build_azure_project
from .azure_cli import (
    AzureResourceNames,
    format_tags,
    run_az_command,
    run_func_command,
    sanitize_function_app,
    sanitize_resource_group,
    sanitize_storage_account,
)

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class AzureSmokeConfig:
    """Configuration for an Azure Functions smoke test run."""

    region: str
    deployment_identity: str
    tags: Dict[str, str]


@dataclass(frozen=True)
class AzureSmokeResult:
    """Result of a smoke test run."""

    resource_names: AzureResourceNames
    function_urls: List[str]
    function_results: List['AzureFunctionResult']
    publish_s: Optional[float]
    failures: List[str]

    @property
    def success(self) -> bool:
        return not self.failures


@dataclass(frozen=True)
class AzureFunctionResult:
    """Per-function invocation result with timing."""

    name: str
    url: str
    success: bool
    status_code: Optional[int]
    error: Optional[str]
    execute_s: Optional[float]


class AzureSmokeTestRunner:
    """Deploy and smoke test Azure Functions from prepared directories."""

    def __init__(self, config: AzureSmokeConfig):
        self.config = config

    def run(
        self,
        prepared_dir: str,
        azure_project_dir: str,
        template_dir: str,
        smart_home_dir: str,
        experiment: str,
        run_id: Optional[str] = None,
    ) -> AzureSmokeResult:
        """Run the Azure Functions smoke test.

        Args:
            prepared_dir: Directory containing prepared function folders.
            azure_project_dir: Destination Azure Functions project directory.
            template_dir: Directory with Azure Functions template files.
            smart_home_dir: Smart home code directory.
            experiment: Experiment name for tagging.
            run_id: Optional run identifier.

        Returns:
            AzureSmokeResult with URLs and failures.

        Raises:
            RuntimeError: When deployment or invocation fails.
        """
        resource_names = self._generate_resource_names(experiment, run_id)
        failures: List[str] = []
        function_urls: List[str] = []
        function_results: List[AzureFunctionResult] = []
        publish_s: Optional[float] = None
        entry_by_route: Dict[str, str] = {}

        tags = dict(self.config.tags)
        tags["experiment"] = experiment
        if run_id:
            tags["run_id"] = run_id

        try:
            entries = build_azure_project(prepared_dir, azure_project_dir, template_dir, smart_home_dir)
            entry_by_route = {entry.route: entry.name for entry in entries}
            self._create_resource_group(resource_names.resource_group, tags)
            self._create_storage_account(resource_names, tags)
            self._ensure_managed_identity(resource_names, tags)
            self._enable_storage_key_auth(resource_names)
            self._create_function_app(resource_names, tags)

            publish_started = time.time()
            self._publish_function_app(resource_names.function_app, azure_project_dir)
            publish_s = time.time() - publish_started
            function_urls = self._list_function_urls(resource_names.function_app)
            if not function_urls:
                raise RuntimeError("No HTTP trigger URLs discovered after publish.")

            for url in function_urls:
                route = _extract_route(url)
                function_name = entry_by_route.get(route, route or url)
                result = self._invoke_function(function_name, url)
                function_results.append(result)
                if not result.success:
                    failures.append(result.error or f"Invocation failed for {url}")
        except Exception as exc:
            failures.append(str(exc))
            logger.exception("Azure smoke test failed.")
        finally:
            self._delete_resource_group(resource_names.resource_group)

        result = AzureSmokeResult(
            resource_names=resource_names,
            function_urls=function_urls,
            function_results=function_results,
            publish_s=publish_s,
            failures=failures,
        )
        if not result.success:
            logger.warning(
                "Azure smoke test failed for %s: %s",
                resource_names.function_app,
                "; ".join(failures),
            )
        else:
            logger.info("Azure smoke test succeeded for %s", resource_names.function_app)
        return result

    def _generate_resource_names(self, experiment: str, run_id: Optional[str]) -> AzureResourceNames:
        timestamp = time.strftime("%Y%m%d%H%M%S")
        suffix = f"{timestamp}" if not run_id else f"{timestamp}-{run_id}"
        rg_base = sanitize_resource_group(f"llm4faas-{experiment}-{suffix}")
        app_base = sanitize_function_app(f"llm4faas-{experiment}-{suffix}")
        storage_base = sanitize_storage_account(f"llm4faas{experiment}{suffix}")
        return AzureResourceNames(resource_group=rg_base, storage_account=storage_base, function_app=app_base)

    def _create_resource_group(self, name: str, tags: Dict[str, str]) -> None:
        run_az_command([
            "az",
            "group",
            "create",
            "--name",
            name,
            "--location",
            self.config.region,
            *format_tags(tags),
        ])

    def _create_storage_account(self, names: AzureResourceNames, tags: Dict[str, str]) -> None:
        run_az_command([
            "az",
            "storage",
            "account",
            "create",
            "--name",
            names.storage_account,
            "--location",
            self.config.region,
            "--resource-group",
            names.resource_group,
            "--sku",
            "Standard_LRS",
            "--allow-blob-public-access",
            "false",
            "--allow-shared-key-access",
            "true",
            *format_tags(tags),
        ])

    def _enable_storage_key_auth(self, names: AzureResourceNames) -> None:
        run_az_command([
            "az",
            "storage",
            "account",
            "update",
            "--name",
            names.storage_account,
            "--resource-group",
            names.resource_group,
            "--allow-shared-key-access",
            "true",
        ])

    def _ensure_managed_identity(self, names: AzureResourceNames, tags: Dict[str, str]) -> None:
        identity_result = run_az_command([
            "az",
            "identity",
            "create",
            "--name",
            self.config.deployment_identity,
            "--resource-group",
            names.resource_group,
            "--location",
            self.config.region,
            "--query",
            "{userId:id, principalId: principalId, clientId: clientId}",
            "-o",
            "json",
            *format_tags(tags),
        ])

        identity_payload = json.loads(identity_result.stdout or "{}")
        principal_id = identity_payload.get("principalId")
        if not principal_id:
            raise RuntimeError("Managed identity creation did not return principalId")

        storage_result = run_az_command([
            "az",
            "storage",
            "account",
            "show",
            "--resource-group",
            names.resource_group,
            "--name",
            names.storage_account,
            "--query",
            "id",
            "-o",
            "tsv",
        ])
        storage_id = (storage_result.stdout or "").strip()
        if not storage_id:
            raise RuntimeError("Storage account lookup did not return an id")

        run_az_command([
            "az",
            "role",
            "assignment",
            "create",
            "--assignee-object-id",
            principal_id,
            "--assignee-principal-type",
            "ServicePrincipal",
            "--role",
            "Storage Blob Data Owner",
            "--scope",
            storage_id,
        ])

    def _create_function_app(self, names: AzureResourceNames, tags: Dict[str, str]) -> None:
        run_az_command([
            "az",
            "functionapp",
            "create",
            "--resource-group",
            names.resource_group,
            "--name",
            names.function_app,
            "--flexconsumption-location",
            self.config.region,
            "--runtime",
            "python",
            "--runtime-version",
            "3.12",
            "--storage-account",
            names.storage_account,
            "--deployment-storage-auth-type",
            "UserAssignedIdentity",
            "--deployment-storage-auth-value",
            self.config.deployment_identity,
            *format_tags(tags),
        ])

    def _publish_function_app(self, app_name: str, project_dir: str) -> str:
        result = run_func_command(
            ["func", "azure", "functionapp", "publish", app_name, "--python"],
            cwd=project_dir,
        )
        logger.info("Publish output: %s", result.stdout.strip())
        return result.stdout

    def _list_function_urls(self, app_name: str) -> List[str]:
        result = run_func_command(
            ["func", "azure", "functionapp", "list-functions", app_name, "--show-keys"],
        )
        urls = _extract_urls(result.stdout)
        logger.info("Discovered %d function URLs", len(urls))
        return urls

    def _invoke_function(self, name: str, url: str) -> AzureFunctionResult:
        started = time.time()
        try:
            response = requests.get(url, timeout=600)
            execute_s = time.time() - started
            success = 200 <= response.status_code < 300
            error = None if success else f"Invocation failed for {url}: {response.status_code}"
            logger.info("Invoked %s - status code: %d", url, response.status_code)
            return AzureFunctionResult(
                name=name,
                url=url,
                success=success,
                status_code=response.status_code,
                error=error,
                execute_s=execute_s,
            )
        except requests.RequestException as exc:
            execute_s = time.time() - started
            error = f"Invocation error for {url}: {exc}"
            return AzureFunctionResult(
                name=name,
                url=url,
                success=False,
                status_code=None,
                error=error,
                execute_s=execute_s,
            )

    def _delete_resource_group(self, name: str) -> None:
        try:
            run_az_command([
                "az",
                "group",
                "delete",
                "--name",
                name,
                "--yes",
            ])
            run_az_command([
                "az",
                "group",
                "wait",
                "--deleted",
                "--name",
                name,
                "--timeout",
                "600",
            ])
        except Exception as exc:
            logger.warning("Failed to delete resource group %s: %s", name, exc)


def _extract_urls(output: str) -> List[str]:
    urls = re.findall(r"https?://[^\s\"'\)]+", output)
    cleaned = []
    for url in urls:
        cleaned.append(url.rstrip("\"')"))
    return sorted(set(cleaned))


def _extract_route(url: str) -> str:
    parsed = urlparse(url)
    path = parsed.path or ""
    if "/api/" not in path:
        return ""
    route = path.split("/api/", 1)[1]
    route = route.strip("/")
    return route

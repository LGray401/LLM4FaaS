"""Azure CLI helpers for Azure Functions smoke testing."""
import logging
import re
import subprocess
from dataclasses import dataclass
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class AzureResourceNames:
    """Generated Azure resource names for a smoke test run."""

    resource_group: str
    storage_account: str
    function_app: str


def run_az_command(args: List[str], cwd: Optional[str] = None) -> subprocess.CompletedProcess:
    """Run an Azure CLI command and return the completed process.

    Args:
        args: Azure CLI arguments (including 'az').
        cwd: Optional working directory.

    Returns:
        CompletedProcess with stdout and stderr.

    Raises:
        subprocess.CalledProcessError: When the CLI command fails.
    """
    logger.info("Running Azure CLI: %s", " ".join(args))
    try:
        return subprocess.run(
            args,
            cwd=cwd,
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as exc:
        stderr = (exc.stderr or "").strip()
        stdout = (exc.stdout or "").strip()
        if stderr:
            logger.error("Azure CLI error output: %s", stderr)
        if stdout:
            logger.error("Azure CLI standard output: %s", stdout)
        raise


def run_func_command(args: List[str], cwd: Optional[str] = None) -> subprocess.CompletedProcess:
    """Run an Azure Functions Core Tools command.

    Args:
        args: Core Tools arguments (including 'func').
        cwd: Optional working directory.

    Returns:
        CompletedProcess with stdout and stderr.

    Raises:
        subprocess.CalledProcessError: When the command fails.
    """
    logger.info("Running Core Tools: %s", " ".join(args))
    try:
        return subprocess.run(
            args,
            cwd=cwd,
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as exc:
        stderr = (exc.stderr or "").strip()
        stdout = (exc.stdout or "").strip()
        if stderr:
            logger.error("Core Tools error output: %s", stderr)
        if stdout:
            logger.error("Core Tools standard output: %s", stdout)
        raise


def format_tags(tags: Dict[str, str]) -> List[str]:
    """Format tags dict for Azure CLI arguments."""
    tag_args = ["--tags"]
    for key, value in tags.items():
        tag_args.append(f"{key}={value}")
    return tag_args


def sanitize_resource_group(name: str) -> str:
    """Sanitize resource group name to allowed characters."""
    cleaned = re.sub(r"[^a-zA-Z0-9-_]", "-", name)
    return cleaned[:90]


def sanitize_function_app(name: str) -> str:
    """Sanitize function app name (letters, digits, hyphens)."""
    cleaned = re.sub(r"[^a-zA-Z0-9-]", "-", name)
    cleaned = cleaned.strip("-")
    return cleaned[:60]


def sanitize_storage_account(name: str) -> str:
    """Sanitize storage account name (lowercase letters and digits, 3-24 chars)."""
    cleaned = re.sub(r"[^a-z0-9]", "", name.lower())
    if len(cleaned) < 3:
        cleaned = f"llm{cleaned}".ljust(3, "0")
    return cleaned[:24]

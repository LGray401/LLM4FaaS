"""Adapt prepared functions into an Azure Functions project layout."""
import logging
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class AzureFunctionEntry:
    """Descriptor for a single HTTP-triggered function."""

    name: str
    module_name: str
    handler_name: str
    route: str


def build_azure_project(
    prepared_dir: str,
    output_dir: str,
    template_dir: str,
    smart_home_dir: str,
) -> List[AzureFunctionEntry]:
    """Build an Azure Functions project from prepared function folders.

    Args:
        prepared_dir: Directory containing prepared function folders (each with fn.py).
        output_dir: Destination Azure Functions project directory.
        template_dir: Template directory containing host.json and requirements.txt.
        smart_home_dir: Smart-home template directory to copy into project root.

    Returns:
        List of AzureFunctionEntry definitions created in function_app.py.

    Raises:
        FileNotFoundError: If expected files or directories are missing.
        ValueError: If no prepared functions are found.
    """
    prepared_path = Path(prepared_dir)
    output_path = Path(output_dir)
    template_path = Path(template_dir)
    smart_home_path = Path(smart_home_dir)

    if not prepared_path.exists():
        raise FileNotFoundError(f"Prepared directory not found: {prepared_dir}")
    if not template_path.exists():
        raise FileNotFoundError(f"Template directory not found: {template_dir}")
    if not smart_home_path.exists():
        raise FileNotFoundError(f"Smart-home directory not found: {smart_home_dir}")

    function_dirs = [p for p in prepared_path.iterdir() if p.is_dir()]
    if not function_dirs:
        raise ValueError(f"No prepared functions found in {prepared_dir}")

    if output_path.exists():
        shutil.rmtree(output_path)
    output_path.mkdir(parents=True, exist_ok=True)

    _copy_if_exists(template_path / "host.json", output_path / "host.json")
    _copy_if_exists(template_path / "requirements.txt", output_path / "requirements.txt")
    _copy_if_exists(template_path / ".funcignore", output_path / ".funcignore")

    _copy_smart_home(smart_home_path, output_path)

    entries: List[AzureFunctionEntry] = []
    for func_dir in function_dirs:
        fn_path = func_dir / "fn.py"
        if not fn_path.exists():
            logger.warning("Skipping %s (missing fn.py)", func_dir.name)
            continue

        module_name = _sanitize_module_name(func_dir.name)
        handler_name = _sanitize_handler_name(func_dir.name)
        route = _sanitize_route(func_dir.name)

        dest_module = output_path / f"{module_name}.py"
        shutil.copy2(fn_path, dest_module)

        entries.append(
            AzureFunctionEntry(
                name=func_dir.name,
                module_name=module_name,
                handler_name=handler_name,
                route=route,
            )
        )

    if not entries:
        raise ValueError("No functions with fn.py were available for Azure adaptation")

    function_app_path = output_path / "function_app.py"
    function_app_path.write_text(_render_function_app(entries), encoding="utf-8")

    return entries


def _copy_if_exists(src: Path, dest: Path) -> None:
    if src.exists():
        shutil.copy2(src, dest)
    else:
        raise FileNotFoundError(f"Missing template file: {src}")


def _copy_smart_home(smart_home_path: Path, output_path: Path) -> None:
    for entry in smart_home_path.iterdir():
        dest = output_path / entry.name
        if entry.is_file():
            shutil.copy2(entry, dest)
        elif entry.is_dir():
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(entry, dest)


def _sanitize_module_name(name: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9_]", "_", name)
    if cleaned and cleaned[0].isdigit():
        cleaned = f"fn_{cleaned}"
    return f"{cleaned}_fn"


def _sanitize_handler_name(name: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9_]", "_", name)
    if cleaned and cleaned[0].isdigit():
        cleaned = f"fn_{cleaned}"
    return f"handle_{cleaned}"


def _sanitize_route(name: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9_-]", "-", name).strip("-")
    return cleaned or "function"


def _render_function_app(entries: Iterable[AzureFunctionEntry]) -> str:
    lines = [
        "import azure.functions as func",
        "import logging",
        "",
        "app = func.FunctionApp()",
        "",
    ]

    for entry in entries:
        lines.append(f"import {entry.module_name} as {entry.handler_name}_mod")
    lines.append("")

    for entry in entries:
        lines.extend(
            [
                f"@app.route(route=\"{entry.route}\", auth_level=func.AuthLevel.FUNCTION)",
                f"def {entry.handler_name}(req: func.HttpRequest) -> func.HttpResponse:",
                f"    logging.info(\"HTTP trigger {entry.route} received a request.\")",
                "    try:",
                f"        {entry.handler_name}_mod.fn(None, None)",
                "        return func.HttpResponse(\"OK\")",
                "    except Exception as exc:",
                "        logging.exception(\"HTTP trigger failed.\")",
                "        return func.HttpResponse(str(exc), status_code=500)",
                "",
            ]
        )

    return "\n".join(lines).rstrip() + "\n"

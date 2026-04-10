from __future__ import annotations

import csv
import json
import subprocess
import urllib.parse
import xml.etree.ElementTree as et
import zipfile
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_EXTERNAL_KB_DIR = BASE_DIR / "knowledge_base" / "raw"
SUPPORTED_EXTENSIONS = {".pdf", ".txt", ".docx", ".json", ".csv", ".md"}


def _normalize_text(raw: str) -> str:
    return " ".join(raw.split()).strip()


def _read_text_file(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def _read_csv_file(path: Path) -> str:
    lines: list[str] = []
    with path.open("r", encoding="utf-8", errors="ignore", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            row_text = ", ".join(item.strip() for item in row if item.strip())
            if row_text:
                lines.append(row_text)
    return "\n".join(lines)


def _json_to_lines(data: Any, prefix: str = "") -> list[str]:
    if isinstance(data, dict):
        lines: list[str] = []
        for key, value in data.items():
            next_prefix = f"{prefix}.{key}" if prefix else str(key)
            lines.extend(_json_to_lines(value, next_prefix))
        return lines
    if isinstance(data, list):
        lines: list[str] = []
        for index, value in enumerate(data, start=1):
            next_prefix = f"{prefix}[{index}]"
            lines.extend(_json_to_lines(value, next_prefix))
        return lines
    if data is None:
        return []

    value = str(data).strip()
    if not value:
        return []
    if prefix:
        return [f"{prefix}: {value}"]
    return [value]


def _read_json_file(path: Path) -> str:
    with path.open("r", encoding="utf-8", errors="ignore") as file:
        data = json.load(file)
    return "\n".join(_json_to_lines(data))


def _read_docx_file(path: Path) -> str:
    namespace = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    with zipfile.ZipFile(path) as archive:
        xml_bytes = archive.read("word/document.xml")
    root = et.fromstring(xml_bytes)
    texts = [node.text for node in root.findall(".//w:t", namespace) if node.text]
    return "\n".join(texts)


def _read_pdf_file(path: Path) -> str:
    try:
        from pypdf import PdfReader  # type: ignore

        reader = PdfReader(str(path))
        pages = [page.extract_text() or "" for page in reader.pages]
        return "\n".join(pages)
    except ImportError:
        pass
    except Exception:
        pass

    try:
        result = subprocess.run(
            ["pdftotext", str(path), "-"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout
    except Exception as err:
        raise RuntimeError("PDF 解析失败，请安装 pypdf 或确保系统可用 pdftotext。") from err


def _extract_text(path: Path) -> str:
    extension = path.suffix.lower()
    if extension in {".txt", ".md"}:
        return _read_text_file(path)
    if extension == ".csv":
        return _read_csv_file(path)
    if extension == ".json":
        return _read_json_file(path)
    if extension == ".docx":
        return _read_docx_file(path)
    if extension == ".pdf":
        return _read_pdf_file(path)
    return ""


def load_external_knowledge_documents(base_dir: str | Path | None = None) -> list[dict[str, Any]]:
    kb_dir = Path(base_dir) if base_dir else DEFAULT_EXTERNAL_KB_DIR
    if not kb_dir.exists():
        return []

    documents: list[dict[str, Any]] = []
    for path in sorted(kb_dir.rglob("*")):
        if not path.is_file():
            continue
        extension = path.suffix.lower()
        if extension not in SUPPORTED_EXTENSIONS:
            continue
        text = _normalize_text(_extract_text(path))
        if not text:
            continue

        relative = path.relative_to(kb_dir).as_posix()
        documents.append(
            {
                "source_type": "external",
                "source": f"外部知识库 · {relative}",
                "link": f"/assistant?kb={urllib.parse.quote(relative)}",
                "content": text,
                "metadata": {"relative_path": relative, "format": extension.lstrip(".")},
            }
        )
    return documents

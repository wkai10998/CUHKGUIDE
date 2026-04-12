from __future__ import annotations

from pathlib import Path
from typing import Any

from utils.content_loader import get_guides, get_programs

BASE_DIR = Path(__file__).resolve().parent.parent
RAG_TEXT_PATH = BASE_DIR / "content" / "rag_kb.txt"


def _load_rag_text() -> str:
    if not RAG_TEXT_PATH.exists():
        return ""
    text = RAG_TEXT_PATH.read_text(encoding="utf-8", errors="ignore")
    return " ".join(text.split()).strip()


def build_knowledge_chunks() -> list[dict[str, Any]]:
    chunks: list[dict[str, Any]] = []

    for program in get_programs():
        summary = (
            f"{program['name']}，学院：{program['school']}，"
            f"方向：{program['focus']}，截止日期：{program['deadline']}，"
            f"语言要求：{program['language']}"
        )
        chunks.append(
            {
                "source_type": "program",
                "source": f"专业速查 · {program['name']}",
                "link": "/programs",
                "content": summary,
            }
        )

    for stage_slug, stage in get_guides().items():
        for step in stage["steps"]:
            content = " ".join(step["tutorial"]) + " " + " ".join(step["notes"])
            chunks.append(
                {
                    "source_type": "guide",
                    "source": f"操作步骤 · {stage['title']} / {step['title']}",
                    "link": f"/guide/{stage_slug}?step={step['id']}",
                    "content": content,
                }
            )

    rag_text = _load_rag_text()
    if rag_text:
        chunks.append(
            {
                "source_type": "external",
                "source": "官方知识库",
                "link": "/assistant",
                "content": rag_text,
            }
        )

    return chunks

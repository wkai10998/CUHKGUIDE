from __future__ import annotations

from typing import Any

from utils.content_loader import get_faqs, get_guides, get_programs


def build_knowledge_chunks() -> list[dict[str, Any]]:
    chunks: list[dict[str, Any]] = []

    for faq in get_faqs():
        chunks.append(
            {
                "source_type": "faq",
                "source": f"常见问题 · {faq['question']}",
                "link": f"/faq/{faq['id']}",
                "content": str(faq["answer"]),
            }
        )

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

    return chunks

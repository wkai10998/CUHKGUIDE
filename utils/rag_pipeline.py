from __future__ import annotations

import hashlib
import os
from typing import Any

from utils import supabase_client, zhipu_client
from utils.knowledge_base import build_knowledge_chunks

DEFAULT_CHUNK_SIZE = 420
DEFAULT_CHUNK_OVERLAP = 80
ALLOWED_SOURCE_TYPES = {"program", "guide", "external"}


def _get_int_env(name: str, fallback: int) -> int:
    raw = os.environ.get(name, "").strip()
    if not raw:
        return fallback
    try:
        return int(raw)
    except ValueError:
        return fallback


def _get_float_env(name: str, fallback: float) -> float:
    raw = os.environ.get(name, "").strip()
    if not raw:
        return fallback
    try:
        return float(raw)
    except ValueError:
        return fallback


def is_rag_runtime_ready() -> bool:
    return supabase_client.is_supabase_enabled() and zhipu_client.is_zhipu_enabled()


def split_text(text: str, chunk_size: int, overlap: int) -> list[str]:
    content = " ".join(text.split())
    if not content:
        return []

    normalized_chunk_size = max(1, int(chunk_size))
    normalized_overlap = max(0, min(int(overlap), normalized_chunk_size - 1))
    if len(content) <= normalized_chunk_size:
        return [content]

    step = max(1, normalized_chunk_size - normalized_overlap)
    chunks: list[str] = []
    start = 0
    while start < len(content):
        end = min(len(content), start + normalized_chunk_size)
        piece = content[start:end].strip()
        if piece:
            chunks.append(piece)
        if end >= len(content):
            break
        start += step
    return chunks


def build_rag_records(
    chunk_size: int | None = None,
    overlap: int | None = None,
) -> list[dict[str, Any]]:
    normalized_chunk_size = chunk_size or _get_int_env("RAG_CHUNK_SIZE", DEFAULT_CHUNK_SIZE)
    normalized_overlap = overlap if overlap is not None else _get_int_env("RAG_CHUNK_OVERLAP", DEFAULT_CHUNK_OVERLAP)

    records: list[dict[str, Any]] = []
    for chunk in build_knowledge_chunks():
        text = str(chunk.get("content", "")).strip()
        if not text:
            continue
        pieces = split_text(text, normalized_chunk_size, normalized_overlap)
        for piece_index, piece in enumerate(pieces):
            uid_seed = (
                f"{chunk.get('source_type', 'general')}|{chunk.get('source', '')}|"
                f"{chunk.get('link', '')}|{piece_index}|{piece}"
            )
            chunk_uid = hashlib.sha1(uid_seed.encode("utf-8")).hexdigest()
            records.append(
                {
                    "chunk_uid": chunk_uid,
                    "source": str(chunk.get("source", "未知来源")),
                    "link": str(chunk.get("link", "/")),
                    "source_type": str(chunk.get("source_type", "general")),
                    "content": piece,
                    "metadata": {"piece_index": piece_index},
                }
            )
    return records


def _embedding_literal(values: list[float]) -> str:
    parts = [format(float(value), ".10f").rstrip("0").rstrip(".") for value in values]
    normalized = [item if item else "0" for item in parts]
    return "[" + ",".join(normalized) + "]"


def _normalize_source_type(value: object) -> str:
    return str(value or "").strip().lower()


def _normalize_match(item: dict[str, object]) -> dict[str, object] | None:
    source_type = _normalize_source_type(item.get("source_type"))
    if source_type not in ALLOWED_SOURCE_TYPES:
        return None

    source = str(item.get("source", "未知来源")).strip() or "未知来源"
    link = str(item.get("link", "")).strip()

    if source_type == "program":
        link = link if link.startswith("/programs") else "/programs"
    elif source_type == "guide":
        link = link if link.startswith("/guide") else "/guide"
    else:
        source = "官方知识库"
        link = "/assistant"

    return {
        "source_type": source_type,
        "source": source,
        "link": link,
        "content": str(item.get("content", "")).strip(),
        "similarity": float(item.get("similarity", 0.0)),
    }


def ingest_knowledge_base(
    chunk_size: int | None = None,
    overlap: int | None = None,
    batch_size: int = 32,
) -> dict[str, int]:
    if not is_rag_runtime_ready():
        raise RuntimeError("请先配置 SUPABASE_* 和 ZHIPU_API_KEY，再执行向量入库。")

    records = build_rag_records(
        chunk_size=chunk_size,
        overlap=overlap,
    )
    if not records:
        return {"records": 0, "upserted": 0}

    embedding_dim = _get_int_env("RAG_EMBEDDING_DIM", 1024)
    safe_batch_size = max(1, min(64, int(batch_size)))

    upserted = 0
    for index in range(0, len(records), safe_batch_size):
        batch = records[index : index + safe_batch_size]
        batch_text = [str(item["content"]) for item in batch]
        vectors = zhipu_client.create_embeddings(batch_text, dimensions=embedding_dim)

        payload: list[dict[str, object]] = []
        for item, vector in zip(batch, vectors):
            payload.append(
                {
                    "chunk_uid": item["chunk_uid"],
                    "source": item["source"],
                    "link": item["link"],
                    "source_type": item["source_type"],
                    "content": item["content"],
                    "metadata": item["metadata"],
                    "embedding": _embedding_literal(vector),
                }
            )
        upserted += supabase_client.upsert_rag_chunks(payload)

    return {"records": len(records), "upserted": upserted}


def ask_with_rag(question: str) -> tuple[str, list[dict[str, str]]]:
    prompt = question.strip()
    if len(prompt) < 2:
        return "问题太短了，请补充更具体的需求，例如“推荐信要提前多久联系老师？”。", []

    if not is_rag_runtime_ready():
        raise RuntimeError("RAG 运行依赖未配置完成。")

    embedding_dim = _get_int_env("RAG_EMBEDDING_DIM", 1024)
    top_k = max(1, _get_int_env("RAG_TOP_K", 2))
    min_similarity = _get_float_env("RAG_MIN_SIMILARITY", 0.45)
    context_char_limit = _get_int_env("RAG_CONTEXT_CHAR_LIMIT", 220)
    candidate_count = max(top_k * 4, top_k + 6)

    query_vector = zhipu_client.create_embeddings([prompt], dimensions=embedding_dim)[0]
    raw_matches = supabase_client.match_rag_chunks(
        query_embedding=query_vector,
        match_count=candidate_count,
        min_similarity=min_similarity,
    )

    if not raw_matches:
        return (
            "我没有在当前知识库检索到直接证据。你可以补充更具体关键词（专业名、材料名、时间点）后再试。",
            [],
        )

    matches: list[dict[str, object]] = []
    for item in raw_matches:
        if not isinstance(item, dict):
            continue
        normalized = _normalize_match(item)
        if normalized is None:
            continue
        matches.append(normalized)
        if len(matches) >= top_k:
            break

    if not matches:
        return (
            "我没有在当前知识库检索到直接证据。你可以补充更具体关键词（专业名、材料名、时间点）后再试。",
            [],
        )

    context_lines: list[str] = []
    sources: list[dict[str, str]] = []
    seen_source: set[str] = set()
    for index, item in enumerate(matches, start=1):
        source_type = str(item.get("source_type", "")).strip().lower()
        source = str(item.get("source", "未知来源"))
        link = str(item.get("link", "/assistant"))
        if source_type == "external":
            source = "官方知识库"
            link = "/assistant"
        content = str(item.get("content", "")).strip()
        if context_char_limit > 0 and len(content) > context_char_limit:
            content = content[:context_char_limit].rstrip() + "..."
        similarity = float(item.get("similarity", 0.0))
        context_lines.append(
            f"[{index}] 来源: {source}\n"
            f"链接: {link}\n"
            f"相关度: {similarity:.3f}\n"
            f"片段: {content}"
        )
        source_key = f"{source}|{link}"
        if source_key not in seen_source:
            sources.append({"source": source, "link": link})
            seen_source.add(source_key)

    system_prompt = (
        "你是港中文申请助手。请只基于给定上下文回答。"
        "如果上下文不足，明确说“未检索到证据”，不要编造。"
        "优先输出简短结论，控制在 1-3 句。"
    )
    user_prompt = (
        f"用户问题：{prompt}\n\n"
        "检索上下文：\n"
        f"{chr(10).join(context_lines)}\n\n"
        "请按顺序输出：1) 结论（先给明确答案）2) 关键依据（最多 2 点）3) 风险提示（可选）。"
    )
    answer = zhipu_client.generate_answer(system_prompt=system_prompt, user_prompt=user_prompt)
    return answer, sources[:3]

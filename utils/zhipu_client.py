from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from typing import Any

ZHIPU_TIMEOUT_SECONDS = 30
ZHIPU_BASE_URL = "https://open.bigmodel.cn/api/paas/v4"


def _get_config() -> dict[str, str]:
    api_key = os.environ.get("ZHIPU_API_KEY", "").strip()
    base_url = os.environ.get("ZHIPU_API_BASE", ZHIPU_BASE_URL).strip().rstrip("/")
    embedding_model = os.environ.get("ZHIPU_EMBEDDING_MODEL", "embedding-3").strip() or "embedding-3"
    chat_model = os.environ.get("ZHIPU_CHAT_MODEL", "glm-4-flash").strip() or "glm-4-flash"
    return {
        "api_key": api_key,
        "base_url": base_url,
        "embedding_model": embedding_model,
        "chat_model": chat_model,
    }


def is_zhipu_enabled() -> bool:
    config = _get_config()
    return bool(config["api_key"] and config["base_url"])


def _post_json(path: str, payload: dict[str, Any]) -> dict[str, Any]:
    config = _get_config()
    if not config["api_key"]:
        raise RuntimeError("ZHIPU_API_KEY 未配置。")

    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    url = f"{config['base_url']}/{path.lstrip('/')}"
    headers = {
        "Authorization": f"Bearer {config['api_key']}",
        "Content-Type": "application/json",
    }
    request_obj = urllib.request.Request(url, data=body, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(request_obj, timeout=ZHIPU_TIMEOUT_SECONDS) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        error_text = err.read().decode("utf-8", errors="ignore")
        raise RuntimeError(f"智谱 API 调用失败（HTTP {err.code}）：{error_text}") from err
    except (urllib.error.URLError, json.JSONDecodeError) as err:
        raise RuntimeError("智谱 API 调用失败，请检查网络或 API Key 配置。") from err

    if not isinstance(data, dict):
        raise RuntimeError("智谱 API 返回格式异常。")
    return data


def create_embeddings(texts: list[str], dimensions: int | None = None) -> list[list[float]]:
    if not texts:
        return []
    if len(texts) > 64:
        raise ValueError("embedding 单次最多 64 条文本，请分批请求。")

    config = _get_config()
    payload: dict[str, Any] = {
        "model": config["embedding_model"],
        "input": texts,
    }
    if dimensions is not None:
        payload["dimensions"] = dimensions

    data = _post_json("embeddings", payload)
    rows = data.get("data", [])
    if not isinstance(rows, list):
        raise RuntimeError("智谱 embedding 返回数据异常。")

    vectors: list[list[float]] = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        embedding = row.get("embedding")
        if not isinstance(embedding, list):
            continue
        vector = [float(value) for value in embedding]
        vectors.append(vector)

    if len(vectors) != len(texts):
        raise RuntimeError("embedding 返回条数与输入不一致。")
    return vectors


def generate_answer(system_prompt: str, user_prompt: str, temperature: float = 0.2) -> str:
    config = _get_config()
    payload: dict[str, Any] = {
        "model": config["chat_model"],
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": temperature,
    }
    data = _post_json("chat/completions", payload)

    choices = data.get("choices", [])
    if not isinstance(choices, list) or not choices:
        raise RuntimeError("智谱对话模型返回为空。")

    first = choices[0]
    if not isinstance(first, dict):
        raise RuntimeError("智谱对话模型返回格式异常。")
    message = first.get("message", {})
    if not isinstance(message, dict):
        raise RuntimeError("智谱对话模型返回 message 异常。")
    content = message.get("content", "")
    if not isinstance(content, str) or not content.strip():
        raise RuntimeError("智谱对话模型未返回有效文本。")
    return content.strip()

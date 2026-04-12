from __future__ import annotations

import json
import os
import socket
import time
import urllib.error
import urllib.request
from typing import Any

DEFAULT_ZHIPU_TIMEOUT_SECONDS = 22
DEFAULT_ZHIPU_CHAT_MAX_TOKENS = 512
DEFAULT_ZHIPU_CHAT_RETRIES = 1
DEFAULT_ZHIPU_RETRY_DELAY_SECONDS = 0.35
ZHIPU_BASE_URL = "https://open.bigmodel.cn/api/paas/v4"


def _get_config() -> dict[str, str]:
    api_key = os.environ.get("ZHIPU_API_KEY", "").strip()
    base_url = os.environ.get("ZHIPU_API_BASE", ZHIPU_BASE_URL).strip().rstrip("/")
    embedding_model = os.environ.get("ZHIPU_EMBEDDING_MODEL", "embedding-3").strip() or "embedding-3"
    chat_model = os.environ.get("ZHIPU_CHAT_MODEL", "GLM-4.5-AirX").strip() or "GLM-4.5-AirX"
    return {
        "api_key": api_key,
        "base_url": base_url,
        "embedding_model": embedding_model,
        "chat_model": chat_model,
    }


def is_zhipu_enabled() -> bool:
    config = _get_config()
    return bool(config["api_key"] and config["base_url"])


def _get_timeout_seconds() -> float:
    raw = os.environ.get("ZHIPU_TIMEOUT_SECONDS", "").strip()
    if not raw:
        return float(DEFAULT_ZHIPU_TIMEOUT_SECONDS)
    try:
        value = float(raw)
    except ValueError:
        return float(DEFAULT_ZHIPU_TIMEOUT_SECONDS)
    return value if value > 0 else float(DEFAULT_ZHIPU_TIMEOUT_SECONDS)


def _get_chat_max_tokens() -> int:
    raw = os.environ.get("ZHIPU_CHAT_MAX_TOKENS", "").strip()
    if not raw:
        return DEFAULT_ZHIPU_CHAT_MAX_TOKENS
    try:
        value = int(raw)
    except ValueError:
        return DEFAULT_ZHIPU_CHAT_MAX_TOKENS
    return max(64, min(4096, value))


def _get_chat_retries() -> int:
    raw = os.environ.get("ZHIPU_CHAT_RETRIES", "").strip()
    if not raw:
        return DEFAULT_ZHIPU_CHAT_RETRIES
    try:
        value = int(raw)
    except ValueError:
        return DEFAULT_ZHIPU_CHAT_RETRIES
    return max(0, min(2, value))


def _post_json(path: str, payload: dict[str, Any], retries: int = 0) -> dict[str, Any]:
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

    max_attempts = max(1, retries + 1)
    timeout_seconds = _get_timeout_seconds()
    last_err: Exception | None = None
    for attempt in range(max_attempts):
        try:
            with urllib.request.urlopen(request_obj, timeout=timeout_seconds) as response:
                data = json.loads(response.read().decode("utf-8"))
            if not isinstance(data, dict):
                raise RuntimeError("智谱 API 返回格式异常。")
            return data
        except urllib.error.HTTPError as err:
            error_text = err.read().decode("utf-8", errors="ignore")
            raise RuntimeError(f"智谱 API 调用失败（HTTP {err.code}）：{error_text}") from err
        except (TimeoutError, socket.timeout, urllib.error.URLError) as err:
            last_err = err
            if attempt < max_attempts - 1:
                time.sleep(DEFAULT_ZHIPU_RETRY_DELAY_SECONDS)
                continue
        except json.JSONDecodeError as err:
            raise RuntimeError("智谱 API 调用失败，返回内容无法解析。") from err

    if isinstance(last_err, (TimeoutError, socket.timeout)):
        raise RuntimeError("智谱 API 请求超时，请稍后重试。") from last_err
    raise RuntimeError("智谱 API 调用失败，请检查网络或 API Key 配置。") from last_err


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
        "max_tokens": _get_chat_max_tokens(),
    }
    data = _post_json("chat/completions", payload, retries=_get_chat_retries())

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

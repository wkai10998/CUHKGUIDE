from __future__ import annotations

import json
import os
import urllib.error
import urllib.parse
import urllib.request

from werkzeug.security import generate_password_hash

SUPABASE_TIMEOUT_SECONDS = 8


def _get_config() -> dict[str, str]:
    url = os.environ.get("SUPABASE_URL", "").strip().rstrip("/")
    key = (
        os.environ.get("SUPABASE_SERVICE_ROLE_KEY", "").strip()
        or os.environ.get("SUPABASE_ANON_KEY", "").strip()
    )
    comments_table = os.environ.get("SUPABASE_COMMENTS_TABLE", "comments").strip() or "comments"
    users_table = os.environ.get("SUPABASE_USERS_TABLE", "users").strip() or "users"
    rag_upsert_rpc = os.environ.get("SUPABASE_RAG_UPSERT_RPC", "upsert_rag_chunks").strip() or "upsert_rag_chunks"
    rag_match_rpc = os.environ.get("SUPABASE_RAG_MATCH_RPC", "match_rag_chunks").strip() or "match_rag_chunks"
    return {
        "url": url,
        "key": key,
        "comments_table": comments_table,
        "users_table": users_table,
        "rag_upsert_rpc": rag_upsert_rpc,
        "rag_match_rpc": rag_match_rpc,
    }


def is_supabase_enabled() -> bool:
    config = _get_config()
    return bool(config["url"] and config["key"])


def _build_headers(key: str, include_json: bool = False) -> dict[str, str]:
    if not key:
        raise RuntimeError("SUPABASE key is missing")

    headers = {
        "apikey": key,
        "Authorization": f"Bearer {key}",
    }
    if include_json:
        headers["Content-Type"] = "application/json"
    return headers


def _post_rpc(rpc_name: str, payload: dict[str, object]) -> object:
    config = _get_config()
    if not is_supabase_enabled():
        raise RuntimeError("Supabase is not configured")

    url = f"{config['url']}/rest/v1/rpc/{rpc_name}"
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    headers = _build_headers(config["key"], include_json=True)
    request_obj = urllib.request.Request(url, data=body, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(request_obj, timeout=SUPABASE_TIMEOUT_SECONDS) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.HTTPError as err:
        error_text = err.read().decode("utf-8", errors="ignore")
        raise RuntimeError(error_text or f"Supabase RPC `{rpc_name}` 调用失败。") from err
    except urllib.error.URLError as err:
        raise RuntimeError(f"Supabase RPC `{rpc_name}` 调用失败，请检查网络配置。") from err

    if not raw:
        return None

    try:
        return json.loads(raw)
    except json.JSONDecodeError as err:
        raise RuntimeError(f"Supabase RPC `{rpc_name}` 返回格式异常。") from err


def _vector_literal(values: list[float]) -> str:
    if not values:
        raise ValueError("向量不能为空")
    parts = [format(float(value), ".10f").rstrip("0").rstrip(".") for value in values]
    normalized = [item if item else "0" for item in parts]
    return "[" + ",".join(normalized) + "]"


def list_comments(page_type: str, page_key: str) -> list[dict[str, object]]:
    config = _get_config()
    if not is_supabase_enabled():
        raise RuntimeError("Supabase comments is not configured")

    query = (
        "select=id,user_id,user_name,avatar_seed,content,created_at"
        f"&page_type=eq.{urllib.parse.quote(page_type, safe='')}"
        f"&page_key=eq.{urllib.parse.quote(page_key, safe='')}"
        "&order=id.desc"
    )
    url = f"{config['url']}/rest/v1/{config['comments_table']}?{query}"
    request_obj = urllib.request.Request(url, headers=_build_headers(config["key"]))

    try:
        with urllib.request.urlopen(request_obj, timeout=SUPABASE_TIMEOUT_SECONDS) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        error_text = err.read().decode("utf-8", errors="ignore")
        if "comments.user_id does not exist" in error_text:
            raise RuntimeError("Supabase comments 表缺少 user_id 字段，请执行 docs/supabase_comments.sql。") from err
        raise RuntimeError("读取评论失败，请检查 Supabase comments 表配置。") from err
    except (urllib.error.URLError, json.JSONDecodeError) as err:
        raise RuntimeError("读取评论失败，请检查网络与 Supabase 配置。") from err

    if not isinstance(data, list):
        raise RuntimeError("Supabase comments response is invalid")

    normalized: list[dict[str, object]] = []
    for row in data:
        if not isinstance(row, dict):
            continue
        normalized.append(
            {
                "id": row.get("id", 0),
                "user_id": row.get("user_id", ""),
                "user_name": row.get("user_name", "游客"),
                "avatar_seed": row.get("avatar_seed", "sky"),
                "content": row.get("content", ""),
                "created_at": row.get("created_at", ""),
            }
        )
    return normalized


def create_comment(
    page_type: str,
    page_key: str,
    user_id: str,
    user_name: str,
    avatar_seed: str,
    content: str,
    created_at: str,
) -> None:
    config = _get_config()
    if not is_supabase_enabled():
        raise RuntimeError("Supabase comments is not configured")

    payload = {
        "page_type": page_type,
        "page_key": page_key,
        "user_id": user_id,
        "user_name": user_name,
        "avatar_seed": avatar_seed,
        "content": content,
        "created_at": created_at,
    }
    body = json.dumps(payload).encode("utf-8")
    headers = _build_headers(config["key"], include_json=True)
    headers["Prefer"] = "return=minimal"

    url = f"{config['url']}/rest/v1/{config['comments_table']}"
    request_obj = urllib.request.Request(url, data=body, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(request_obj, timeout=SUPABASE_TIMEOUT_SECONDS) as response:
            response.read()
    except urllib.error.HTTPError as err:
        error_text = err.read().decode("utf-8", errors="ignore")
        if "comments.user_id does not exist" in error_text:
            raise RuntimeError("Supabase comments 表缺少 user_id 字段，请执行 docs/supabase_comments.sql。") from err
        raise RuntimeError("评论写入失败，请检查 Supabase comments 表配置。") from err
    except urllib.error.URLError as err:
        raise RuntimeError("评论写入失败，请检查网络与 Supabase 配置。") from err


def get_user_by_email(email: str) -> dict[str, object] | None:
    config = _get_config()
    if not is_supabase_enabled():
        raise RuntimeError("Supabase is not configured")

    query = (
        "select=id,name,email,password_hash,avatar_seed"
        f"&email=eq.{urllib.parse.quote(email, safe='')}"
        "&limit=1"
    )
    url = f"{config['url']}/rest/v1/{config['users_table']}?{query}"
    request_obj = urllib.request.Request(url, headers=_build_headers(config["key"]))

    try:
        with urllib.request.urlopen(request_obj, timeout=SUPABASE_TIMEOUT_SECONDS) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        error_text = err.read().decode("utf-8", errors="ignore")
        if "Could not find the table 'public.users'" in error_text:
            raise RuntimeError("Supabase 缺少 users 表，请执行 docs/supabase_comments.sql。") from err
        raise RuntimeError("读取用户失败，请检查 Supabase users 表配置。") from err
    except (urllib.error.URLError, json.JSONDecodeError) as err:
        raise RuntimeError("读取用户失败，请检查网络与 Supabase 配置。") from err

    if not isinstance(data, list):
        raise RuntimeError("Supabase user response is invalid")
    if not data:
        return None

    user = data[0]
    if not isinstance(user, dict):
        return None
    return user


def create_user(name: str, email: str, password: str, avatar_seed: str) -> dict[str, object]:
    config = _get_config()
    if not is_supabase_enabled():
        raise RuntimeError("Supabase is not configured")

    payload = {
        "name": name,
        "email": email,
        "password_hash": generate_password_hash(password),
        "avatar_seed": avatar_seed,
    }
    headers = _build_headers(config["key"], include_json=True)
    headers["Prefer"] = "return=representation"
    body = json.dumps(payload).encode("utf-8")
    url = f"{config['url']}/rest/v1/{config['users_table']}"
    request_obj = urllib.request.Request(url, data=body, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(request_obj, timeout=SUPABASE_TIMEOUT_SECONDS) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        error_text = err.read().decode("utf-8", errors="ignore")
        if "Could not find the table 'public.users'" in error_text:
            raise RuntimeError("Supabase 缺少 users 表，请执行 docs/supabase_comments.sql。") from err
        if "duplicate key value" in error_text or "unique" in error_text:
            raise ValueError("该邮箱已注册，请直接登录。") from err
        raise RuntimeError("注册失败，请检查 Supabase users 表配置。") from err
    except (urllib.error.URLError, json.JSONDecodeError) as err:
        raise RuntimeError("注册失败，请检查网络与 Supabase 配置。") from err

    if not isinstance(data, list) or not data or not isinstance(data[0], dict):
        raise RuntimeError("Supabase register response is invalid")
    return data[0]


def update_user_profile(user_id: str, name: str, avatar_seed: str) -> dict[str, object]:
    config = _get_config()
    if not is_supabase_enabled():
        raise RuntimeError("Supabase is not configured")
    if not user_id:
        raise RuntimeError("用户 ID 为空，无法更新资料。")

    payload = {
        "name": name,
        "avatar_seed": avatar_seed,
    }
    body = json.dumps(payload).encode("utf-8")
    headers = _build_headers(config["key"], include_json=True)
    headers["Prefer"] = "return=representation"

    user_id_filter = urllib.parse.quote(user_id, safe="")
    url = f"{config['url']}/rest/v1/{config['users_table']}?id=eq.{user_id_filter}"
    request_obj = urllib.request.Request(url, data=body, headers=headers, method="PATCH")

    try:
        with urllib.request.urlopen(request_obj, timeout=SUPABASE_TIMEOUT_SECONDS) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        error_text = err.read().decode("utf-8", errors="ignore")
        if "Could not find the table 'public.users'" in error_text:
            raise RuntimeError("Supabase 缺少 users 表，请执行 docs/supabase_comments.sql。") from err
        raise RuntimeError("更新资料失败，请检查 Supabase users 表配置。") from err
    except (urllib.error.URLError, json.JSONDecodeError) as err:
        raise RuntimeError("更新资料失败，请检查网络与 Supabase 配置。") from err

    if not isinstance(data, list):
        raise RuntimeError("Supabase profile response is invalid")

    if data and isinstance(data[0], dict):
        return data[0]

    return {"id": user_id, "name": name, "avatar_seed": avatar_seed}


def upsert_rag_chunks(rows: list[dict[str, object]]) -> int:
    if not rows:
        return 0

    config = _get_config()
    try:
        result = _post_rpc(config["rag_upsert_rpc"], {"payload": rows})
    except RuntimeError as err:
        message = str(err)
        if "upsert_rag_chunks" in message or "function" in message:
            raise RuntimeError("Supabase 缺少 RAG RPC，请先执行 docs/supabase_rag.sql。") from err
        raise RuntimeError(f"写入 RAG 向量失败：{message}") from err

    if isinstance(result, int):
        return result
    if isinstance(result, float):
        return int(result)
    return len(rows)


def match_rag_chunks(
    query_embedding: list[float],
    match_count: int = 4,
    min_similarity: float = 0.45,
) -> list[dict[str, object]]:
    config = _get_config()
    payload = {
        "query_embedding": _vector_literal(query_embedding),
        "match_count": max(1, int(match_count)),
        "min_similarity": float(min_similarity),
    }

    try:
        result = _post_rpc(config["rag_match_rpc"], payload)
    except RuntimeError as err:
        message = str(err)
        if "match_rag_chunks" in message or "function" in message:
            raise RuntimeError("Supabase 缺少 RAG 检索 RPC，请先执行 docs/supabase_rag.sql。") from err
        raise RuntimeError(f"RAG 检索失败：{message}") from err

    if not isinstance(result, list):
        raise RuntimeError("RAG 检索结果格式异常。")

    normalized: list[dict[str, object]] = []
    for row in result:
        if not isinstance(row, dict):
            continue
        normalized.append(
            {
                "chunk_uid": row.get("chunk_uid", ""),
                "source": row.get("source", ""),
                "link": row.get("link", ""),
                "source_type": row.get("source_type", ""),
                "content": row.get("content", ""),
                "similarity": float(row.get("similarity", 0.0)),
            }
        )
    return normalized

from __future__ import annotations

import os
import sqlite3
from datetime import datetime
from pathlib import Path

from flask import (
    Flask,
    abort,
    flash,
    g,
    make_response,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from data.stages import STAGES
from data.questions import QUESTIONS
from data.guides import GUIDE_DATA

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-secret-change-me")

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "app.db"


def get_db() -> sqlite3.Connection:
    if "db" not in g:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db


def init_db() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS comments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                page_type TEXT NOT NULL,
                page_key TEXT NOT NULL,
                user_name TEXT NOT NULL,
                avatar_seed TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )
        conn.commit()


def close_db(_err: Exception | None = None) -> None:
    db = g.pop("db", None)
    if db is not None:
        db.close()


def get_current_user() -> dict[str, str]:
    name = session.get("user_name", "游客")
    avatar_seed = session.get("avatar_seed", "sky")
    return {
        "name": name,
        "avatar_seed": avatar_seed,
        "initial": (name[:1] if name else "游"),
    }


def list_comments(page_type: str, page_key: str) -> list[sqlite3.Row]:
    db = get_db()
    rows = db.execute(
        """
        SELECT id, user_name, avatar_seed, content, created_at
        FROM comments
        WHERE page_type = ? AND page_key = ?
        ORDER BY id DESC
        """,
        (page_type, page_key),
    ).fetchall()
    return rows


def create_comment(page_type: str, page_key: str, content: str) -> None:
    text = content.strip()
    if not text:
        raise ValueError("评论内容不能为空")
    if len(text) > 500:
        raise ValueError("评论不能超过 500 字")

    user = get_current_user()
    db = get_db()
    db.execute(
        """
        INSERT INTO comments (page_type, page_key, user_name, avatar_seed, content, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            page_type,
            page_key,
            user["name"],
            user["avatar_seed"],
            text,
            datetime.now().strftime("%Y-%m-%d %H:%M"),
        ),
    )
    db.commit()


@app.context_processor
def inject_global_data() -> dict[str, object]:
    return {
        "current_user": get_current_user(),
        "stage_nav_items": STAGES,
        "avatar_colors": {
            "sky": "bg-sky-500",
            "emerald": "bg-emerald-500",
            "amber": "bg-amber-500",
            "rose": "bg-rose-500",
            "violet": "bg-violet-500",
        },
    }


@app.teardown_appcontext
def teardown_db(exception: Exception | None) -> None:
    close_db(exception)


@app.route("/")
def index():
    last_stage = request.cookies.get("last_stage", "")
    return render_template("index.html", stages=STAGES, last_stage=last_stage)


@app.route("/guide")
def guide_list():
    return render_template("guide_list.html", stages=STAGES)


@app.route("/profile", methods=["POST"])
def update_profile():
    name = request.form.get("user_name", "").strip()
    avatar_seed = request.form.get("avatar_seed", "sky").strip()

    allowed = {"sky", "emerald", "amber", "rose", "violet"}
    if avatar_seed not in allowed:
        avatar_seed = "sky"

    if name:
        session["user_name"] = name[:20]
    else:
        session["user_name"] = "游客"
    session["avatar_seed"] = avatar_seed

    flash("个人资料已更新", "success")
    return redirect(request.referrer or url_for("index"))


@app.route("/profile/reset", methods=["POST"])
def reset_profile():
    session.pop("user_name", None)
    session.pop("avatar_seed", None)
    flash("已恢复默认身份", "success")
    return redirect(request.referrer or url_for("index"))


@app.route("/qa")
def qa_list():
    return render_template("qa_list.html", questions=QUESTIONS)


@app.route("/qa/<int:q_id>")
def qa_detail(q_id: int):
    q = next((item for item in QUESTIONS if item["id"] == q_id), None)
    comments = list_comments("qa", str(q_id))
    return render_template("qa_detail.html", q=q, comments=comments)


@app.route("/qa/<int:q_id>/comment", methods=["POST"])
def qa_comment(q_id: int):
    try:
        create_comment("qa", str(q_id), request.form.get("content", ""))
        flash("评论已发布", "success")
    except ValueError as err:
        flash(str(err), "error")
    return redirect(url_for("qa_detail", q_id=q_id))


@app.route("/guide/<stage_slug>")
def guide(stage_slug: str):
    stage = GUIDE_DATA.get(stage_slug)
    if not stage:
        abort(404)

    step_id = request.args.get("step", 1, type=int)
    current_step = next((step for step in stage["steps"] if step["id"] == step_id), None)

    if current_step is None:
        current_step = stage["steps"][0]

    page_key = f"{stage_slug}:{current_step['id']}"
    comments = list_comments("guide", page_key)

    response = make_response(
        render_template(
            "guide.html",
            stage_slug=stage_slug,
            stage=stage,
            current_step=current_step,
            comments=comments,
        )
    )
    response.set_cookie("last_stage", stage_slug, max_age=60 * 60 * 24 * 14)
    return response


@app.route("/guide/<stage_slug>/comment", methods=["POST"])
def guide_comment(stage_slug: str):
    step_id = request.form.get("step_id", type=int, default=1)
    stage = GUIDE_DATA.get(stage_slug)
    if not stage:
        abort(404)

    valid_step = next((step for step in stage["steps"] if step["id"] == step_id), None)
    if not valid_step:
        valid_step = stage["steps"][0]
        step_id = valid_step["id"]

    page_key = f"{stage_slug}:{step_id}"

    try:
        create_comment("guide", page_key, request.form.get("content", ""))
        flash("评论已发布", "success")
    except ValueError as err:
        flash(str(err), "error")

    return redirect(url_for("guide", stage_slug=stage_slug, step=step_id))


@app.errorhandler(404)
def not_found(_error):
    return render_template("errors/404.html"), 404


@app.errorhandler(500)
def server_error(_error):
    return render_template("errors/500.html"), 500


init_db()

if __name__ == "__main__":
    app.run(debug=True)

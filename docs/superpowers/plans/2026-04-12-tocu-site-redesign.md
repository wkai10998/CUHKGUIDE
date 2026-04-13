# ToCU Site Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement the approved whole-site redesign for ToCU so the site follows `DESIGN.md`, ships a minimal cover-style homepage, moves the six-stage process overview to Guides, and unifies the core pages under one editorial visual system.

**Architecture:** Keep the existing Flask routes and data sources intact, and implement the redesign by reworking shared templates plus page templates and the main stylesheet. Preserve current app behaviors such as login/profile state, program search, guide progress tracking, comments, and assistant chat while reshaping layout, hierarchy, and page responsibilities.

**Tech Stack:** Flask, Jinja2 templates, Tailwind CDN config, custom CSS in `static/css/app.css`, existing vanilla JavaScript page scripts

---

## File Map

- Modify: `/Users/wkai/Desktop/FlaskProject/templates/base.html`
  Responsibility: update document fonts/theme config and main container behavior shared by all pages.
- Modify: `/Users/wkai/Desktop/FlaskProject/templates/header.html`
  Responsibility: redesign the sticky editorial header and account state UI.
- Modify: `/Users/wkai/Desktop/FlaskProject/templates/footer.html`
  Responsibility: simplify footer and move FAQ to secondary/supporting navigation.
- Modify: `/Users/wkai/Desktop/FlaskProject/templates/index.html`
  Responsibility: implement the minimal A1 cover-style homepage.
- Modify: `/Users/wkai/Desktop/FlaskProject/templates/programs.html`
  Responsibility: convert programs page into the calmer lookup directory layout.
- Modify: `/Users/wkai/Desktop/FlaskProject/templates/guide_list.html`
  Responsibility: make Guides the six-stage overview/default process page.
- Modify: `/Users/wkai/Desktop/FlaskProject/templates/guide.html`
  Responsibility: rebalance the detail page into a reading-first guide chapter.
- Modify: `/Users/wkai/Desktop/FlaskProject/templates/assistant.html`
  Responsibility: keep assistant light-themed and aligned with the shared visual system.
- Modify: `/Users/wkai/Desktop/FlaskProject/templates/faq.html`
  Responsibility: restyle FAQ as a secondary-supporting page in the same system.
- Modify: `/Users/wkai/Desktop/FlaskProject/templates/login.html`
  Responsibility: align the full login/register page with the redesigned surfaces.
- Modify: `/Users/wkai/Desktop/FlaskProject/templates/login_modal.html`
  Responsibility: align modal auth surfaces with the redesigned visual language.
- Modify: `/Users/wkai/Desktop/FlaskProject/static/css/app.css`
  Responsibility: replace the current purple-heavy visual layer with the `DESIGN.md` system and page-specific layout styles.
- Create: `/Users/wkai/Desktop/FlaskProject/tests/test_pages.py`
  Responsibility: add Flask view smoke tests that lock in the redesigned page structure and key navigation/content expectations.

### Task 1: Add page smoke tests for the redesigned IA

**Files:**
- Create: `/Users/wkai/Desktop/FlaskProject/tests/test_pages.py`
- Test: `/Users/wkai/Desktop/FlaskProject/tests/test_pages.py`

- [ ] **Step 1: Write the failing test**

```python
from app import app


def test_home_programs_guides_and_assistant_pages_render_key_navigation_and_content():
    client = app.test_client()

    home = client.get("/")
    programs = client.get("/programs")
    guides = client.get("/guide")
    assistant = client.get("/assistant")

    assert home.status_code == 200
    assert "ToCU" in home.get_data(as_text=True)
    assert "专业速查" in home.get_data(as_text=True)
    assert "操作步骤" in home.get_data(as_text=True)
    assert "智能助手" in home.get_data(as_text=True)

    assert programs.status_code == 200
    assert "专业速查" in programs.get_data(as_text=True)

    assert guides.status_code == 200
    assert "操作步骤" in guides.get_data(as_text=True)
    assert "Stage 01" in guides.get_data(as_text=True) or "01" in guides.get_data(as_text=True)

    assert assistant.status_code == 200
    assert "智能助手" in assistant.get_data(as_text=True)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_pages.py -v`
Expected: FAIL because `tests/test_pages.py` does not exist yet, then after creation should fail on missing assertions that the old templates do not satisfy consistently.

- [ ] **Step 3: Write minimal implementation**

Create the test file with the code above, using the Flask app test client and plain string assertions rather than brittle DOM parsing.

- [ ] **Step 4: Run test to verify it passes or fails for the right reason**

Run: `pytest tests/test_pages.py -v`
Expected: initial FAIL on real template output expectations, proving the redesign test is meaningful.

- [ ] **Step 5: Commit**

```bash
git add tests/test_pages.py
git commit -m "test: add page smoke tests for redesign"
```

### Task 2: Redesign shared shell, navigation, and footer

**Files:**
- Modify: `/Users/wkai/Desktop/FlaskProject/templates/base.html`
- Modify: `/Users/wkai/Desktop/FlaskProject/templates/header.html`
- Modify: `/Users/wkai/Desktop/FlaskProject/templates/footer.html`
- Modify: `/Users/wkai/Desktop/FlaskProject/static/css/app.css`
- Test: `/Users/wkai/Desktop/FlaskProject/tests/test_pages.py`

- [ ] **Step 1: Extend the failing test for shared shell expectations**

```python
def test_shared_shell_shows_four_primary_nav_items_and_supporting_footer_links():
    client = app.test_client()
    response = client.get("/")
    html = response.get_data(as_text=True)

    assert "首页" in html
    assert "专业速查" in html
    assert "操作步骤" in html
    assert "智能助手" in html
    assert "常见问题" in html
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_pages.py::test_shared_shell_shows_four_primary_nav_items_and_supporting_footer_links -v`
Expected: FAIL until the footer/header copy and structure are updated.

- [ ] **Step 3: Write minimal implementation**

Update shared templates so they use:

```html
<body class="tocu-body">
  {% include "header.html" %}
  <main class="tocu-site-shell {% if is_home %}tocu-site-shell-home{% endif %}">
    ...
  </main>
  {% include "login_modal.html" %}
  {% include "footer.html" %}
</body>
```

Use a four-item primary nav and make FAQ a secondary footer link. In CSS, add root tokens and shared classes such as:

```css
:root {
  --tocu-bg: #f5f4ed;
  --tocu-surface: #faf9f5;
  --tocu-surface-strong: #ffffff;
  --tocu-ink: #141413;
  --tocu-muted: #5e5d59;
  --tocu-subtle: #87867f;
  --tocu-border: #f0eee6;
  --tocu-border-strong: #e8e6dc;
  --tocu-accent: #c96442;
  --tocu-accent-strong: #b85637;
  --tocu-focus: #3898ec;
}
```

- [ ] **Step 4: Run tests to verify the shared shell passes**

Run: `pytest tests/test_pages.py -v`
Expected: shared-shell assertions pass, while page-specific redesign assertions may still fail until later tasks.

- [ ] **Step 5: Commit**

```bash
git add templates/base.html templates/header.html templates/footer.html static/css/app.css tests/test_pages.py
git commit -m "feat: redesign shared site shell"
```

### Task 3: Implement the minimal A1 cover homepage

**Files:**
- Modify: `/Users/wkai/Desktop/FlaskProject/templates/index.html`
- Modify: `/Users/wkai/Desktop/FlaskProject/static/css/app.css`
- Test: `/Users/wkai/Desktop/FlaskProject/tests/test_pages.py`

- [ ] **Step 1: Extend the failing test for homepage content**

```python
def test_homepage_uses_cover_style_message_without_timeline_overview():
    client = app.test_client()
    html = client.get("/").get_data(as_text=True)

    assert "港中文硕士申请信息服务平台" in html
    assert "把港中文硕士申请的时间、材料与步骤讲清楚" in html
    assert "进入专业速查" in html or "专业速查" in html
    assert "查看操作步骤" in html or "操作步骤" in html
    assert "You Are Here" not in html
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_pages.py::test_homepage_uses_cover_style_message_without_timeline_overview -v`
Expected: FAIL because the current home page still renders the old roadmap section.

- [ ] **Step 3: Write minimal implementation**

Replace `templates/index.html` body with a dedicated cover section using the approved structure:

```html
<section class="tocu-home-cover">
  <div class="tocu-home-cover__inner">
    <p class="tocu-home-cover__eyebrow">CUHK Master's Application Companion</p>
    <h1 class="tocu-home-cover__title">ToCU</h1>
    <p class="tocu-home-cover__slogan">把港中文硕士申请的时间、材料与步骤讲清楚</p>
    <p class="tocu-home-cover__summary">一个为港中文硕士申请者准备的信息服务平台。</p>
    <div class="tocu-home-cover__actions">
      <a href="{{ url_for('programs') }}" class="tocu-btn tocu-btn--primary">进入专业速查</a>
      <a href="{{ url_for('guide_list') }}" class="tocu-btn tocu-btn--secondary">查看操作步骤</a>
      <a href="{{ url_for('assistant') }}" class="tocu-btn tocu-btn--ghost">问智能助手</a>
    </div>
  </div>
</section>
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_pages.py::test_homepage_uses_cover_style_message_without_timeline_overview -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add templates/index.html static/css/app.css tests/test_pages.py
git commit -m "feat: redesign homepage as editorial cover"
```

### Task 4: Move process visualization to the Guides overview

**Files:**
- Modify: `/Users/wkai/Desktop/FlaskProject/templates/guide_list.html`
- Modify: `/Users/wkai/Desktop/FlaskProject/static/css/app.css`
- Test: `/Users/wkai/Desktop/FlaskProject/tests/test_pages.py`

- [ ] **Step 1: Extend the failing test for the six-stage overview**

```python
def test_guides_page_shows_six_stage_overview_and_resume_hint():
    client = app.test_client()
    response = client.get("/guide", headers={"Cookie": "last_stage=docs"})
    html = response.get_data(as_text=True)

    assert "申请前准备（2.1+2.2）" in html
    assert "网申阶段（2.3）" in html
    assert "申请材料寄送（2.4）" in html
    assert "申请积极信号（2.5）" in html
    assert "缴纳留位费（2.6）" in html
    assert "入学前准备（2.7）" in html
    assert "继续上次进度" in html or "上次看到" in html
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_pages.py::test_guides_page_shows_six_stage_overview_and_resume_hint -v`
Expected: FAIL because the current page does not show a resume panel.

- [ ] **Step 3: Write minimal implementation**

Restructure `guide_list.html` into:

```html
<section class="tocu-guides-overview">
  <header class="tocu-page-hero">
    ...
  </header>
  {% if request.cookies.get("last_stage") %}
    <aside class="tocu-resume-panel">...</aside>
  {% endif %}
  <div class="tocu-stage-overview-grid">
    {% for stage in stages %}
      <article class="tocu-stage-overview-card">...</article>
    {% endfor %}
  </div>
</section>
```

Use all six stages from `stages.json`.

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_pages.py::test_guides_page_shows_six_stage_overview_and_resume_hint -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add templates/guide_list.html static/css/app.css tests/test_pages.py
git commit -m "feat: redesign guides overview as six-stage entry"
```

### Task 5: Redesign Programs into a calmer directory

**Files:**
- Modify: `/Users/wkai/Desktop/FlaskProject/templates/programs.html`
- Modify: `/Users/wkai/Desktop/FlaskProject/static/css/app.css`
- Test: `/Users/wkai/Desktop/FlaskProject/tests/test_pages.py`

- [ ] **Step 1: Extend the failing test for the programs directory**

```python
def test_programs_page_keeps_lookup_behavior_with_directory_style_copy():
    client = app.test_client()
    html = client.get("/programs").get_data(as_text=True)

    assert "专业速查" in html
    assert "用于快速对比专业方向、语言要求和截止日期" in html
    assert "输入专业名、学院或方向关键词" in html
```

- [ ] **Step 2: Run test to verify it fails if copy or structure is missing**

Run: `pytest tests/test_pages.py::test_programs_page_keeps_lookup_behavior_with_directory_style_copy -v`
Expected: FAIL if the updated copy/markup has not been implemented.

- [ ] **Step 3: Write minimal implementation**

Keep the existing data loop, but update the surrounding page chrome and card markup to use calmer directory presentation classes such as:

```html
<section class="tocu-directory-page">
  <header class="tocu-page-hero">...</header>
  <div class="tocu-directory-toolbar">...</div>
  <div id="program-list" class="tocu-directory-grid">...</div>
</section>
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_pages.py::test_programs_page_keeps_lookup_behavior_with_directory_style_copy -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add templates/programs.html static/css/app.css tests/test_pages.py
git commit -m "feat: redesign programs directory"
```

### Task 6: Redesign Guide detail as a reading-first chapter page

**Files:**
- Modify: `/Users/wkai/Desktop/FlaskProject/templates/guide.html`
- Modify: `/Users/wkai/Desktop/FlaskProject/static/css/app.css`
- Test: `/Users/wkai/Desktop/FlaskProject/tests/test_pages.py`

- [ ] **Step 1: Extend the failing test for guide detail**

```python
def test_guide_detail_keeps_progress_controls_and_materials_sections():
    client = app.test_client()
    html = client.get("/guide/docs").get_data(as_text=True)

    assert "步骤导航" in html
    assert "如何推进本步骤" in html
    assert "材料清单" in html
    assert "标记为已完成" in html or "已完成" in html
```

- [ ] **Step 2: Run test to verify it fails only if expectations are not met**

Run: `pytest tests/test_pages.py::test_guide_detail_keeps_progress_controls_and_materials_sections -v`
Expected: PASS on content presence today or fail after markup changes if a required section is lost; use this test as a guardrail while redesigning.

- [ ] **Step 3: Write minimal implementation**

Keep the existing data-driven sections but move to a calmer layout hierarchy, for example:

```html
<section class="tocu-guide-detail-shell">
  <aside class="tocu-guide-detail-nav">...</aside>
  <article class="tocu-guide-detail-main">...</article>
  <aside class="tocu-guide-detail-notes">...</aside>
</section>
```

Refine type scale and spacing so the center column reads as the main document.

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_pages.py::test_guide_detail_keeps_progress_controls_and_materials_sections -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add templates/guide.html static/css/app.css tests/test_pages.py
git commit -m "feat: redesign guide detail layout"
```

### Task 7: Align Assistant, FAQ, and auth surfaces with the shared system

**Files:**
- Modify: `/Users/wkai/Desktop/FlaskProject/templates/assistant.html`
- Modify: `/Users/wkai/Desktop/FlaskProject/templates/faq.html`
- Modify: `/Users/wkai/Desktop/FlaskProject/templates/login.html`
- Modify: `/Users/wkai/Desktop/FlaskProject/templates/login_modal.html`
- Modify: `/Users/wkai/Desktop/FlaskProject/static/css/app.css`
- Test: `/Users/wkai/Desktop/FlaskProject/tests/test_pages.py`

- [ ] **Step 1: Extend the failing test for assistant and auth surfaces**

```python
def test_assistant_and_login_pages_still_render_primary_labels():
    client = app.test_client()
    assistant_html = client.get("/assistant").get_data(as_text=True)
    login_html = client.get("/login").get_data(as_text=True)

    assert "智能助手" in assistant_html
    assert "快速提问" in assistant_html
    assert "登录 / 注册" in login_html
```

- [ ] **Step 2: Run test to verify it fails if redesign drops required UI**

Run: `pytest tests/test_pages.py::test_assistant_and_login_pages_still_render_primary_labels -v`
Expected: PASS today or FAIL after partial redesign if key labels are lost; use this as a guardrail while aligning styles.

- [ ] **Step 3: Write minimal implementation**

Keep assistant, FAQ, login, and login modal on the same warm/light system. Update wrappers to use the shared hero and surface classes, for example:

```html
<section class="tocu-page-stack">
  <header class="tocu-page-hero">...</header>
  <div class="tocu-surface-panel">...</div>
</section>
```

Do not introduce a dark assistant theme.

- [ ] **Step 4: Run full page smoke tests to verify everything passes**

Run: `pytest tests/test_pages.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add templates/assistant.html templates/faq.html templates/login.html templates/login_modal.html static/css/app.css tests/test_pages.py
git commit -m "feat: align supporting pages with redesign"
```

### Task 8: Final verification and cleanup

**Files:**
- Modify: `/Users/wkai/Desktop/FlaskProject/static/css/app.css`
- Test: `/Users/wkai/Desktop/FlaskProject/tests/test_pages.py`

- [ ] **Step 1: Run the full test suite**

Run: `pytest -v`
Expected: PASS

- [ ] **Step 2: Run a lightweight template sanity check**

Run: `python3 -m compileall app.py utils`
Expected: PASS with no syntax errors

- [ ] **Step 3: Inspect git diff for accidental regressions**

Run: `git diff --stat`
Expected: only the intended template, CSS, test, and plan changes

- [ ] **Step 4: Make any minimal cleanup edits needed to keep everything green**

If `pytest` or `compileall` surfaces issues, fix only the failing templates/styles/scripts required to restore green status.

- [ ] **Step 5: Commit**

```bash
git add templates static/css/app.css tests/test_pages.py
git commit -m "chore: finalize ToCU redesign"
```

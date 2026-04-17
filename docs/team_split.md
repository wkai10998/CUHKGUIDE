# 团队分工与交付清单（5 位同学）

## 目标
围绕当前线上版本完成课堂汇报，核心页面为：
1. 首页
2. 专业速查
3. 操作步骤
4. 智能助手
5. 登录/注册/评论与后端同步

## 统一口径（先对齐）
- 当前版本主导航是 4 个页面：首页、专业速查、操作步骤、智能助手。
- FAQ 路由已移除，统一由免责声明页承接风险提示。
- BeautifulSoup 抓取是已完成的离线流程，不是实时同步。
- 抓取数据先清洗，再写入 `content/programs.json` 和 `content/rag_kb.txt`（或其生成源），供前端展示与 RAG 使用。

## 分工建议（按汇报模块）

### 土土：首页前端设计与响应式
- 负责内容：首页视觉结构、色彩字体体系、移动端适配。
- 讲解重点：导航布局、组件复用、断点策略、首页信息入口设计。
- 对应文件：
  - `templates/index.html`
  - `templates/header.html`
  - `templates/base.html`
  - `static/css/app.css`

### 塔塔：专业速查 + BeautifulSoup 数据抓取与清洗
- 负责内容：专业速查数据来源、抓取字段、清洗规则、入库/落盘流程。
- 讲解重点：
  - BeautifulSoup 一次性抓取（非实时）
  - 清洗与字段标准化
  - 如何落到 `programs.json` 并补充 RAG 知识
  - 前端搜索与按学院筛选逻辑
- 对应文件：
  - `content/programs.json`
  - `content/rag_kb.txt`
  - `templates/programs.html`
  - `static/js/programs.js`
  - `utils/content_loader.py`
  - 抓取脚本（塔塔本地/分支中的 BeautifulSoup 脚本）

### 冯少：网站信息结构、路由、Jinja2 模板
- 负责内容：网站信息架构、`app.py` 路由、模板继承、页面流转。
- 讲解重点：
  - 路由与模板映射关系
  - `extends/include/block` 的模板复用
  - “继续上次进度”与 cookie/session 交互
  - 与 Supabase 交互的后端入口位置
- 对应文件：
  - `app.py`
  - `templates/base.html`
  - `templates/guide_list.html`
  - `templates/guide.html`
  - `utils/supabase_client.py`

### Kai：AI 智能助手与 RAG
- 负责内容：聊天界面、问答 API、RAG 检索与回退机制。
- 讲解重点：
  - 前端聊天交互
  - `/assistant/message` 请求链路
  - 知识切片、向量入库、相似度检索
  - 回答来源与可验证性
- 对应文件：
  - `templates/assistant.html`
  - `static/js/assistant_chat.js`
  - `utils/knowledge_base.py`
  - `utils/rag_pipeline.py`
  - `utils/zhipu_client.py`
  - `scripts/ingest_rag.py`
  - `docs/supabase_rag.sql`

### 洗神：注册登录、评论、Supabase 后端与错误处理
- 负责内容：登录注册流程、session 机制、评论入库、错误处理策略。
- 讲解重点：
  - 登录注册校验与 session 写入
  - 评论与用户绑定（`user_id`）
  - Supabase 建表与后端调用
  - 页面与接口异常处理（含 404/500）
- 对应文件：
  - `app.py`
  - `templates/login_modal.html`
  - `static/js/components/login_modal.js`
  - `static/js/guide.js`
  - `utils/supabase_client.py`
  - `docs/supabase_comments.sql`
  - `templates/errors/404.html`
  - `templates/errors/500.html`

## 验收标准
1. 每位同学能用 3 到 5 分钟讲清自己模块的用户价值和技术路径。
2. 每位同学都能指出自己模块的核心代码文件（至少 3 个）。
3. 全组口径一致：BeautifulSoup 是离线抓取，不是实时同步。
4. 全组口径一致：FAQ 不在当前主流程页面中。

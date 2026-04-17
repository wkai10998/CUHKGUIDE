# 项目目录说明与优化建议（当前版本）

## 1. 项目定位
本项目是基于 Flask 的课程项目，主题是“港中文申请一站式助手”。

当前主功能：
- 首页功能入口
- 专业速查（搜索 + 学院筛选）
- 操作步骤（阶段、步骤、评论、完成状态）
- 智能助手（RAG 检索 + 回答 + 来源）
- 登录/注册/资料修改

补充口径：
- FAQ 路由已移除，不属于当前主流程页面。
- BeautifulSoup 数据抓取为离线一次性流程，不是运行时实时同步。

## 2. 当前目录总览

```text
FlaskProject/
├── app.py
├── content/
├── docs/
├── scripts/
├── static/
├── templates/
├── tests/
├── utils/
├── README.md
├── requirements.txt
├── .env.example
└── .gitignore
```

## 3. 目录逐个说明

### 3.1 `app.py`
主入口，集中管理：
- 页面路由与交互路由
- 登录/注册/退出
- session 与 cookie
- 评论发布与读取 API
- 助手消息 API
- 404/500 错误页

### 3.2 `content/`
页面和知识库使用的结构化数据：
- `stages.json`：阶段导航
- `guide_steps.json`：步骤内容
- `programs.json`：专业速查数据
- `rag_kb.txt`：RAG 补充文本

说明：`programs.json` 与 `rag_kb.txt` 可以由离线抓取清洗流程更新。

### 3.3 `templates/`
Jinja2 模板：
- 骨架：`base.html`
- 公共组件：`header.html`、`footer.html`、`login_modal.html`
- 页面：`index.html`、`programs.html`、`guide_list.html`、`guide.html`、`assistant.html`、`disclaimer.html`
- 错误页：`errors/404.html`、`errors/500.html`

### 3.4 `static/`
- `static/css/app.css`：视觉系统与布局样式
- `static/js/programs.js`：专业搜索/筛选
- `static/js/guide.js`：步骤完成状态 + 评论加载
- `static/js/assistant_chat.js`：聊天交互
- `static/js/components/login_modal.js`：登录注册弹窗

### 3.5 `utils/`
后端工具层：
- `content_loader.py`：读取 JSON 数据
- `knowledge_base.py`：构造知识片段
- `rag_pipeline.py`：切片、入库、检索、生成
- `supabase_client.py`：users/comments/rag_chunks 的 Supabase 访问
- `zhipu_client.py`：模型 embedding 与回答接口

### 3.6 `scripts/`
- `ingest_rag.py`：知识切片向量化并写入 Supabase

说明：该脚本是预处理工具，不在用户页面请求时执行。

### 3.7 `docs/`
- 汇报讲解文档
- 团队分工文档
- Supabase 建表 SQL（`supabase_comments.sql`、`supabase_rag.sql`）

### 3.8 `tests/`
覆盖方向：
- 主页面与路由可用性
- 登录/注册/session 行为
- 评论与权限行为
- 助手 API 与回退机制
- 结构稳定性（如 FAQ 路由移除）

## 4. 当前结构优点
- 单入口清晰，课堂讲解友好。
- 数据、模板、静态资源分层明确。
- 测试覆盖核心用户路径。
- 与 Supabase/RAG 的演示链路完整。

## 5. 当前结构风险点
- `app.py` 职责较多，后续扩展时会增长过快。
- `utils/` 聚合了多种职责，长期可考虑再分层。
- 文档更新频率要与代码同步，避免“历史描述”误导汇报。

## 6. 关于 BeautifulSoup 抓取的准确描述
当前正确表述应为：
1. 抓取脚本用于离线抓取官网数据。
2. 抓取结果需要清洗、标准化后再写入本项目数据。
3. 页面和 RAG 使用的是清洗后的本地数据结果。
4. 不提供实时自动同步能力。

## 7. 后续优化建议（汇报后再做）
- 路由按模块拆分（`routes/auth.py`、`routes/assistant.py` 等）。
- `utils/` 细分为 `clients/`、`services/`、`data/`。
- 建立 `content/raw -> clean -> curated` 数据链路目录。
- 文档按 `presentation/`、`database/`、`team/` 分类。

## 8. 一句话结论
当前目录结构适合课程项目展示；现阶段重点是统一讲解口径与分工，不是大规模重构。

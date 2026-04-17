# 5 人小组 PPT 汇报与代码理解指南（当前版本）

## 1. 使用范围
这份文档基于当前代码版本编写，用于统一课堂汇报口径与分工。

当前主流程页面：
- 首页 `/`
- 专业速查 `/programs`
- 操作步骤 `/guide`
- 智能助手 `/assistant`

补充说明：
- FAQ 路由已移除（测试中有覆盖），不要按 FAQ 页面讲主流程。
- 免责声明页为 `/disclaimer`。

## 2. 汇报必须统一的三句话
1. 我们项目是 Flask + Jinja2 + JS + Supabase + RAG 的教学型网站。
2. BeautifulSoup 抓取是离线一次性流程，抓完清洗后再写入本项目数据文件。
3. 当前版本不做“官网更新后自动实时同步到页面”。

## 3. 推荐 PPT 结构（10-12 页）

### 第 1 页：项目背景
- 信息分散、步骤复杂、容易漏材料和时间点。
- 目标是做一个一站式申请辅助网站。

### 第 2 页：功能总览
- 首页、专业速查、操作步骤、智能助手、登录评论。
- 可放 4-5 张页面截图。

### 第 3 页：技术栈
- Flask、Jinja2、Tailwind/CSS、JavaScript、Session、Supabase、RAG。

### 第 4 页：项目结构
- `app.py`、`templates/`、`static/`、`content/`、`utils/`、`scripts/`、`docs/`、`tests/`。

### 第 5 页：用户流程
```text
首页 -> 专业速查/操作步骤 -> 登录注册 -> 评论与进度 -> 智能助手提问
```

### 第 6 页：前端与响应式
- 导航复用、组件复用、移动端适配、视觉规范。

### 第 7 页：后端交互
- GET/POST、登录注册、session、评论写入与读取。

### 第 8 页：数据抓取与清洗
- BeautifulSoup 抓取字段、清洗规则、写入 JSON/RAG 的流程。
- 强调离线流程，不是实时同步。

### 第 9 页：AI 助手与 RAG
- 用户提问 -> 检索 -> 生成 -> 来源展示。
- 检索失败时本地回退机制。

### 第 10 页：小组分工
- 每人模块、代码文件、讲解边界。

### 第 11 页：测试与稳定性
- 页面可用性、登录流程、评论权限、助手 API、错误页。

### 第 12 页：总结与后续计划
- 收获、可维护性、下一步优化。

## 4. 5 人分工（按你们最新安排）

### 4.1 土土：首页功能（前端设计）
负责讲：
- 首页视觉结构、配色和字体选择
- 响应式布局与移动端导航

建议重点文件：
- [templates/index.html](/Users/wkai/Desktop/FlaskProject/templates/index.html)
- [templates/header.html](/Users/wkai/Desktop/FlaskProject/templates/header.html)
- [templates/base.html](/Users/wkai/Desktop/FlaskProject/templates/base.html)
- [static/css/app.css](/Users/wkai/Desktop/FlaskProject/static/css/app.css)

### 4.2 塔塔：专业速查 + BeautifulSoup 抓取清洗
负责讲：
- 抓取来源、字段提取、清洗规则
- 数据如何进入 `programs.json` 与 RAG 补充知识
- 前端搜索和学院筛选

必须统一口径：
- 抓取代码已完成
- 作用是离线批量更新数据
- 不是网站运行时实时同步

建议重点文件：
- [content/programs.json](/Users/wkai/Desktop/FlaskProject/content/programs.json)
- [content/rag_kb.txt](/Users/wkai/Desktop/FlaskProject/content/rag_kb.txt)
- [templates/programs.html](/Users/wkai/Desktop/FlaskProject/templates/programs.html)
- [static/js/programs.js](/Users/wkai/Desktop/FlaskProject/static/js/programs.js)
- [utils/content_loader.py](/Users/wkai/Desktop/FlaskProject/utils/content_loader.py)
- 塔塔本地/分支中的 BeautifulSoup 抓取脚本

### 4.3 冯少：网站信息结构、路由与模板
负责讲：
- `app.py` 路由总览与页面跳转
- Jinja2 模板继承与组件复用
- “继续上次进度”与 cookie/session 的协作

建议重点文件：
- [app.py](/Users/wkai/Desktop/FlaskProject/app.py)
- [templates/base.html](/Users/wkai/Desktop/FlaskProject/templates/base.html)
- [templates/guide_list.html](/Users/wkai/Desktop/FlaskProject/templates/guide_list.html)
- [templates/guide.html](/Users/wkai/Desktop/FlaskProject/templates/guide.html)

### 4.4 Kai：AI 助手与 RAG
负责讲：
- 聊天界面与消息 API
- 检索增强、来源追溯、回退机制
- 向量库初始化与入库脚本

建议重点文件：
- [templates/assistant.html](/Users/wkai/Desktop/FlaskProject/templates/assistant.html)
- [static/js/assistant_chat.js](/Users/wkai/Desktop/FlaskProject/static/js/assistant_chat.js)
- [utils/knowledge_base.py](/Users/wkai/Desktop/FlaskProject/utils/knowledge_base.py)
- [utils/rag_pipeline.py](/Users/wkai/Desktop/FlaskProject/utils/rag_pipeline.py)
- [utils/zhipu_client.py](/Users/wkai/Desktop/FlaskProject/utils/zhipu_client.py)
- [scripts/ingest_rag.py](/Users/wkai/Desktop/FlaskProject/scripts/ingest_rag.py)
- [docs/supabase_rag.sql](/Users/wkai/Desktop/FlaskProject/docs/supabase_rag.sql)

### 4.5 洗神：注册登录、评论、Supabase、错误处理
负责讲：
- 登录注册规则、session 机制、资料更新
- 评论写入/读取与用户绑定
- users/comments 建表和后端调用
- 错误处理（前端提示 + 404/500）

建议重点文件：
- [app.py](/Users/wkai/Desktop/FlaskProject/app.py)
- [templates/login_modal.html](/Users/wkai/Desktop/FlaskProject/templates/login_modal.html)
- [static/js/components/login_modal.js](/Users/wkai/Desktop/FlaskProject/static/js/components/login_modal.js)
- [static/js/guide.js](/Users/wkai/Desktop/FlaskProject/static/js/guide.js)
- [utils/supabase_client.py](/Users/wkai/Desktop/FlaskProject/utils/supabase_client.py)
- [docs/supabase_comments.sql](/Users/wkai/Desktop/FlaskProject/docs/supabase_comments.sql)
- [templates/errors/404.html](/Users/wkai/Desktop/FlaskProject/templates/errors/404.html)
- [templates/errors/500.html](/Users/wkai/Desktop/FlaskProject/templates/errors/500.html)

## 5. 你们应该怎么读代码（从外到内）

### 第一步：跑起来
- 启动项目，逐个访问 4 个主页面 + 登录弹窗。

### 第二步：看路由
- 重点看 `app.py` 的页面路由和交互路由。

### 第三步：看模板和 JS
- 看 `templates/` 和 `static/js/` 如何配合页面交互。

### 第四步：看数据
- 看 `content/*.json` 与 `content/rag_kb.txt` 的字段和用途。

### 第五步：看 Supabase + RAG
- 看 `utils/supabase_client.py`、`utils/rag_pipeline.py`、`scripts/ingest_rag.py`。

## 6. 常见问答（答辩版）

### Q1：为什么不用更复杂的框架？
因为这是课程项目，目标是把 Flask 路由、模板渲染、前后端交互、数据库和 RAG 的核心链路讲清楚。

### Q2：BeautifulSoup 是实时抓取吗？
不是。它是离线一次性抓取与清洗流程，清洗后写入项目数据文件，供页面和 RAG 使用。

### Q3：BeautifulSoup 代码在哪里？
由塔塔维护在其本地/分支，课堂展示会说明抓取字段、清洗规则和落地结果，不依赖线上实时运行。

### Q4：AI 助手是否绝对可靠？
不是。我们通过检索增强和来源展示提高可验证性；当向量检索不可用时会回退到本地检索。

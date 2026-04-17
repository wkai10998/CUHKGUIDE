# 15 页 PPT 完整内容与讲稿（当前版本）

## 使用说明
本稿按当前代码状态编写，避免历史版本信息干扰。

统一口径：
- 当前主导航页面：首页、专业速查、操作步骤、智能助手。
- FAQ 路由已移除，不作为主流程讲解。
- BeautifulSoup 抓取为离线一次性流程，不是实时同步。

---

## 第 1 页：封面
- 标题：港中文申请一站式助手
- 副标题：Flask 课程项目
- 展示：首页截图 + 小组成员

讲稿：
我们项目目标是把申请流程、专业信息、步骤指引和智能问答放到一个统一入口，减少信息分散带来的决策成本。

## 第 2 页：项目背景与痛点
- 信息分散
- 节点复杂
- 容易漏材料

讲稿：
用户常在多个渠道来回找资料，我们把高频问题拆成清晰页面和可执行步骤。

## 第 3 页：功能总览
- 首页
- 专业速查
- 操作步骤
- 智能助手
- 登录/评论

讲稿：
页面围绕“查信息、做动作、问问题”三条主线设计。

## 第 4 页：技术栈
- Flask / Jinja2
- Tailwind + CSS
- JavaScript
- Session
- Supabase
- RAG（智谱 + pgvector）

讲稿：
项目重点不是堆技术，而是让每个技术点都对应到可演示的用户功能。

## 第 5 页：目录结构
- `app.py`
- `templates/`
- `static/`
- `content/`
- `utils/`
- `scripts/`
- `tests/`

讲稿：
这是教学友好的单体结构，入口清晰，适合多人分工和课堂讲解。

## 第 6 页：用户访问流程
```text
首页 -> 专业速查/操作步骤 -> 登录 -> 评论与进度 -> 智能助手
```

讲稿：
流程从“信息浏览”到“交互沉淀”再到“问答辅助”，形成闭环。

## 第 7 页：首页与视觉系统（土土）
- 信息入口布局
- 字体、色彩、组件风格
- 移动端适配

对应代码：
- `templates/index.html`
- `templates/header.html`
- `static/css/app.css`

讲稿：
首页强调快速分流，保证用户 1-2 次点击进入目标任务页面。

## 第 8 页：专业速查与筛选（土土/塔塔）
- 关键词搜索
- 按学院筛选
- 项目卡片结构

对应代码：
- `templates/programs.html`
- `static/js/programs.js`
- `content/programs.json`

讲稿：
前端筛选逻辑在浏览器本地完成，响应快，交互成本低。

## 第 9 页：BeautifulSoup 抓取与清洗（塔塔）
- 抓取官网页面字段
- 数据清洗与标准化
- 写入 `programs.json` 与 RAG 补充数据

必须强调：
- 已完成离线抓取流程
- 不是实时自动同步

讲稿：
抓取流程用于批量更新数据底座，页面展示依赖的是清洗后的结构化结果。

## 第 10 页：路由与模板结构（冯少）
- 路由映射
- `extends/include/block`
- 页面间跳转与 `redirect`

对应代码：
- `app.py`
- `templates/base.html`
- `templates/guide_list.html`
- `templates/guide.html`

讲稿：
我们把路由、模板、数据注入的关系讲清楚，老师很容易判断项目是否真正可维护。

## 第 11 页：登录注册、评论与 Session（洗神）
- 登录/注册流程
- session 存储用户状态
- 评论绑定 `user_id`

对应代码：
- `templates/login_modal.html`
- `static/js/components/login_modal.js`
- `static/js/guide.js`
- `app.py`
- `utils/supabase_client.py`

讲稿：
页面权限由 session 控制，评论和用户关系由 Supabase 数据表保证。

## 第 12 页：Supabase 建表与后端同步（洗神/Kai）
- `users` 表
- `comments` 表
- `rag_chunks` 表 + RPC

对应 SQL：
- `docs/supabase_comments.sql`
- `docs/supabase_rag.sql`

讲稿：
数据库层把账号、评论、向量检索三条链路分开，便于扩展和排错。

## 第 13 页：AI 助手与 RAG（Kai）
- 聊天前端
- `/assistant/message` API
- 检索增强 + 来源返回
- 失败回退到本地检索

对应代码：
- `templates/assistant.html`
- `static/js/assistant_chat.js`
- `utils/knowledge_base.py`
- `utils/rag_pipeline.py`

讲稿：
我们强调“可验证回答”，所以在返回内容里保留来源信息。

## 第 14 页：测试与稳定性
- 页面可用测试
- 登录与 session 测试
- 助手 API 测试
- 结构变更测试（如 FAQ 路由移除）

对应代码：
- `tests/test_course_structure.py`
- `tests/test_pages.py`
- `tests/test_auth_session.py`
- `tests/test_assistant_chat_api.py`

讲稿：
测试让我们能在重构样式和页面结构后快速确认主流程没有回归。

## 第 15 页：分工总结与项目收获
- 土土：首页设计与响应式
- 塔塔：抓取清洗 + 专业速查数据
- 冯少：结构、路由、模板
- Kai：AI 助手与 RAG
- 洗神：登录评论与 Supabase 后端

讲稿：
我们这次最大的收获是把前端、后端、数据和 AI 链路串成了一个可以演示、可以验证、可以分工协作的完整项目。

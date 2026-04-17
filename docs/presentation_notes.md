# 展示讲解要点（简版）

## 一、项目主线
- 首页：功能入口与信息架构
- 专业速查：专业信息检索与按学院筛选
- 操作步骤：阶段与步骤、评论区、完成状态
- 智能助手：RAG 问答（检索 + 回答 + 来源）
- 登录/注册：session 登录态、资料修改、评论权限控制

## 二、技术点覆盖
- Flask 路由（`GET` 页面渲染、`POST` 交互提交）
- Jinja2（`extends/include/block` 模板结构）
- Tailwind + 自定义 CSS（响应式布局与视觉系统）
- JavaScript 交互（搜索筛选、步骤状态切换、聊天交互）
- Session + Cookie（登录态与“继续上次进度”）
- JSON 内容管理（`content/*.json`）
- Supabase（`users`、`comments`、`rag_chunks`）
- 错误处理（接口异常提示 + 404/500 页面）

## 三、数据口径（答辩统一）
- BeautifulSoup 抓取流程已完成，但属于离线一次性抓取。
- 抓取后会做清洗，再写入本项目 JSON / RAG 知识源。
- 当前项目不做“官网更新 -> 页面自动实时同步”。

## 四、目录亮点
- `app.py`：集中管理路由、认证、评论、助手 API
- `templates/`：`base + header/footer + 页面模板` 的复用结构
- `static/js/`：`programs/guide/assistant/login_modal` 按功能拆分
- `utils/`：内容加载、Supabase 客户端、RAG 流程、模型调用

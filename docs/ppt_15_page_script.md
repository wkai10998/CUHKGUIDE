# 15 页 PPT 完整内容与讲稿

## 使用说明

这份文档是给你们小组直接做 PPT 用的。

每一页我都拆成了 5 个部分：
- 页码与标题
- 这一页 PPT 上建议展示什么
- 页面上建议写哪些文字
- 对应项目文件
- 台上讲稿

建议使用方式：
- PPT 上不要把讲稿全文贴进去
- PPT 只保留关键词、流程图、截图、结构图
- 台上讲话时参考“讲稿”部分

## 整体讲述节奏

建议控制在 10 到 15 分钟。

推荐节奏：
- 前 3 页：项目背景与整体目标
- 中间 9 页：功能、前端、后端、数据、AI
- 后 3 页：分工、学习路径、优化方向

## 推荐主讲分配

- 第 1 位同学：第 1、2、9、14 页
- 第 2 位同学：第 4、5、10 页
- 第 3 位同学：第 8 页
- 第 4 位同学：第 6、7 页
- 第 5 位同学：第 11、12 页
- 第 13、15 页可由第 1 位同学收尾，或者由组长总结

---

## 第 1 页：封面页

### 建议标题
Flask 课程项目：港中文申请一站式助手

### PPT 上展示什么
- 项目名称
- 小组成员姓名
- 课程名称
- 汇报日期
- 一张项目首页截图或者时间线截图做背景

### 页面上建议写的文字
- Flask 课程项目
- 港中文申请一站式助手
- 小组成员：A / B / C / D / E
- 关键词：Flask / Jinja2 / Tailwind / Supabase / RAG

### 对应项目文件
- [README.md](/Users/wkai/Desktop/FlaskProject/README.md)
- [templates/index.html](/Users/wkai/Desktop/FlaskProject/templates/index.html)

### 台上讲稿
大家好，我们小组本次展示的课程项目叫做“港中文申请一站式助手”。这个项目围绕研究生申请流程，整合了申请时间线、专业速查、申请指南、FAQ、用户登录评论，以及 AI 助手等功能。我们希望通过这个项目，把分散的信息整理成一个更清晰、更好用的网站，同时也把 Flask、前后端交互、结构化数据和 AI 检索这些课程知识点串起来。

---

## 第 2 页：项目背景与痛点

### 建议标题
项目背景：为什么要做这个网站

### PPT 上展示什么
- 左边放“原有问题”
- 右边放“我们的解决思路”
- 可以用 2 列对照表

### 页面上建议写的文字
- 申请信息分散：官网、FAQ、材料说明、经验贴分布在不同地方
- 申请流程复杂：时间线长、步骤多、容易遗漏材料
- 用户需求明确：想快速知道“什么时候做什么、去哪里看、材料要准备什么”
- 我们的目标：做一个统一入口，帮助用户快速定位信息

### 对应项目文件
- [docs/presentation_guide.md](/Users/wkai/Desktop/FlaskProject/docs/presentation_guide.md)
- [docs/project_structure.md](/Users/wkai/Desktop/FlaskProject/docs/project_structure.md)

### 台上讲稿
我们做这个项目的出发点，是发现研究生申请的信息非常分散。用户往往需要在官网、FAQ、材料说明、论坛经验之间来回查找，而且每个阶段的任务也很多，容易漏掉材料或者错过时间节点。所以我们的目标不是简单做一个展示页面，而是做一个更完整的申请辅助网站，让用户能够在一个入口里查看时间线、搜索专业、按步骤准备材料，并且在有疑问的时候还能通过 AI 助手快速定位信息。

---

## 第 3 页：项目目标与功能总览

### 建议标题
项目目标与核心功能

### PPT 上展示什么
- 5 个核心页面截图拼图
- 中间放一条主流程箭头

### 页面上建议写的文字
- 首页：申请时间路线图
- 专业速查：项目信息筛选
- 申请指南：阶段 -> 步骤 -> 材料 -> 评论
- FAQ：问题搜索与详情查看
- 智能助手：RAG 检索 + 回答 + 来源

### 对应项目文件
- [app.py](/Users/wkai/Desktop/FlaskProject/app.py)
- [templates/programs.html](/Users/wkai/Desktop/FlaskProject/templates/programs.html)
- [templates/guide.html](/Users/wkai/Desktop/FlaskProject/templates/guide.html)
- [templates/faq.html](/Users/wkai/Desktop/FlaskProject/templates/faq.html)
- [templates/assistant.html](/Users/wkai/Desktop/FlaskProject/templates/assistant.html)

### 台上讲稿
我们把整个项目拆成了 5 个核心页面。首页负责让用户快速建立整体时间观念；专业速查页帮助用户从专业角度筛选信息；申请指南页是整个项目最核心的内容页，按阶段和步骤组织具体材料和操作建议；FAQ 页主要用来快速查常见问题；最后是智能助手页面，它会结合项目内部知识库给出检索增强后的回答。这样一来，用户既可以按页面浏览，也可以带着问题直接查找。

---

## 第 4 页：技术栈与知识点覆盖

### 建议标题
技术栈与课程知识点对应

### PPT 上展示什么
- 表格形式最合适
- 左列写技术
- 右列写在项目中承担的作用

### 页面上建议写的文字
- Flask：路由与后端入口
- Jinja2：模板渲染
- Tailwind CSS：快速布局与响应式设计
- JavaScript：搜索、局部刷新、弹窗交互
- Session / Cookie：登录状态与用户体验
- Supabase：用户、评论、RAG 向量数据
- 智谱 API：embedding 与回答生成

### 对应项目文件
- [README.md](/Users/wkai/Desktop/FlaskProject/README.md)
- [templates/base.html](/Users/wkai/Desktop/FlaskProject/templates/base.html)
- [static/js/guide.js](/Users/wkai/Desktop/FlaskProject/static/js/guide.js)
- [utils/supabase_client.py](/Users/wkai/Desktop/FlaskProject/utils/supabase_client.py)
- [utils/zhipu_client.py](/Users/wkai/Desktop/FlaskProject/utils/zhipu_client.py)

### 台上讲稿
从技术栈来看，这个项目其实把课程中的多个知识点连接在了一起。Flask 负责网站后端和路由分发，Jinja2 负责把 Python 数据渲染成 HTML 页面，Tailwind CSS 负责页面布局和响应式适配，JavaScript 负责前端交互，比如搜索、评论加载和状态切换。用户登录和页面状态管理使用了 Session 和 Cookie，而用户评论和 RAG 向量数据则放在 Supabase 中。AI 助手调用的是智谱接口，用于生成 embedding 和最终回答。

---

## 第 5 页：项目目录结构

### 建议标题
项目目录结构与职责划分

### PPT 上展示什么
- 一棵简化目录树
- 每个目录右边写一句职责

### 页面上建议写的文字
```text
app.py         -> 项目主入口
content/       -> 结构化内容数据
templates/     -> Jinja2 页面模板
static/        -> CSS / JS / 图片
utils/         -> 数据库、RAG、工具函数
scripts/       -> 辅助脚本
tests/         -> 自动化测试
docs/          -> 文档与 SQL
```

### 对应项目文件
- [docs/project_structure.md](/Users/wkai/Desktop/FlaskProject/docs/project_structure.md)
- [README.md](/Users/wkai/Desktop/FlaskProject/README.md)

### 台上讲稿
这个项目目前采用的是比较适合教学和零基础协作的目录结构。`app.py` 是总入口，`content` 保存页面直接用的 JSON 数据，`templates` 负责 HTML 模板，`static` 负责样式、脚本和图片，`utils` 放后端工具模块，`scripts` 放辅助脚本，`tests` 用来做验证。这样分层的好处是，大家不需要一下子读懂所有代码，而是可以先根据自己负责的模块去找对应目录。

---

## 第 6 页：内容数据是怎么组织的

### 建议标题
内容层设计：JSON 如何组织申请信息

### PPT 上展示什么
- 4 个 JSON 文件名
- 每个文件展示 2 到 3 个关键字段
- 可以放字段结构示意图

### 页面上建议写的文字
- `stages.json`：阶段导航
- `guide_steps.json`：步骤标题、教程、提示、材料
- `programs.json`：专业名、学院、截止时间、语言要求
- `faq.json`：分类、问题、答案

### 对应项目文件
- [content/stages.json](/Users/wkai/Desktop/FlaskProject/content/stages.json)
- [content/guide_steps.json](/Users/wkai/Desktop/FlaskProject/content/guide_steps.json)
- [content/programs.json](/Users/wkai/Desktop/FlaskProject/content/programs.json)
- [content/faq.json](/Users/wkai/Desktop/FlaskProject/content/faq.json)
- [utils/content_loader.py](/Users/wkai/Desktop/FlaskProject/utils/content_loader.py)

### 台上讲稿
在这个项目中，我们没有把所有内容都直接写死在 HTML 里，而是把核心内容做成结构化 JSON。比如阶段导航放在 `stages.json`，申请步骤详情放在 `guide_steps.json`，专业速查放在 `programs.json`，FAQ 则放在 `faq.json`。这样做有两个好处：第一，内容和页面展示逻辑分开；第二，零基础同学也可以通过维护 JSON 参与项目，因为他们不需要一开始就修改 Python 或模板代码。

---

## 第 7 页：申请指南页面如何由数据渲染出来

### 建议标题
内容展示流程：从 JSON 到页面

### PPT 上展示什么
- 一条流程图
- `content -> Flask -> Jinja2 -> HTML 页面`
- 旁边配一张申请指南页截图

### 页面上建议写的文字
- Step 1：读取 `guide_steps.json`
- Step 2：根据 URL 找到阶段和步骤
- Step 3：Flask 把数据传给模板
- Step 4：Jinja2 循环渲染标题、教程、材料、评论区

### 对应项目文件
- [app.py](/Users/wkai/Desktop/FlaskProject/app.py)
- [templates/guide.html](/Users/wkai/Desktop/FlaskProject/templates/guide.html)
- [utils/content_loader.py](/Users/wkai/Desktop/FlaskProject/utils/content_loader.py)

### 台上讲稿
这一页想说明的是，我们的页面不是手工写死的，而是数据驱动的。以申请指南页为例，当用户访问某个阶段页面时，Flask 会先读取 `guide_steps.json`，再根据 URL 中的阶段参数找到对应内容，然后把当前步骤的数据交给 Jinja2 模板。模板再通过循环和变量，把步骤标题、教程、提示、材料清单和评论区渲染出来。这样后续如果我们要补充内容，只要更新 JSON 文件，页面就能自动展示。

---

## 第 8 页：数据抓取与清洗的扩展方案

### 建议标题
数据抓取：当前现状与后续扩展

### PPT 上展示什么
- 左边写“当前已完成”
- 右边写“后续计划”
- 中间画一个抓取流程

### 页面上建议写的文字
- 当前已完成：
  - 使用结构化 JSON 管理内容
  - 页面展示与 AI 助手可复用同一批数据
- 后续计划：
  - BeautifulSoup 抓取官网页面
  - 解析 HTML 提取字段
  - 清洗成 JSON / CSV
  - 写入页面和 AI 知识库

### 对应项目文件
- [content/programs.json](/Users/wkai/Desktop/FlaskProject/content/programs.json)
- [content/faq.json](/Users/wkai/Desktop/FlaskProject/content/faq.json)
- [docs/project_structure.md](/Users/wkai/Desktop/FlaskProject/docs/project_structure.md)

### 台上讲稿
这一部分我们要说明真实情况。当前仓库中已经落地的是结构化 JSON 数据，也就是说页面和 AI 助手已经能使用统一的数据格式。但自动抓取官网内容这一块，目前还是我们的扩展方向，还没有正式写成脚本。后续我们计划使用 BeautifulSoup 抓取官网页面，再把原始 HTML 中的信息解析成字段，比如专业名称、截止日期、语言要求等，最后清洗成 JSON 或 CSV。这样数据层就会更完整，也更适合长期维护。

---

## 第 9 页：系统整体工作流

### 建议标题
系统工作流：一次页面访问是怎么完成的

### PPT 上展示什么
- 一张从浏览器到数据库再回到页面的流程图
- 箭头建议 6 步

### 页面上建议写的文字
```text
浏览器发起请求
-> Flask 路由接收
-> 读取 JSON / Supabase
-> render_template 渲染模板
-> 浏览器展示页面
-> 用户继续交互
```

### 对应项目文件
- [app.py](/Users/wkai/Desktop/FlaskProject/app.py)
- [utils/supabase_client.py](/Users/wkai/Desktop/FlaskProject/utils/supabase_client.py)
- [templates/base.html](/Users/wkai/Desktop/FlaskProject/templates/base.html)

### 台上讲稿
这一页是整个项目最关键的技术逻辑图。用户在浏览器访问一个页面之后，请求会先到 Flask 路由。路由根据页面类型决定是读取 JSON 数据，还是去 Supabase 查询评论和用户信息。然后 Flask 会把这些数据交给 Jinja2 模板进行渲染，生成 HTML 返回给浏览器。浏览器显示页面后，用户又可以继续进行搜索、登录、评论或向 AI 助手提问。也就是说，我们整个项目的主线就是“请求进入后端，后端组织数据，模板渲染页面，前端继续交互”。

---

## 第 10 页：前端页面设计与响应式布局

### 建议标题
前端设计：Jinja2 + Tailwind + 响应式

### PPT 上展示什么
- 左边放桌面端截图
- 右边放移动端布局示意
- 底部放几个关键类名

### 页面上建议写的文字
- 统一骨架：`base.html`
- 公共组件：`header.html` / `footer.html`
- 响应式类：`md:` / `lg:`
- 典型布局：`grid grid-cols-1 lg:grid-cols-12`
- 视觉风格：统一卡片、颜色、标题体系

### 对应项目文件
- [templates/base.html](/Users/wkai/Desktop/FlaskProject/templates/base.html)
- [templates/header.html](/Users/wkai/Desktop/FlaskProject/templates/header.html)
- [templates/guide.html](/Users/wkai/Desktop/FlaskProject/templates/guide.html)
- [static/css/app.css](/Users/wkai/Desktop/FlaskProject/static/css/app.css)

### 台上讲稿
在前端部分，我们没有采用复杂的前端框架，而是使用了 Flask 模板加 Tailwind CSS 的方式来搭建页面。`base.html` 提供全局骨架，页头页脚作为公共组件复用，不同页面再通过 `extends` 和 `include` 进行组合。为了兼顾手机和电脑端，我们使用了 Tailwind 的响应式断点类，比如 `md:` 和 `lg:`。这样在移动端时页面保持单列，在桌面端时再切换成多列布局。整体样式上，我们也通过统一的颜色、卡片和标题字体，让页面风格更一致。

---

## 第 11 页：JavaScript 交互实现

### 建议标题
前端交互：搜索、弹窗、局部更新

### PPT 上展示什么
- 3 个模块卡片
- 每个卡片写“做了什么”

### 页面上建议写的文字
- `programs.js`
  - 专业关键词筛选
- `faq.js`
  - FAQ 搜索过滤
- `guide.js`
  - 步骤完成状态切换
  - 评论区异步加载
- `login_modal.js`
  - 登录注册弹窗切换

### 对应项目文件
- [static/js/programs.js](/Users/wkai/Desktop/FlaskProject/static/js/programs.js)
- [static/js/faq.js](/Users/wkai/Desktop/FlaskProject/static/js/faq.js)
- [static/js/guide.js](/Users/wkai/Desktop/FlaskProject/static/js/guide.js)
- [static/js/components/login_modal.js](/Users/wkai/Desktop/FlaskProject/static/js/components/login_modal.js)

### 台上讲稿
在前端交互部分，我们主要用了原生 JavaScript。比如 `programs.js` 和 `faq.js` 负责关键词搜索筛选，用户输入后页面会立即过滤相关内容；`guide.js` 负责申请步骤的完成状态切换，还会通过接口异步加载评论区内容；`login_modal.js` 则负责登录注册弹窗的打开、关闭和标签切换。这样做的优点是逻辑比较直接，适合教学，也能让我们更清楚地理解前后端之间是如何通过请求和 DOM 更新协作的。

---

## 第 12 页：用户登录、Session、Cookie 与评论

### 建议标题
用户交互：登录状态与评论系统

### PPT 上展示什么
- 左边放登录流程
- 右边放评论流程
- 中间补一个 Session/Cookie 对照

### 页面上建议写的文字
- 登录成功后保存：
  - `user_id`
  - `user_name`
  - `user_email`
  - `avatar_seed`
- Session：保存登录态和步骤完成状态
- Cookie：保存 `last_stage`
- 评论：登录后提交，写入 Supabase

### 对应项目文件
- [app.py](/Users/wkai/Desktop/FlaskProject/app.py)
- [templates/login_modal.html](/Users/wkai/Desktop/FlaskProject/templates/login_modal.html)
- [static/js/components/login_modal.js](/Users/wkai/Desktop/FlaskProject/static/js/components/login_modal.js)
- [tests/test_auth_session.py](/Users/wkai/Desktop/FlaskProject/tests/test_auth_session.py)

### 台上讲稿
用户交互部分主要涉及登录、Session、Cookie 和评论功能。用户登录成功后，后端会把 `user_id`、昵称、邮箱和头像颜色等信息保存在 Session 中，页面就可以根据登录状态显示不同的内容，比如评论区是否可用、右上角是否显示用户菜单。同时我们也使用了 Cookie 记录用户上一次浏览的申请阶段，提高页面体验。评论功能则要求用户先登录，提交后再由后端写入 Supabase，这样评论就和具体用户绑定起来了。

---

## 第 13 页：Supabase 数据存储

### 建议标题
数据持久化：Supabase 在项目中的作用

### PPT 上展示什么
- 三个数据库对象的方框图
- `users`、`comments`、`rag_chunks`

### 页面上建议写的文字
- `users`
  - 注册账号
  - 邮箱
  - 密码哈希
  - 昵称
- `comments`
  - 页面评论
  - `user_id` 绑定用户
- `rag_chunks`
  - 向量片段
  - 用于 AI 检索

### 对应项目文件
- [utils/supabase_client.py](/Users/wkai/Desktop/FlaskProject/utils/supabase_client.py)
- [docs/supabase_comments.sql](/Users/wkai/Desktop/FlaskProject/docs/supabase_comments.sql)
- [docs/supabase_rag.sql](/Users/wkai/Desktop/FlaskProject/docs/supabase_rag.sql)

### 台上讲稿
为了让项目不仅能展示静态内容，还能具备真实的用户交互能力，我们使用了 Supabase 作为数据存储服务。`users` 表用于保存用户账号信息，比如邮箱、密码哈希和昵称；`comments` 表用于保存评论，并通过 `user_id` 绑定用户；`rag_chunks` 则用于保存知识片段及其向量数据，为 AI 助手提供检索能力。也就是说，Supabase 在这个项目里既承担了用户与评论的持久化，也承担了 AI 检索的数据底座。

---

## 第 14 页：AI 助手与 RAG 流程

### 建议标题
AI 助手：RAG 检索增强的实现思路

### PPT 上展示什么
- 一张 RAG 流程图
- 最好分成 5 步

### 页面上建议写的文字
```text
用户提问
-> 知识库切片
-> 生成 embedding
-> Supabase 向量检索
-> 大模型生成回答
-> 返回来源
```

补充一行：
- 如果 RAG 不可用，自动回退到本地关键词检索

### 对应项目文件
- [utils/knowledge_base.py](/Users/wkai/Desktop/FlaskProject/utils/knowledge_base.py)
- [utils/rag_pipeline.py](/Users/wkai/Desktop/FlaskProject/utils/rag_pipeline.py)
- [scripts/ingest_rag.py](/Users/wkai/Desktop/FlaskProject/scripts/ingest_rag.py)
- [utils/zhipu_client.py](/Users/wkai/Desktop/FlaskProject/utils/zhipu_client.py)
- [tests/test_assistant_rag.py](/Users/wkai/Desktop/FlaskProject/tests/test_assistant_rag.py)

### 台上讲稿
AI 助手并不是直接把问题丢给大模型，而是先经过一个 RAG，也就是检索增强生成的流程。我们先把项目中的 FAQ、专业数据、申请步骤和补充知识组织成知识片段，再对这些片段进行切片和 embedding，写入 Supabase 的向量表中。当用户提问时，系统先对问题生成向量，再去数据库中检索最相关的知识片段，最后把检索到的上下文交给大模型生成回答。这样回答会更贴近项目知识库，也更可控。如果外部向量检索或者模型调用失败，系统还会回退到本地关键词检索，保证页面依然可用。

---

## 第 15 页：团队分工、学习路径与未来优化

### 建议标题
团队分工、学习收获与未来计划

### PPT 上展示什么
- 上半部分写 5 人分工
- 下半部分写未来优化
- 右下角可以放一句总结

### 页面上建议写的文字
- 第 1 位：网站骨架 + 后端数据 + AI RAG
- 第 2 位：前端 UI + PPT
- 第 3 位：数据抓取与清洗方案
- 第 4 位：材料收集与结构化整理
- 第 5 位：登录与用户交互

未来优化：
- 增加 BeautifulSoup 抓取模块
- 数据分层：原始 / 清洗 / 展示 / RAG
- 拆分 `app.py`
- 完善评论和用户体验

总结语：
- 从页面展示到数据组织，再到 AI 助手，我们完成了一个较完整的课程项目闭环

### 对应项目文件
- [docs/presentation_guide.md](/Users/wkai/Desktop/FlaskProject/docs/presentation_guide.md)
- [docs/project_structure.md](/Users/wkai/Desktop/FlaskProject/docs/project_structure.md)
- [docs/team_split.md](/Users/wkai/Desktop/FlaskProject/docs/team_split.md)

### 台上讲稿
最后我们想从团队协作和学习过程做一个总结。这个项目并不是某一个人独立完成的，而是围绕网站骨架、前端界面、数据组织、登录交互和 AI 助手这几个方向进行分工协作。对我们来说，最大的收获不是只学会了某个单点技术，而是第一次把 Flask、模板、前端交互、结构化数据、用户系统和 AI 检索放到同一个项目中理解。未来如果继续完善这个项目，我们希望加入官网自动抓取、更加清晰的数据分层，以及更细致的后端模块拆分，让这个项目从课程作品进一步走向更完整的应用。

---

## 最后建议：PPT 排版怎么做

### 1. 每页只保留 3 到 5 个关键词

不要把讲稿全文写进 PPT。

### 2. 多放截图、流程图、表格

你们这个项目最适合：
- 页面截图
- 目录树
- 数据流图
- 模块关系图

### 3. 每一页讲 30 到 60 秒

不要某一页讲太久。

### 4. 演示和讲稿要配合

讲到首页就切首页，讲到登录就切登录，讲到助手就切助手。

## 如果你们还想继续补充

下一步可以继续做这 3 个东西：
- 把这 15 页进一步缩成真正适合 PPT 的“每页可直接复制文字”
- 给 5 位同学分别写 1 分钟到 2 分钟的个人发言稿
- 帮你们整理一个答辩问题清单和参考回答

# PPT 设计方案（中文 + English，可直接用于制作与演讲）

> 文档目标：给 5 人小组直接落地做 PPT 与演讲。  
> 输出内容：逐页布局（详细坐标）+ 每页内容清单 + 每页讲稿。  
> 口径统一：BeautifulSoup 为离线抓取与清洗，不是官网实时同步。

---

## 中文方案（详细版）

### 0. 全局版式规范（所有页面都按这个做）
- 画布比例：16:9（推荐 1920 x 1080）
- 统一安全边距：左右各 96px（约 5%）
- 页面三层：
  - 标题层：Y = 40~145（约 10%）
  - 主内容层：Y = 162~928（约 71%）
  - 页脚层：Y = 944~1028（约 8%）
- 字号建议：
  - 主标题：52-60
  - 二级标题：34-40
  - 正文：24-30
  - 注释：18-22
- 视觉系统（统一）：
  - 背景：`#f5f4ed`
  - 主文字：`#141413`
  - 主强调色：`#c96442`
  - 深色按钮/标签：`#210F37`
  - 边框：`#e8e6dc`
- 动画建议（统一）：
  - 每页最多 3 次出现动画
  - 仅用淡入（0.3s）+ 顺序出现

### 1. 主讲分配
1. 土土：第 1、6、7 页
2. 塔塔：第 8、9、10 页
3. 冯少：第 4、5、11 页
4. Kai：第 2、12、13 页
5. 洗神：第 3、14、15 页

---

## 第 1 页 封面（土土）
### 布局（像素坐标）
- 标题：`x=96, y=80, w=980, h=120`
- 副标题：`x=96, y=220, w=760, h=120`
- 成员/课程信息：`x=96, y=360, w=760, h=200`
- 首页大图：`x=1050, y=150, w=770, h=760`
- 页脚标签（组名/日期）：`x=96, y=960, w=1728, h=52`

### 页面内容（可直接粘贴）
- 标题：港中文申请一站式助手（ToCU）
- 副标题：Flask 课程项目汇报
- 信息：课程名称 / 小组成员 / 汇报日期
- 关键词：Flask、Jinja2、JavaScript、Supabase、RAG

### 讲稿（约 50-70 秒）
大家好，我们小组今天汇报的项目是“港中文申请一站式助手（ToCU）”。这个项目聚焦研究生申请场景，把分散的信息整理成统一的网站入口。用户可以先从首页进入，再根据需求去专业速查、操作步骤或智能助手页面。我们在这个项目中完整串联了前端交互、后端路由、数据库和 AI 检索增强流程。接下来我们会按“问题背景—系统架构—核心功能—技术实现—测试与总结”的顺序进行汇报。

---

## 第 2 页 背景与目标（Kai）
### 布局
- 左栏痛点卡片区：`x=96, y=180, w=820, h=700`
- 右栏目标卡片区：`x=980, y=180, w=840, h=700`
- 顶部小标题条：`x=96, y=110, w=1728, h=60`

### 页面内容
- 左栏（用户痛点）：
  1. 信息分散：官网、流程说明、经验信息不在一个入口
  2. 时间压力：节点多，容易错过截止和补件时机
  3. 材料复杂：不同项目要求差异大，容易漏项
- 右栏（项目目标）：
  1. 统一入口：把“查信息、看步骤、问问题”放在同一站点
  2. 降低门槛：结构化展示，减少检索与判断成本
  3. 增强可信：回答附来源，检索失败有回退机制

### 讲稿（60-80 秒）
我们做这个项目的起点是用户痛点非常明确。第一是信息分散，申请者经常在多个来源来回切换。第二是时间节点密集，尤其是提交、补件、缴费等阶段容易漏。第三是材料规则复杂，不同学院和项目要求差异很大。针对这些问题，我们提出三个目标：第一，做统一入口；第二，用结构化页面降低理解门槛；第三，在 AI 问答里强调可验证性，通过来源展示和失败回退保证可用性。

---

## 第 3 页 汇报结构与分工（洗神）
### 布局
- 流程时间轴：`x=96, y=180, w=1728, h=180`
- 五人分工卡片（5 列）：`x=96, y=390, w=1728, h=420`
- 演示顺序条：`x=96, y=840, w=1728, h=90`

### 页面内容
- 汇报流程：背景 -> 架构 -> 前端 -> 抓取清洗 -> AI&RAG -> 后端与测试 -> 总结
- 分工（每人一句）：
  - 土土：首页视觉、布局和响应式
  - 塔塔：专业速查 + BeautifulSoup 抓取清洗
  - 冯少：路由、模板、信息结构
  - Kai：智能助手、RAG 流程
  - 洗神：登录注册、评论、Supabase、错误处理

### 讲稿（50-70 秒）
这一页先说明我们怎么讲，以及谁负责什么。汇报会按用户使用路径推进，从背景和目标进入系统架构，再到首页、专业速查、步骤页与智能助手，最后回到后端、测试和总结。分工上我们按模块负责，避免重复讲同一个点。这样既能体现协作，也能保证每位同学都讲自己最熟悉的实现细节，整体叙事会更连贯。

---

## 第 4 页 功能与系统架构（冯少）
### 布局
- 中央架构图主画布：`x=160, y=190, w=1600, h=520`
- 左下“输入层”：`x=160, y=740, w=760, h=170`
- 右下“输出层”：`x=1000, y=740, w=760, h=170`

### 页面内容（架构图节点文案）
- 输入层：
  - 结构化数据（Programs / Stages / Guide Steps）
  - RAG 补充知识文本
  - 用户交互（登录、评论、提问）
- 应用层：
  - 首页（入口分流）
  - 专业速查（检索筛选）
  - 操作步骤（阶段与步骤）
  - 智能助手（检索增强问答）
- 数据层：
  - Supabase users / comments / rag_chunks
- 输出层：
  - 页面内容展示
  - 评论和进度状态
  - 带来源的回答

### 讲稿（70-90 秒）
这里展示的是完整系统架构。最上层是输入，包括结构化内容数据、RAG 补充知识和用户交互。中间是四个核心功能模块：首页负责分流，专业速查负责检索，操作步骤负责流程执行，智能助手负责问答支持。底层是 Supabase 数据支撑用户、评论和向量片段。最终输出是三类：可读页面、可保存的用户行为、可追溯来源的助手回答。这个架构的重点是模块清晰、路径可解释、数据可追溯。

---

## 第 5 页 技术栈与代码结构（冯少）
### 布局
- 左侧技术栈矩阵：`x=96, y=180, w=820, h=700`
- 右侧目录树+说明：`x=980, y=180, w=840, h=700`

### 页面内容（技术栈矩阵）
- 前端：Jinja2 模板、JavaScript 交互、Tailwind + 自定义 CSS
- 后端：Flask 路由、表单处理、Session 状态管理
- 数据层：JSON 内容文件 + Supabase 持久化
- AI 层：Embedding + 向量检索 + 生成回答（RAG）
- 工具层：环境变量管理、脚本化知识入库

### 页面内容（目录树）
```text
app.py                # 统一路由入口
content/              # 结构化内容数据
templates/            # 页面模板
static/               # 样式与前端脚本
utils/                # 数据与AI服务逻辑
scripts/              # 入库脚本
docs/                 # 文档与SQL
tests/                # 测试用例
```

### 讲稿（70-90 秒）
技术选型上，我们优先考虑教学可理解性和可演示性。前端使用模板加原生 JS，逻辑直观；后端使用 Flask 统一管理页面和交互；数据层采用 JSON + Supabase，方便内容维护与状态持久化；AI 部分采用 RAG 让回答基于已知资料。目录结构也是按职责拆分：入口、内容、模板、静态资源、服务逻辑、脚本和测试分层清晰，便于多人协作。

---

## 第 6 页 首页功能与信息架构（土土）
### 布局
- 左：首页截图（带 1/2/3 标注）：`x=96, y=180, w=980, h=700`
- 右：说明卡片区：`x=1120, y=180, w=700, h=700`

### 页面内容
- 标注 1：专业速查入口（快速比较）
- 标注 2：操作步骤入口（阶段化执行）
- 标注 3：智能助手入口（即时问答）
- 设计目标：用户 1-2 次点击直达任务场景

### 讲稿（60-80 秒）
首页是全站的信息分发中心。我们没有把大量信息堆在首页，而是保留三个清晰入口：查专业、看步骤、问助手。这样用户第一眼就能根据任务类型进入正确页面。视觉上首页用大标题和卡片入口建立主次关系，避免认知负担。信息架构的核心不是“内容越多越好”，而是“最短路径到达目标功能”。

---

## 第 7 页 响应式与视觉系统（土土）
### 布局
- 上半区：桌面/移动对比图：`x=96, y=180, w=1728, h=350`
- 下半区：设计规则卡片：`x=96, y=560, w=1728, h=320`

### 页面内容
- 响应式策略：
  1. 桌面端主导航完整显示
  2. 移动端导航改为紧凑布局
  3. 搜索区小屏纵向、大屏横向
- 视觉系统：
  - 统一色板、统一按钮、统一圆角、统一字体
  - 保持跨页面一致性，减少学习成本

### 讲稿（60-80 秒）
这一页强调的是体验一致性。我们不是只做“能看”的适配，而是做“可用”的适配。桌面和移动端在信息量和交互方式不同，所以导航和搜索布局都做了针对性调整。视觉系统层面，我们统一了颜色、按钮、圆角和字体，让用户在不同页面切换时没有割裂感。这种一致性对课程项目很关键，因为它直接体现了前端规范能力。

---

## 第 8 页 专业速查功能（塔塔）
### 布局
- 顶部流程：`x=96, y=170, w=1728, h=120`
- 左“筛选前”：`x=96, y=320, w=840, h=560`
- 右“筛选后”：`x=980, y=320, w=840, h=560`

### 页面内容
- 支持关键词检索字段：
  - 专业名（中/英）
  - 学院
  - 方向
- 支持学院筛选列表：
  - 全部、文学院、商学院、教育学院、工学院、跨学院、法学院、医学院、理学院、社科学院
- 卡片展示字段：
  - 专业名、学位、学院、方向、语言要求、截止日期、官网入口

### 可贴数据样例
```json
{
  "name_zh": "信息工程硕士",
  "name_en": "MSc in Information Engineering",
  "college": "工学院",
  "focus": "数据与智能系统",
  "language": "IELTS 6.5 / TOEFL 79",
  "deadline": "2027-01-15"
}
```

### 讲稿（70-90 秒）
专业速查页的目标是“低成本比较”。用户可以用关键词搜索，也可以按学院筛选，结果会实时更新。我们把专业信息组织成统一卡片，每张卡都包含申请决策最关心的字段，比如方向、语言和截止日期，并提供官网入口。这样用户不需要在多个页面来回切换，就能先完成第一轮筛选，再进入更深层步骤。

---

## 第 9 页 BeautifulSoup 抓取与清洗（塔塔）
### 布局
- 中央流程图：`x=180, y=210, w=1560, h=500`
- 底部高亮口径框：`x=180, y=740, w=1560, h=160`

### 页面内容（流程图）
1. 选定目标官网页面
2. 抓取 HTML 内容
3. 解析字段（专业、学院、语言、截止、链接）
4. 清洗标准化（去重、日期统一、字段映射）
5. 输出结构化数据文件

### 必放口径（建议原文）
- “本项目中的抓取流程是离线批量更新，不是官网实时同步。”

### 讲稿（70-90 秒）
这一页要讲清边界。塔塔负责的 BeautifulSoup 流程是已经完成的，但它不是实时服务，而是离线批量更新流程。我们先抓取，再做清洗，把信息转成统一结构。这样做的好处是数据质量可控、字段稳定，适合课堂项目演示和后续维护。换句话说，官网有变化时，我们需要重新执行抓取与清洗，而不是自动实时联动。

---

## 第 10 页 抓取数据如何支撑页面与 RAG（塔塔）
### 布局
- 左：页面数据去向图：`x=96, y=190, w=840, h=690`
- 右：RAG 数据去向图：`x=980, y=190, w=840, h=690`

### 页面内容
- 去向 A（页面）：清洗后数据进入 `programs.json`，驱动专业速查展示
- 去向 B（知识库）：清洗后高价值信息用于补充 RAG 知识
- 统一收益：前端页面与 AI 问答引用同源信息，减少口径冲突

### 讲稿（70-90 秒）
这页的核心是“同源数据双用途”。清洗后的结构化数据一部分用于页面展示，另一部分用于知识检索。这样做有两个价值：第一，前端显示和 AI 回答使用相同知识源，减少前后口径不一致；第二，后续更新时只要更新一次数据，两个能力都能受益。这个设计让数据工作真正服务到产品功能，而不是孤立存在。

---

## 第 11 页 路由、模板与信息结构（冯少）
### 布局
- 左：URL 映射表：`x=96, y=190, w=840, h=690`
- 右：模板复用图：`x=980, y=190, w=840, h=690`

### 页面内容
- URL 映射示例：
  - `/` -> 首页
  - `/programs` -> 专业速查
  - `/guide` -> 阶段列表
  - `/guide/<stage_slug>` -> 阶段详情
  - `/assistant` -> 智能助手
- 模板复用关系：
  - `base`（全局骨架）
  - `header/footer/login modal`（公共组件）
  - 各页面模板（业务内容）
- 体验点：返回“操作步骤”时可显示“继续上次进度”

### 讲稿（70-90 秒）
这个模块强调“结构清晰”。用户访问 URL 后，后端路由把请求分发到对应页面，再由模板渲染返回。模板层面我们采用基础骨架加公共组件复用，保证不同页面风格一致。信息结构上，操作步骤页支持记忆上次阶段，帮助用户继续任务。这些设计共同目标是让网站路径可预测、维护成本可控。

---

## 第 12 页 AI 助手界面与消息 API（Kai）
### 布局
- 左：聊天界面截图：`x=96, y=190, w=980, h=690`
- 右：请求/响应示意：`x=1120, y=190, w=700, h=690`

### 页面内容（可直接贴）
请求：
```json
POST /assistant/message
{
  "message": "推荐信要提前多久联系老师？"
}
```
响应：
```json
{
  "ok": true,
  "question": "推荐信要提前多久联系老师？",
  "answer": "建议提前 4-8 周联系老师。",
  "sources": [{"source": "官方知识库", "link": "/assistant"}],
  "elapsed_ms": 680
}
```
交互特性：
- 建议问题一键发送
- Enter 发送，Shift+Enter 换行
- 状态提示：检索中 -> 生成中 -> 完成

### 讲稿（70-90 秒）
智能助手的交互重点是“低门槛提问 + 可解释返回”。用户输入问题后，前端通过消息 API 发送请求，后端返回答案、来源和耗时。我们特意保留来源字段，方便用户核验信息出处。界面上也做了状态提示，让用户知道系统当前在检索还是生成，避免等待焦虑。这个模块不只是聊天界面，更是把检索结果可视化给用户。

---

## 第 13 页 RAG 检索与回退机制（Kai）
### 布局
- 上：主流程图：`x=96, y=190, w=1728, h=360`
- 下：参数与回退卡片：`x=96, y=580, w=1728, h=300`

### 页面内容
主流程：
1. 用户提问
2. 问题向量化
3. 向量库检索 TopK 片段
4. 组合上下文生成回答
5. 返回答案与来源

参数示例：
- TopK：2
- 最低相似度：0.45
- 上下文截断：220 字符
- 文本切片：420 字符，重叠 80

回退策略：
- 当 RAG 不可用或超时，自动回退到本地关键词检索，保证可用性。

### 讲稿（70-90 秒）
这一页讲的是 AI 能力的可靠性设计。RAG 路径先检索再生成，减少模型自由发挥。我们设置了相似度阈值和上下文长度控制，避免噪音信息影响结果。如果向量检索或外部模型调用失败，系统会自动切回本地检索逻辑，至少给出可参考答案。也就是说，我们把“回答质量”和“服务可用性”分层保障，不把系统稳定性赌在单一路径上。

---

## 第 14 页 登录注册、评论与 Supabase（洗神）
### 布局
- 左：认证与 session 流程图：`x=96, y=190, w=840, h=690`
- 右：数据表关系图：`x=980, y=190, w=840, h=690`

### 页面内容
登录与 session：
- 登录成功后写入：`user_id`、`user_name`、`user_email`、`avatar_seed`
- 未登录发表评论会被拦截并引导登录

数据库结构（可做三列表）：
- users：账号与身份信息
- comments：评论内容与页面定位（page_type/page_key）
- rag_chunks：知识片段与向量

关系说明：
- comments.user_id 关联 users.id
- 评论与用户绑定，保证身份可追溯

### 讲稿（70-90 秒）
这一页是后端数据链路。认证成功后我们把必要身份信息写入 session，页面据此控制权限和展示状态。评论模块要求登录后提交，避免匿名污染数据。数据库方面，users 管账号，comments 管互动，rag_chunks 管知识向量。通过外键和字段设计，我们实现了“谁说了什么、在哪个步骤说的”的可追溯结构，这也是后续做分析和治理的基础。

---

## 第 15 页 错误处理、测试与总结（洗神）
### 布局
- 上：错误处理矩阵：`x=96, y=190, w=1728, h=260`
- 中：测试结果卡片：`x=96, y=480, w=1728, h=230`
- 下：总结与 Q&A：`x=96, y=740, w=1728, h=160`

### 页面内容
错误处理矩阵：
- 页面级：404/500 统一错误页
- 接口级：返回可理解错误消息
- 前端级：失败提示与重试引导

测试结论（直接贴）：
- 核心测试总数：22
- 通过结果：22 passed
- 覆盖模块：
  - 主页面与路由
  - 登录/会话
  - 助手 API
  - RAG 回退逻辑

可贴命令：
```bash
.venv/bin/python -m unittest tests.test_course_structure tests.test_auth_session tests.test_assistant_chat_api tests.test_assistant_rag -v
```

### 讲稿（70-90 秒）
最后一页我们汇总系统可靠性。我们把异常处理分为页面、接口和前端三层，目标是“出错可见、可理解、可恢复”。在测试方面，核心用例已全部通过，覆盖路由、认证、助手接口和回退机制。整体上，这个项目不仅完成了功能演示，也体现了工程化思路：结构清晰、口径统一、可验证、可维护。接下来欢迎老师和同学提问。

---

## 备用页（答辩）

## B1 数据库与 SQL 细节
### 布局
- 左：users/comments 字段与关系
- 右：rag_chunks 与 RPC 逻辑

### 可讲要点
- 为什么评论必须绑定用户
- 为什么向量检索要做相似度阈值
- 为什么需要 upsert / match 两个 RPC

### 30 秒讲稿
这一页主要回答“为什么这么建表”。users 与 comments 的绑定保证行为可追溯，rag_chunks 则服务检索增强。通过 upsert 与 match，我们把知识更新和在线检索分开，既保证更新效率，也保证查询稳定。

## B2 风险边界与后续规划
### 布局
- 上：当前边界
- 下：近期计划 / 中期计划 / 长期计划 三列

### 可讲要点
- 当前边界：离线抓取，不是实时同步
- 近期：抓取脚本纳入主仓 + 自动校验
- 中期：数据流水线分层（raw/clean/curated）
- 长期：模块拆分与服务化

### 30 秒讲稿
我们当前版本优先保证功能可用和演示清晰，所以抓取流程是离线更新。后续会逐步推进自动校验和数据分层，再进一步做模块拆分，降低耦合、提高可维护性。

---

## English Plan (Detailed)

### 0. Global Deck Rules
- Deck size: 15 core slides + 2 backup slides
- Duration: 15-18 minutes
- Ratio: 16:9
- Fixed zones:
  - Title zone (top 10%)
  - Content zone (middle 72%)
  - Footer zone (bottom 6%-8%)
- Unified style:
  - Warm paper background
  - Dark body text
  - One accent color for highlights/buttons

### 1. Speaker Allocation
1. Tutu: Slides 1, 6, 7
2. Tata: Slides 8, 9, 10
3. Fengshao: Slides 4, 5, 11
4. Kai: Slides 2, 12, 13
5. Xishen: Slides 3, 14, 15

---

## Slide 1 Cover (Tutu)
### Layout
- Left top: project title
- Left middle: course + team info
- Right: homepage hero screenshot

### Slide Copy
- Title: ToCU — CUHK Application One-Stop Assistant
- Subtitle: Flask Course Project Presentation
- Keywords: Flask / Jinja2 / JavaScript / Supabase / RAG

### Speaker Notes (50-70s)
Hello everyone. Today we present ToCU, our one-stop assistant for CUHK applications. The project organizes scattered application information into one clear website flow: search programs, follow step-by-step guidance, and ask the AI assistant. In this project, we integrated frontend interaction, backend routing, database persistence, and retrieval-augmented AI answering into one coherent product.

---

## Slide 2 Problem & Goals (Kai)
### Layout
- Left: three pain points
- Right: three product goals

### Slide Copy
- Pain points:
  1. Information is scattered across different channels
  2. Timeline is complex and deadline-sensitive
  3. Material requirements are easy to miss
- Goals:
  1. Build one unified entry point
  2. Support search + guidance + Q&A workflow
  3. Keep answers source-grounded and reliable

### Speaker Notes (60-80s)
Our project starts from concrete user pain. Applicants face fragmented information, many timeline checkpoints, and complicated material requirements. We designed ToCU with three goals: unify the entry point, reduce decision friction through structured pages, and improve trust through source-grounded answers with fallback behavior.

---

## Slide 3 Agenda & Team Roles (Xishen)
### Layout
- Top: presentation timeline
- Middle: five role cards
- Bottom: demo sequence

### Slide Copy
- Flow: Problem -> Architecture -> Frontend -> Data pipeline -> AI/RAG -> Backend & tests -> Summary
- Roles:
  - Tutu: homepage UI + responsive design
  - Tata: scraping/cleaning + programs module
  - Fengshao: routing/template architecture
  - Kai: assistant + RAG
  - Xishen: auth/comments/supabase/error handling

### Speaker Notes (50-70s)
This page aligns expectations for the whole presentation. We follow the product flow and keep each module owned by one presenter. This division helps us avoid overlap and ensures each part is explained by the person who implemented it most deeply.

---

## Slide 4 System Architecture (Fengshao)
### Layout
- Center: architecture diagram
- Bottom left: inputs
- Bottom right: outputs

### Slide Copy
- Inputs: structured content, RAG text, user interactions
- App modules: Home / Programs / Guide / Assistant
- Data layer: Supabase users/comments/rag_chunks
- Outputs: rendered pages, persisted interactions, source-linked answers

### Speaker Notes (70-90s)
The architecture is intentionally modular. Inputs include structured content and user interactions. Four modules handle core user tasks. Supabase stores identity, comments, and vector chunks. Outputs are not only UI pages but also persistent user state and traceable assistant answers.

---

## Slide 5 Tech Stack & Project Structure (Fengshao)
### Layout
- Left: stack matrix
- Right: project tree

### Slide Copy
- Frontend: Jinja2 templates + JavaScript + Tailwind/CSS
- Backend: Flask routes/forms/session
- Data: JSON content + Supabase
- AI: Embedding + vector retrieval + answer generation

### Speaker Notes (70-90s)
Our stack favors clarity and teachability. The backend stays compact with Flask, the frontend remains transparent with template + JS patterns, and data/AI concerns are separated into dedicated layers. This structure supports both classroom explanation and team collaboration.

---

## Slide 6 Home Information Architecture (Tutu)
### Layout
- Left: annotated screenshot
- Right: entry-point explanations

### Slide Copy
- Three primary entries:
  1. Program lookup
  2. Step-by-step guide
  3. AI assistant
- UX objective: reach key tasks in 1-2 clicks

### Speaker Notes (60-80s)
The homepage is designed as a task router, not an information dump. Users immediately choose between program comparison, procedural guidance, or Q&A support. This improves orientation speed and reduces cognitive load.

---

## Slide 7 Responsive & Visual Consistency (Tutu)
### Layout
- Top: desktop/mobile comparison
- Bottom: visual token summary

### Slide Copy
- Responsive behavior:
  1. Full navigation on desktop
  2. Compact nav mode on mobile
  3. Search layout adapts by screen width
- Consistency: same palette, spacing rhythm, button style, typography

### Speaker Notes (60-80s)
Responsive design here is not only about shrinking UI. It is about preserving usability under different contexts. We keep visual consistency across pages while adjusting navigation and layout patterns based on device constraints.

---

## Slide 8 Programs Feature (Tata)
### Layout
- Top: filter logic flow
- Left: before filter
- Right: after filter

### Slide Copy
- Search dimensions: Chinese/English major names, school, focus
- College filter options: full list by school category
- Card fields: major, degree, language, deadline, official link

### Data Sample
```json
{
  "name_zh": "信息工程硕士",
  "name_en": "MSc in Information Engineering",
  "college": "工学院",
  "focus": "数据与智能系统",
  "deadline": "2027-01-15"
}
```

### Speaker Notes (70-90s)
This page minimizes comparison effort. Users can combine keyword search and college filtering, and each card exposes decision-critical fields. The goal is to complete first-round filtering quickly before users dive into detailed requirements.

---

## Slide 9 BeautifulSoup Pipeline (Tata)
### Layout
- Center: pipeline diagram
- Bottom: highlighted scope note

### Slide Copy
- Pipeline: target pages -> parse -> extract -> clean -> write
- Scope note (must show):
  - This is an offline batch update pipeline, not runtime real-time synchronization.

### Speaker Notes (70-90s)
This slide clarifies boundaries. Our BeautifulSoup pipeline is implemented and used for offline data refresh. It improves data quality through extraction and normalization, but it is not a live sync service.

---

## Slide 10 Data Landing for UI + RAG (Tata)
### Layout
- Left: cleaned data to Programs UI
- Right: cleaned data to RAG knowledge input

### Slide Copy
- One cleaned dataset, two outputs:
  1. Program page rendering
  2. Assistant knowledge enrichment
- Benefit: lower inconsistency between displayed content and AI answers

### Speaker Notes (70-90s)
By using the same cleaned source for both UI and RAG inputs, we reduce mismatch risk between what users read and what the assistant says. This design gives us consistency and update efficiency.

---

## Slide 11 Routing & Template Reuse (Fengshao)
### Layout
- Left: URL-to-page mapping
- Right: template reuse diagram

### Slide Copy
- Mapping: URL -> Flask view -> rendered template
- Reuse structure: base layout + shared components + page-specific templates
- UX enhancement: “resume previous stage” card

### Speaker Notes (70-90s)
This module focuses on maintainability. The route map keeps behavior explicit, while template reuse ensures consistent structure and style. The resume-progress feature also improves continuity in multi-step workflows.

---

## Slide 12 Assistant UI & Message API (Kai)
### Layout
- Left: chat interface screenshot
- Right: request/response blocks

### Slide Copy
Request:
```json
POST /assistant/message
{ "message": "How early should I contact recommenders?" }
```
Response:
```json
{
  "ok": true,
  "answer": "Contact recommenders 4-8 weeks earlier.",
  "sources": [{"source": "Official KB", "link": "/assistant"}],
  "elapsed_ms": 680
}
```

### Speaker Notes (70-90s)
The assistant interaction is designed to be simple and transparent. Users ask in natural language, then receive an answer with source references and response timing. This improves both usability and trust.

---

## Slide 13 RAG + Fallback Strategy (Kai)
### Layout
- Top: RAG flow
- Bottom: fallback logic and key parameters

### Slide Copy
- Core flow: query -> embedding -> vector retrieval -> grounded generation -> answer + sources
- Example parameters: TopK=2, min similarity=0.45, context limit=220 chars
- Fallback: switch to local keyword retrieval on RAG timeout/failure

### Speaker Notes (70-90s)
We designed reliability through layered behavior. RAG is preferred for grounded answers, but when vector retrieval is unavailable, local retrieval keeps the service usable. So quality and availability are both addressed.

---

## Slide 14 Auth, Comments, and Supabase (Xishen)
### Layout
- Left: auth/session sequence
- Right: table relationship diagram

### Slide Copy
- Session keys after login:
  - user_id, user_name, user_email, avatar_seed
- Comment rule: login required, then bind comment to user_id
- Table summary: users / comments / rag_chunks

### Speaker Notes (70-90s)
This page shows how interaction data becomes persistent. Session controls identity and permissions, comments are user-bound for traceability, and table separation keeps account data, user content, and vector knowledge independently manageable.

---

## Slide 15 Error Handling, Testing, and Closing (Xishen)
### Layout
- Top: error handling matrix
- Middle: test evidence card
- Bottom: final summary + Q&A

### Slide Copy
- Error handling layers:
  - Page-level (404/500)
  - API-level (friendly error messages)
  - Frontend-level (retry-friendly prompts)
- Test result:
  - Core suite executed: 22 tests
  - Result: all passed

### Speaker Notes (70-90s)
We conclude with reliability. Error handling is layered for visibility and recovery. Core tests passed across routing, auth/session, assistant API, and fallback behavior. This project demonstrates not only feature delivery but also maintainability and verification discipline.

---

## Backup Slides

### B1 SQL Deep Dive
- Layout: left users/comments, right rag_chunks + RPC
- Notes (30s): explain why identity binding and vector retrieval are both necessary

### B2 Scope Boundary & Roadmap
- Layout: top current scope, bottom 3-column roadmap
- Notes (30s): clarify offline crawling boundary and staged improvement plan


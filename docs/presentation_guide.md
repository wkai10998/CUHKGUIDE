# 5 人小组 PPT 汇报与代码理解指南

## 1. 这份文档是给谁的

这份文档是给零基础小组成员使用的，目标不是把每个人都训练成后端工程师，而是帮助大家：
- 看懂这个项目的大致结构
- 知道自己该负责讲什么
- 知道 PPT 应该怎么安排
- 知道接下来按什么顺序理解代码库

## 2. 汇报时最重要的原则

### 2.1 不要按“文件列表”汇报

老师和听众更容易理解的是：
- 这个项目解决什么问题
- 用户怎么使用它
- 页面之间怎么连接
- 数据怎么流动

而不是：
- 我们有几个 HTML
- 我们有几个 JSON
- 我们有几个 Python 文件

所以汇报应该按“用户使用流程”去讲，而不是按目录逐个念文件名。

### 2.2 先讲已经做出来的，再讲准备扩展的

你们现在已经真实完成的部分有：
- Flask 页面
- Jinja2 模板
- Tailwind + CSS 页面布局
- JS 搜索和步骤切换
- Session 登录状态
- Supabase 用户和评论
- AI 助手和 RAG 回退机制

你们还没有完全落地、但可以作为扩展讲的部分有：
- BeautifulSoup 自动抓取
- CSV 批量导入
- 更完整的数据清洗流水线

汇报时要把这两类分开，不要混在一起。

### 2.3 零基础汇报的目标不是“讲很深”，而是“讲清楚”

你们不需要把每个技术原理讲到特别底层。
你们更需要做到：
- 概念说对
- 文件说对
- 页面流程说对
- 分工和学习过程说得真实

## 3. 推荐的 PPT 结构

建议全组做 10 到 12 页左右，不要太多。

### 第 1 页：项目背景

可以讲：
- 申请港中文研究生时，信息分散、流程复杂
- 官方信息、材料准备、时间线、FAQ 和经验往往分散在不同页面
- 所以你们做了一个“申请一站式助手”

### 第 2 页：项目功能总览

展示 5 个核心页面：
- 首页
- 专业速查
- 申请指南
- FAQ
- 智能助手

这里建议放 1 张总览图或者 5 张小截图。

### 第 3 页：项目技术栈

建议简洁列出：
- Flask：后端框架和路由
- Jinja2：模板渲染
- Tailwind CSS：页面布局和响应式
- JavaScript：前端交互
- Session/Cookie：登录和状态保存
- Supabase：用户、评论、RAG 数据库
- 智谱 API：Embedding 和回答

### 第 4 页：项目目录结构

这页可以用 [docs/project_structure.md](/Users/wkai/Desktop/FlaskProject/docs/project_structure.md) 的内容，讲这些目录：
- `app.py`
- `content/`
- `templates/`
- `static/`
- `utils/`
- `scripts/`
- `tests/`

### 第 5 页：用户使用流程

推荐画成一条流程：

```text
打开首页
-> 查看时间线和功能入口
-> 浏览专业/FAQ/申请步骤
-> 登录后评论与保存状态
-> 向 AI 助手提问
```

这一页特别重要，因为它能把你们全组的内容串起来。

### 第 6 页：前端页面设计

这里重点讲：
- 页面骨架如何复用
- 导航栏、页头、页脚如何统一
- 响应式布局如何适配手机和桌面
- JS 如何实现搜索和局部更新

### 第 7 页：后端与用户交互

这里讲：
- Flask 路由如何处理 GET 和 POST
- 登录注册如何写入 Session
- 评论如何提交到 Supabase
- 完成状态如何保存在 Session 中

### 第 8 页：AI 助手与 RAG

这里讲最简单清楚的版本：
- 用户提问
- 系统先检索知识片段
- 再把相关内容交给模型生成回答
- 如果向量检索不可用，就回退到本地关键词检索

### 第 9 页：小组分工

这页直接按 5 个人写：
- 谁负责哪块
- 用到了什么技术
- 对应哪些文件

### 第 10 页：项目优化与未来计划

可以讲：
- 加入 BeautifulSoup 抓取官网信息
- 数据分成原始、清洗、展示三层
- 拆分 `app.py`
- 提高评论和用户系统完整度

### 第 11 页：项目收获

这里讲：
- 学会了前后端如何协作
- 知道了结构化数据在项目里的作用
- 理解了登录状态、评论、RAG 等真实功能
- 体会到团队协作和分工的重要性

### 第 12 页：演示页或答辩备用页

可以放：
- 页面截图
- 功能流程图
- 简化版目录树

## 4. 5 个人怎么分工讲

下面这个分法贴近你给出的方向，也贴近现在真实代码。

### 4.1 第 1 位同学：网站骨架 + 后端数据 + AI RAG 助手

#### 主要负责内容
- 介绍整个网站是怎么跑起来的
- 解释 Flask 路由和页面之间的连接
- 说明 AI 助手的工作流程

#### 建议重点文件
- [app.py](/Users/wkai/Desktop/FlaskProject/app.py)
- [utils/rag_pipeline.py](/Users/wkai/Desktop/FlaskProject/utils/rag_pipeline.py)
- [utils/knowledge_base.py](/Users/wkai/Desktop/FlaskProject/utils/knowledge_base.py)
- [utils/supabase_client.py](/Users/wkai/Desktop/FlaskProject/utils/supabase_client.py)
- [scripts/ingest_rag.py](/Users/wkai/Desktop/FlaskProject/scripts/ingest_rag.py)

#### 需要掌握的关键词
- Flask
- route
- render_template
- request / response
- JSON
- RAG
- embedding
- Supabase

#### 汇报时可以怎么说
- 用户访问一个页面时，Flask 会根据 URL 找到对应函数
- 函数从 JSON 或数据库中取数据
- 再用 Jinja2 渲染成 HTML 返回页面
- AI 助手则会从知识库中检索相关内容，再生成回答

### 4.2 第 2 位同学：前端 UI + PPT

#### 主要负责内容
- 讲页面长什么样
- 讲布局怎么做
- 讲响应式怎么实现
- 负责把全组内容整理成统一的 PPT 风格

#### 建议重点文件
- [templates/base.html](/Users/wkai/Desktop/FlaskProject/templates/base.html)
- [templates/header.html](/Users/wkai/Desktop/FlaskProject/templates/header.html)
- [templates/guide.html](/Users/wkai/Desktop/FlaskProject/templates/guide.html)
- [static/css/app.css](/Users/wkai/Desktop/FlaskProject/static/css/app.css)

#### 需要掌握的关键词
- Tailwind CSS
- 响应式布局
- `md:` / `lg:`
- grid
- flex
- 组件复用

#### 汇报时可以怎么说
- 我们使用了统一骨架页面
- 头部和底部在多个页面中复用
- 通过 Tailwind 的断点类适配移动端和桌面端
- 页面视觉风格通过统一颜色和卡片样式保持一致

### 4.3 第 3 位同学：数据抓取

#### 主要负责内容
- 讲未来的数据来源
- 讲官网信息怎样抓取和清洗
- 讲为什么结构化数据很重要

#### 当前项目里的真实情况
- 当前项目已经在使用 JSON 数据
- 但仓库里还没有真正写出 BeautifulSoup 抓取脚本
- 所以这位同学汇报时要明确说明：这一部分是“下一步扩展方向”

#### 建议重点文件
- [content/programs.json](/Users/wkai/Desktop/FlaskProject/content/programs.json)
- [content/faq.json](/Users/wkai/Desktop/FlaskProject/content/faq.json)
- [content/guide_steps.json](/Users/wkai/Desktop/FlaskProject/content/guide_steps.json)
- [utils/content_loader.py](/Users/wkai/Desktop/FlaskProject/utils/content_loader.py)

#### 需要掌握的关键词
- JSON
- CSV
- BeautifulSoup
- 数据抓取
- 数据清洗
- 字段标准化

#### 汇报时可以怎么说
- 当前项目中的专业和 FAQ 数据已经结构化保存在 JSON 中
- 未来我们计划用 BeautifulSoup 抓取官网页面
- 抓取后会把原始 HTML 解析成字段，再清洗成 JSON 或 CSV
- 清洗后的数据既能给页面使用，也能给 AI 助手使用

### 4.4 第 4 位同学：材料收集与内容整理

#### 主要负责内容
- 讲申请步骤内容如何被整理
- 讲结构化内容如何被模板展示出来
- 讲 Jinja2 如何把数据渲染到页面上

#### 建议重点文件
- [content/stages.json](/Users/wkai/Desktop/FlaskProject/content/stages.json)
- [content/guide_steps.json](/Users/wkai/Desktop/FlaskProject/content/guide_steps.json)
- [templates/guide_list.html](/Users/wkai/Desktop/FlaskProject/templates/guide_list.html)
- [templates/guide.html](/Users/wkai/Desktop/FlaskProject/templates/guide.html)
- [utils/content_loader.py](/Users/wkai/Desktop/FlaskProject/utils/content_loader.py)

#### 需要掌握的关键词
- Jinja2
- Flask
- DOM
- JSON
- for 循环渲染
- 模板变量

#### 汇报时可以怎么说
- 我们把申请阶段、步骤、材料清单等信息整理成结构化 JSON
- Flask 读取这些内容后传给模板
- 模板用 Jinja2 循环把它们渲染成页面
- 所以内容和页面展示逻辑是分开的

### 4.5 第 5 位同学：用户登录与交互

#### 主要负责内容
- 讲登录注册
- 讲评论功能
- 讲 Session 和 Cookie
- 讲前端 JS 如何和后端交互

#### 建议重点文件
- [templates/login_modal.html](/Users/wkai/Desktop/FlaskProject/templates/login_modal.html)
- [static/js/components/login_modal.js](/Users/wkai/Desktop/FlaskProject/static/js/components/login_modal.js)
- [static/js/guide.js](/Users/wkai/Desktop/FlaskProject/static/js/guide.js)
- [app.py](/Users/wkai/Desktop/FlaskProject/app.py)
- [tests/test_auth_session.py](/Users/wkai/Desktop/FlaskProject/tests/test_auth_session.py)

#### 需要掌握的关键词
- JavaScript
- Flask
- Session
- Cookie
- fetch
- 评论提交

#### 汇报时可以怎么说
- 用户登录成功后，后端会把用户信息保存到 Session
- 页面就能根据登录状态显示不同内容
- 评论通过表单提交到 Flask，再写入 Supabase
- 步骤完成状态通过 JS 调用接口，再局部更新页面内容

## 5. 你们具体应该怎么讲

建议采用“产品演示 + 技术解释”结合的方式。

### 演示顺序

1. 首页
2. 专业速查
3. 申请指南
4. FAQ
5. 登录与评论
6. AI 助手

这个顺序的好处是符合普通用户使用习惯，也容易自然过渡到技术说明。

### 每个人讲的时候尽量遵守这 4 句结构

每个人基本都可以按这 4 句话组织：

1. 我负责的功能是什么
2. 它解决了什么问题
3. 它对应项目中的哪些文件
4. 我在这个部分学到了什么技术

这样不容易讲乱，也不容易卡住。

## 6. 你们接下来怎么理解这个代码库

对于零基础团队，最推荐的顺序不是直接看所有代码，而是按“从外到内”的方式理解。

### 第一步：先把项目跑起来

每个人都要做到：
- 能本地启动项目
- 能点开首页、专业页、指南页、FAQ、助手页
- 知道每个页面大概在做什么

这一阶段的目标不是看懂代码，而是先建立整体印象。

### 第二步：先看路由，再看页面

推荐从 [app.py](/Users/wkai/Desktop/FlaskProject/app.py) 开始，只先看这些：
- `/`
- `/programs`
- `/guide`
- `/faq`
- `/assistant`
- `/auth/login`
- `/auth/register`

先搞明白：
- 哪个 URL 对应哪个函数
- 哪个函数渲染哪个模板
- 哪个函数处理表单和交互

### 第三步：看模板和静态资源

接着看：
- `templates/`
- `static/css/`
- `static/js/`

目标是搞清楚：
- 页面长什么样
- 样式从哪里来
- 搜索、弹窗、评论加载是谁控制的

### 第四步：再看数据文件

再去看：
- `content/stages.json`
- `content/guide_steps.json`
- `content/programs.json`
- `content/faq.json`

重点是理解：
- 这些字段为什么这样设计
- 它们怎么被页面使用

### 第五步：最后看 AI 和数据库

最后看：
- `utils/supabase_client.py`
- `utils/knowledge_base.py`
- `utils/rag_pipeline.py`
- `scripts/ingest_rag.py`

因为这一部分抽象稍微高一些，适合在前面几步建立信心后再看。

## 7. 推荐的 7 天理解计划

如果你们离汇报时间不远，可以按这个节奏。

### 第 1 天
- 所有人把项目跑起来
- 每个人把 5 个页面都点一遍

### 第 2 天
- 全组一起过一遍 `app.py`
- 只讲“页面入口和交互入口”

### 第 3 天
- 前端同学重点看 `templates/` 和 `static/`
- 内容同学重点看 `content/`
- 后端同学重点看 `utils/`

### 第 4 天
- 每个人整理自己负责的 3 到 5 个文件
- 写出自己负责部分的“能讲出口”的解释

### 第 5 天
- 开始做 PPT
- 每个人至少交 1 页自己负责的内容

### 第 6 天
- 全组彩排
- 调整谁先讲、谁后讲、谁负责演示

### 第 7 天
- 做最终精简
- 准备答辩问题

## 8. 汇报时常见问题怎么答

### 如果老师问：为什么不用更复杂的框架？

可以答：
这个项目是课程项目，目标是把 Flask、Jinja2、前后端交互、结构化数据和 AI 助手流程讲清楚，所以我们选择了更直观的技术组合。

### 如果老师问：BeautifulSoup 代码在哪里？

可以答：
目前项目已经完成了结构化展示、用户交互和 AI 助手，数据抓取是我们下一步的扩展方向。现在仓库中主要是已经清洗后的 JSON 数据。

### 如果老师问：AI 助手是不是完全可靠？

可以答：
不是完全依赖模型生成，而是先从知识库检索相关内容，再回答；如果向量检索不可用，还会回退到本地关键词检索，所以我们强调它是辅助工具，不替代官网信息。

## 9. 最后给你们的建议

你们现在最需要的，不是把每个技术点都学得很深，而是先做到三件事：
- 知道页面和功能是怎么串起来的
- 知道自己负责的文件在哪里
- 能用自己的话把它讲清楚

如果全组都能做到这一点，这次汇报就已经会很稳。

# Flask 申请助手（课程作业）

## 快速启动

```bash
cd /Users/wkai/Desktop/FlaskProject
.venv/bin/python app.py
```

访问：
- http://127.0.0.1:5000/
- http://127.0.0.1:5000/qa

## 功能
- 网申地图：首页阶段卡片
- 操作步骤：图文步骤页 + 材料清单 + 步骤评论
- 交流区：Q&A 列表/详情 + 评论
- 用户体验：右上角头像 Hover 菜单（Session）
- 状态记忆：最近浏览阶段（Cookie）
- 稳定性：404/500 错误页

## 目录结构

```text
FlaskProject/
├── app.py
├── requirements.txt
├── data/
│   └── app.db
├── docs/
│   ├── presentation_notes.md
│   └── team_split.md
├── scripts/
│   └── init_db.py
├── static/
│   ├── css/app.css
│   ├── js/qa.js
│   └── images/guides/*.svg
└── templates/
    ├── base.html
    ├── index.html
    ├── guide.html
    ├── qa_list.html
    ├── qa_detail.html
    └── errors/
        ├── 404.html
        └── 500.html
```

## 数据说明
- 示例流程数据：在 `app.py` 的 `STAGES` 与 `GUIDE_DATA`
- 示例问答数据：在 `app.py` 的 `QUESTIONS`
- 评论数据：SQLite（`data/app.db`）

# 基于 Vue 框架的电影推荐网页

本项目是一个基于 Vue 3 实现的电影推荐页面，仅包含前端内容，使用本地 JSON 文件作为数据源，界面简洁美观，适合学习和演示。

---

## 项目概览

- 框架：Vue 3
- 开发工具：Visual Studio Code
- 样式库：原生 CSS + [Funcss](https://funcss.liujueyi.cn/)（包含丰富组件和动画）
- 数据来源：[scrape.center](https://scrape.center/)，通过自定义爬虫 `request.py` 抓取
- 数据文件路径：`src/assets/movies.json`
- 项目特点：无需后端，使用静态 JSON 文件模拟数据库

---

## 快速开始

```bash
cd [your-project-folder]           # 进入项目目录
npm create vue@latest              # 创建 Vue 项目
npm install                        # 安装依赖
npm run dev                        # 启动开发服务器
```

## 目录结构
```
├── public/                    # 静态资源
├── src/
│   ├── assets/
│   │   └── movies.json        # 静态电影数据
│   ├── components/            # 通用组件（如 MovieList.vue）
│   ├── views/                 # 页面视图（如 Home.vue）
│   ├── App.vue                # 根组件
│   ├── main.js                # 应用入口
├── request.py                 # 爬虫脚本
├── result.png                 # 页面截图
└── README.md                  # 项目说明
```

## 页面说明
页面使用了 Funcss 提供的卡片样式（如 coin22），用于丰富展示效果，使界面更具动感和层次感，避免纯静态内容造成的视觉单调。

项目根目录下可查看 result.png 文件，获取页面实际展示效果。
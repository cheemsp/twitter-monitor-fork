# Twitter Monitor - Fork改造版

基于 BANKA2017/twitter-monitor 理念改造

## 🎯 改造目标

原项目：Twitter Crawler Core  
**改造后**：全自动化X热点监控站 + Discord推送

## ✨ 新增功能

| 功能 | 原项目 | 改造后 |
|------|--------|--------|
| 多类别监控 | ❌ | ✅ 6类别 |
| Discord推送 | ❌ | ✅ |
| 静态网站生成 | ❌ | ✅ |
| 服务器直跑 | ❌ | ✅ |
| GitHub Pages | ❌ | ✅ |
| 中文支持 | ❌ | ✅ |

## 🏗️ 架构

```
Fork自: BANKA2017/twitter-monitor (228⭐)
    ↓
改造:
  - 添加6类别搜索规则
  - 添加Discord webhook推送
  - 添加静态网站生成
  - 添加服务器定时任务
    ↓
输出: 网站 + Discord推送
```

## 📁 文件结构

```
.
├── README.md
├── config.py          # 配置（搜索规则、Discord webhook）
├── crawler.py         # 核心爬虫（基于bird）
├── discord_bot.py     # Discord推送模块
├── web_generator.py   # 网站生成器
├── run.sh             # 一键运行脚本
└── .github/
    └── workflows/
        └── deploy.yml # GitHub Actions备用
```

## 🚀 使用方法

### 方式1：服务器直跑（推荐）

```bash
# 1. 克隆仓库
git clone https://github.com/cheemsp/twitter-monitor-fork.git
cd twitter-monitor-fork

# 2. 配置环境变量
export X_AUTH_TOKEN="你的token"
export X_CT0="你的ct0"
export DISCORD_WEBHOOK="你的webhook"

# 3. 运行
bash run.sh
```

### 方式2：GitHub Actions

配置GitHub Secrets后自动运行。

## 📊 监控类别

1. 🌐 全球AI科技
2. 🇨🇳 中文AI圈
3. 🔥 中文万赞神贴
4. 🇯🇵 日区热门
5. 📊 技术干货
6. 🖼️ 带图热门

## 📝 改造说明

- **原项目**: 基础Twitter爬虫框架
- **改造点**: 
  - 增加分类搜索策略
  - 增加Discord推送
  - 增加网站可视化
  - 增加自动化部署

## 🔧 技术栈

- Python 3.11
- bird (Twitter/X CLI)
- Jinja2 (模板引擎)
- Discord Webhook
- GitHub Pages

## 📄 许可证

继承原项目许可证 (MIT)

## 🙏 致谢

- 原项目: [BANKA2017/twitter-monitor](https://github.com/BANKA2017/twitter-monitor)
- 改造: NAVI for Lain

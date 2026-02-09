#!/bin/bash
# Twitter Monitor Fork - 一键运行脚本
# 服务器直跑方案

set -e

echo "🚀 X-Monitor Fork | $(date '+%Y-%m-%d %H:%M:%S')"
echo "========================================"

# 检查环境变量
if [ -z "$X_AUTH_TOKEN" ] || [ -z "$X_CT0" ]; then
    echo "❌ 错误: 请设置 X_AUTH_TOKEN 和 X_CT0 环境变量"
    echo "例如: export X_AUTH_TOKEN='your_token'"
    exit 1
fi

# 安装依赖（如果需要）
if ! command -v bird &> /dev/null; then
    echo "📦 安装 bird..."
    npm install -g @steipete/bird
fi

# 运行主程序
echo "🔍 开始抓取..."
python3 main.py

# 推送到GitHub（如果配置了git）
if [ -d ".git" ]; then
    echo "📤 推送到GitHub..."
    git add docs/
    git commit -m "Auto update: $(date '+%Y-%m-%d %H:%M')" || echo "无变更"
    git push origin master || echo "推送失败或无需推送"
fi

echo "✅ 完成!"
echo "🏁 $(date '+%Y-%m-%d %H:%M:%S')"

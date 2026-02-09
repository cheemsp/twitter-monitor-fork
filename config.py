"""
配置文件
搜索规则、Discord webhook等
"""

import os

# X/Twitter 认证
X_AUTH_TOKEN = os.environ.get('X_AUTH_TOKEN', '')
X_CT0 = os.environ.get('X_CT0', '')

# Discord Webhook（可选）
DISCORD_WEBHOOK = os.environ.get('DISCORD_WEBHOOK', '')

# 搜索规则配置
SEARCH_RULES = {
    'global_ai': {
        'name': '🌐 全球AI科技',
        'query': '"AI" OR "ChatGPT" OR "Claude" OR "Gemini" OR "OpenAI" lang:en min_faves:3000 within_time:12h -is:retweet',
        'limit': 10,
        'enabled': True
    },
    'cn_ai': {
        'name': '🇨🇳 中文AI圈',
        'query': '"AI" OR "人工智能" OR "大模型" OR "ChatGPT" OR "提示词" lang:zh-cn min_faves:300 within_time:12h -is:retweet',
        'limit': 10,
        'enabled': True
    },
    'cn_viral': {
        'name': '🔥 中文万赞神贴',
        'query': 'lang:zh-cn min_faves:10000 -is:retweet within_time:24h',
        'limit': 5,
        'enabled': True
    },
    'jp_trending': {
        'name': '🇯🇵 日区热门',
        'query': 'lang:ja min_faves:500 within_time:4h -is:retweet',
        'limit': 8,
        'enabled': True
    },
    'tech_insights': {
        'name': '📊 技术干货',
        'query': 'lang:en min_faves:5000 filter:links within_time:12h -is:retweet',
        'limit': 8,
        'enabled': True
    },
    'visual': {
        'name': '🖼️ 带图热门',
        'query': 'filter:images lang:zh-cn min_faves:500 within_time:12h -is:retweet',
        'limit': 6,
        'enabled': True
    }
}

# 输出配置
OUTPUT_DIR = 'docs'
MAX_CONTENT_LENGTH = 300  # 推文内容最大长度

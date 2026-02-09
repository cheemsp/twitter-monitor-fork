#!/usr/bin/env python3
"""
Twitter Monitor Fork - 主程序
整合爬虫、Discord推送、网站生成
"""

import os
from crawler import TwitterCrawler
from discord_bot import DiscordPusher
from web_generator import WebGenerator
from config import SEARCH_RULES, DISCORD_WEBHOOK

def main():
    print("🚀 Twitter Monitor Fork 启动...")
    print("=" * 50)
    
    # 初始化组件
    crawler = TwitterCrawler(
        os.environ.get('X_AUTH_TOKEN'),
        os.environ.get('X_CT0')
    )
    
    discord = DiscordPusher(DISCORD_WEBHOOK)
    web_gen = WebGenerator()
    
    # 抓取所有类别
    all_data = {}
    for key, config in SEARCH_RULES.items():
        if not config['enabled']:
            continue
            
        print(f"\n🔍 {config['name']}")
        tweets = crawler.search(config['query'], config['limit'])
        all_data[key] = tweets
        print(f"   找到 {len(tweets)} 条推文")
        
        # Discord推送
        if DISCORD_WEBHOOK:
            discord.send_tweets(config['name'], tweets)
    
    # 生成网站
    print("\n🌐 生成网站...")
    web_gen.generate(all_data, SEARCH_RULES)
    
    print("\n✅ 全部完成!")

if __name__ == '__main__':
    main()

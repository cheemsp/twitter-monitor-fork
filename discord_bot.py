#!/usr/bin/env python3
"""
Discord推送模块
"""

import requests
import json
from datetime import datetime

class DiscordPusher:
    """Discord推送类"""
    
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url
    
    def send_message(self, content, embeds=None):
        """发送消息"""
        if not self.webhook_url:
            print("⚠️ 未配置Discord Webhook")
            return False
        
        payload = {
            'content': content,
            'username': 'X-Monitor'
        }
        
        if embeds:
            payload['embeds'] = embeds
        
        try:
            response = requests.post(
                self.webhook_url,
                json=payload,
                timeout=30
            )
            return response.status_code == 204
        except Exception as e:
            print(f"Discord推送失败: {e}")
            return False
    
    def send_tweets(self, category_name, tweets):
        """发送推文列表"""
        if not tweets:
            return
        
        # 生成消息
        content = f"**{category_name}** | {datetime.now().strftime('%m-%d %H:%M')}\n"
        content += "=" * 40 + "\n\n"
        
        for i, tweet in enumerate(tweets[:5], 1):
            user = tweet.get('user', '')
            text = tweet.get('content', '')[:150]
            if len(tweet.get('content', '')) > 150:
                text += '...'
            url = tweet.get('url', '')
            
            content += f"{i}. {user}\n{text}\n"
            if url:
                content += f"🔗 {url}\n"
            content += "\n"
        
        self.send_message(content)

if __name__ == '__main__':
    # 测试
    import os
    pusher = DiscordPusher(os.environ.get('DISCORD_WEBHOOK', ''))
    pusher.send_message("🤖 X-Monitor 测试消息")

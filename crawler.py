#!/usr/bin/env python3
"""
Twitter Monitor - Fork改造版
核心爬虫模块（基于bird CLI）
"""

import subprocess
import json
import os
from datetime import datetime
from pathlib import Path

class TwitterCrawler:
    """Twitter爬虫类"""
    
    def __init__(self, auth_token, ct0):
        self.auth_token = auth_token
        self.ct0 = ct0
        
    def search(self, query, limit=10):
        """搜索推文"""
        cmd = [
            'bird', 'search', query,
            '-n', str(limit),
            '--auth-token', self.auth_token,
            '--ct0', self.ct0,
            '--plain'
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            if result.returncode == 0:
                return self._parse_tweets(result.stdout)
        except Exception as e:
            print(f"搜索错误: {e}")
        return []
    
    def _parse_tweets(self, output):
        """解析推文"""
        tweets = []
        current = {}
        
        for line in output.split('\n'):
            line = line.strip()
            if line.startswith('@'):
                if current:
                    tweets.append(current)
                current = {'user': line, 'content': '', 'date': '', 'url': ''}
            elif line.startswith('date:'):
                current['date'] = line.replace('date:', '').strip()
            elif line.startswith('url:'):
                current['url'] = line.replace('url:', '').strip()
            elif line and not line.startswith('─') and not line.startswith('PHOTO'):
                current['content'] += line + ' '
        
        if current:
            tweets.append(current)
        
        return tweets

if __name__ == '__main__':
    # 测试
    crawler = TwitterCrawler(
        os.environ.get('X_AUTH_TOKEN'),
        os.environ.get('X_CT0')
    )
    
    tweets = crawler.search('"AI" OR "ChatGPT" lang:en min_faves:1000 within_time:6h', 5)
    print(f"找到 {len(tweets)} 条推文")

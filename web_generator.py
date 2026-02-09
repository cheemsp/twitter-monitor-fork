#!/usr/bin/env python3
"""
网站生成器
生成静态HTML页面
"""

import json
from datetime import datetime
from pathlib import Path

def generate_html(data, category_config, output_dir='docs'):
    """生成HTML"""
    date_str = datetime.now().strftime('%Y-%m-%d %H:%M')
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 生成导航
    nav_links = ''
    for key, config in category_config.items():
        nav_links += f'<a href="#{key}" class="nav-link">{config["name"].split()[0]}</a>\n'
    
    # 生成分类内容
    categories = ''
    for key, config in category_config.items():
        tweets = data.get(key, [])
        categories += generate_category(key, config['name'], tweets)
    
    # 构建HTML
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>X-Monitor | Twitter热点监控</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', sans-serif;
            background: #0f0f23;
            color: #e0e0e0;
            line-height: 1.6;
        }}
        .header {{
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            padding: 2rem 1rem;
            text-align: center;
            border-bottom: 1px solid #2a2a4a;
        }}
        .header h1 {{
            font-size: 1.8rem;
            background: linear-gradient(90deg, #00d4ff, #7b2cbf);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .header .meta {{ color: #888; font-size: 0.9rem; margin-top: 0.5rem; }}
        .container {{ max-width: 900px; margin: 0 auto; padding: 1rem; }}
        .category {{
            margin-bottom: 2rem;
            background: #1a1a2e;
            border-radius: 12px;
            overflow: hidden;
            border: 1px solid #2a2a4a;
        }}
        .category-header {{
            background: linear-gradient(90deg, #2a2a4a 0%, #1a1a2e 100%);
            padding: 1rem 1.5rem;
            font-size: 1.1rem;
            font-weight: 600;
            border-bottom: 1px solid #2a2a4a;
        }}
        .tweet {{
            padding: 1rem 1.5rem;
            border-bottom: 1px solid #2a2a4a;
            transition: background 0.2s;
        }}
        .tweet:hover {{ background: #252542; }}
        .tweet:last-child {{ border-bottom: none; }}
        .tweet-user {{ color: #00d4ff; font-weight: 600; font-size: 0.9rem; margin-bottom: 0.3rem; }}
        .tweet-content {{ color: #e0e0e0; font-size: 0.95rem; margin-bottom: 0.5rem; line-height: 1.5; }}
        .tweet-meta {{ display: flex; justify-content: space-between; font-size: 0.8rem; color: #888; }}
        .tweet-link {{ color: #7b2cbf; text-decoration: none; }}
        .tweet-link:hover {{ text-decoration: underline; }}
        .empty {{ padding: 2rem; text-align: center; color: #666; }}
        .nav {{ position: sticky; top: 0; background: rgba(15, 15, 35, 0.95); backdrop-filter: blur(10px); padding: 1rem; border-bottom: 1px solid #2a2a4a; z-index: 100; }}
        .nav-links {{ display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }}
        .nav-link {{ color: #888; text-decoration: none; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.85rem; transition: all 0.2s; }}
        .nav-link:hover, .nav-link.active {{ color: #00d4ff; background: #2a2a4a; }}
        footer {{ text-align: center; padding: 2rem; color: #666; font-size: 0.85rem; }}
        @media (max-width: 600px) {{
            .header h1 {{ font-size: 1.4rem; }}
            .container {{ padding: 0.5rem; }}
            .tweet {{ padding: 0.8rem 1rem; }}
        }}
    </style>
</head>
<body>
    <header class="header">
        <h1>🤖 X-Monitor</h1>
        <div class="meta">Twitter热点监控 | {date_str} 更新</div>
    </header>
    <nav class="nav">
        <div class="nav-links">
            {nav_links}
        </div>
    </nav>
    <main class="container">
        {categories}
    </main>
    <footer>
        <p>X-Monitor Fork改造版 | 基于 BANKA2017/twitter-monitor</p>
        <p style="margin-top: 0.5rem;">🤖 by NAVI</p>
    </footer>
</body>
</html>'''
    
    # 保存
    output_file = output_dir / 'index.html'
    output_file.write_text(html, encoding='utf-8')
    print(f"✅ 网站已生成: {output_file}")
    
    # 同时保存JSON数据
    data_file = output_dir / 'data.json'
    data_file.write_text(json.dumps({
        'updated_at': datetime.now().isoformat(),
        'data': data
    }, ensure_ascii=False, indent=2), encoding='utf-8')

def generate_category(key, name, tweets):
    """生成单个分类"""
    html = f'<section class="category" id="{key}">\n'
    html += f'<div class="category-header">{name}</div>\n'
    
    if tweets:
        for tweet in tweets:
            content = tweet.get('content', '')[:300]
            if len(tweet.get('content', '')) > 300:
                content += '...'
            
            html += '<div class="tweet">\n'
            html += f'<div class="tweet-user">{tweet.get("user", "")}</div>\n'
            html += f'<div class="tweet-content">{content}</div>\n'
            html += '<div class="tweet-meta">\n'
            html += f'<span>{tweet.get("date", "")}</span>\n'
            if tweet.get('url'):
                html += f'<a href="{tweet["url"]}" target="_blank" class="tweet-link">查看原文 →</a>\n'
            html += '</div>\n'
            html += '</div>\n'
    else:
        html += '<div class="empty">暂无数据</div>\n'
    
    html += '</section>\n'
    return html

if __name__ == '__main__':
    # 测试
    generate_html(
        {'test': [{'user': '@test', 'content': 'Test content', 'date': 'now', 'url': 'https://x.com/test'}]},
        {'test': {'name': 'Test Category'}},
        'docs'
    )

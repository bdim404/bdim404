import json
import urllib.request
import re
import sys

PLUGINS = [
    'bdim/abstracts-index',
    'bdim/steam',
    'bdim/tianyancha',
    'bdim/zhipuai_web_search'
]

def fetch_install_count(plugin_id):
    url = f'https://marketplace.dify.ai/api/v1/plugins/{plugin_id}'
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
        return data['data']['plugin']['install_count']

def main():
    total = sum(fetch_install_count(p) for p in PLUGINS)

    with open('README.md', 'r') as f:
        content = f.read()

    logo_svg = 'PHN2ZyB3aWR0aD0iNTAiIGhlaWdodD0iMjYiIHZpZXdCb3g9IjAgMCA1MCAyNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNNi42MTc4NCAyLjA2NEM4LjM3Nzg0IDIuMDY0IDkuOTIxODQgMi40MDggMTEuMjQ5OCAzLjA5NkMxMi41OTM4IDMuNzg0IDEzLjYyNTggNC43NjggMTQuMzQ1OCA2LjA0OEMxNS4wODE4IDcuMzEyIDE1LjQ0OTggOC43ODQgMTUuNDQ5OCAxMC40NjRDMTUuNDQ5OCAxMi4xNDQgMTUuMDgxOCAxMy42MTYgMTQuMzQ1OCAxNC44OEMxMy42MjU4IDE2LjEyOCAxMi41OTM4IDE3LjA5NiAxMS4yNDk4IDE3Ljc4NEM5LjkyMTg0IDE4LjQ3MiA4LjM3Nzg0IDE4LjgxNiA2LjYxNzg0IDE4LjgxNkgwLjc2MTg0MVYyLjA2NEg2LjYxNzg0Wk02LjQ5Nzg0IDE1Ljk2QzguMjU3ODQgMTUuOTYgOS42MTc4NCAxNS40OCAxMC41Nzc4IDE0LjUyQzExLjUzNzggMTMuNTYgMTIuMDE3OCAxMi4yMDggMTIuMDE3OCAxMC40NjRDMTIuMDE3OCA4LjcyIDExLjUzNzggNy4zNiAxMC41Nzc4IDYuMzg0QzkuNjE3ODQgNS4zOTIgOC4yNTc4NCA0Ljg5NiA2LjQ5Nzg0IDQuODk2SDQuMTIxODRWMTUuOTZINi40OTc4NFoiIGZpbGw9IndoaXRlIi8+PHBhdGggZD0iTTIwLjg2OSAzLjkzNkMyMC4yNzcgMy45MzYgMTkuNzgxIDMuNzUyIDE5LjM4MSAzLjM4NEMxOC45OTcgMyAxOC44MDUgMi41MjggMTguODA1IDEuOTY4QzE4LjgwNSAxLjQwOCAxOC45OTcgMC45NDQgMTkuMzgxIDAuNTc2QzE5Ljc4MSAwLjE5MiAyMC4yNzcgMCAyMC44NjkgMEMyMS40NjEgMCAyMS45NDkgMC4xOTIgMjIuMzMzIDAuNTc2QzIyLjczMyAwLjk0NCAyMi45MzMgMS40MDggMjIuOTMzIDEuOTY4QzIyLjkzMyAyLjUyOCAyMi43MzMgMyAyMi4zMzMgMy4zODRDMjEuOTQ5IDMuNzUyIDIxLjQ2MSAzLjkzNiAyMC44NjkgMy45MzZaTTIyLjUyNSA1LjUyVjE4LjgxNkgxOS4xNjVWNS41MkgyMi41MjVaIiBmaWxsPSJ3aGl0ZSIvPjxwYXRoIGQ9Ik0zMy4xNDA3IDguMjhIMzAuODEyN1YxOC44MTZIMjcuNDA0N1Y4LjI4SDI1Ljg5MjdWNS41MkgyNy40MDQ3VjQuODQ4QzI3LjQwNDcgMy4yMTYgMjcuODY4NyAyLjAxNiAyOC43OTY3IDEuMjQ4QzI5LjcyNDcgMC40OCAzMS4xMjQ3IDAuMTIgMzIuOTk2NyAwLjE2ODAwMVYzQzMyLjE4MDcgMi45ODQgMzEuNjEyNyAzLjEyIDMxLjI5MjcgMy40MDhDMzAuOTcyNyAzLjY5NiAzMC44MTI3IDQuMjE2IDMwLjgxMjcgNC45NjhWNS41MkgzMy4xNDA3VjguMjhaIiBmaWxsPSJ3aGl0ZSIvPjxwYXRoIGQ9Ik00OS4yMzgxIDUuNTJMNDEuMDA2MSAyNS4xMDRIMzcuNDMwMUw0MC4zMTAxIDE4LjQ4TDM0Ljk4MjEgNS41MkgzOC43NTAxTDQyLjE4MjEgMTQuODA4TDQ1LjY2MjEgNS41Mkg0OS4yMzgxWiIgZmlsbD0id2hpdGUiLz48L3N2Zz4='
    badge_url = f'https://img.shields.io/badge/Total_Downloads-{total}-0033ff?style=for-the-badge&logo=data:image/svg+xml;base64,{logo_svg}'
    badge_html = f'<a href="https://marketplace.dify.ai/plugins?author=bdim"><img src="{badge_url}" alt="Total Downloads" /></a>'

    pattern = r'<a href="https://marketplace\.dify\.ai/plugins\?author=bdim"><img src="https://img\.shields\.io/badge/Total_Downloads-\d+-[^"]*" alt="Total Downloads" /></a>'

    if re.search(pattern, content):
        new_content = re.sub(pattern, badge_html, content)
    else:
        marketplace_pattern = r'(### 🚀 Dify Plugin Developer\n\n)'
        new_content = re.sub(
            marketplace_pattern,
            r'\1' + badge_html + '\n\n',
            content
        )

    if new_content != content:
        with open('README.md', 'w') as f:
            f.write(new_content)
        print(f'Updated README.md with total downloads: {total}')
    else:
        print(f'No changes needed. Total downloads: {total}')

if __name__ == '__main__':
    main()

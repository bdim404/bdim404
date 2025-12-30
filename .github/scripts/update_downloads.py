import json
import urllib.request
import re
import sys

PLUGINS = [
    'bdim/abstracts-index',
    'bdim/steam',
    'bdim/tianyancha'
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

    logo_svg = 'PHN2ZyB3aWR0aD0iNjQiIGhlaWdodD0iNjQiIHZpZXdCb3g9IjAgMCA2NCA2NCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48Y2lyY2xlIGN4PSIzMiIgY3k9IjMyIiByPSIzMiIgZmlsbD0idXJsKCNnMSkiLz48cGF0aCBkPSJNMzIgMTZWNDhNMjQgMjRIMzJNMjQgNDBIMzIiIHN0cm9rZT0id2hpdGUiIHN0cm9rZS13aWR0aD0iNCIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIi8+PGRlZnM+PGxpbmVhckdyYWRpZW50IGlkPSJnMSIgeDE9IjMyIiB5MT0iMCIgeDI9IjMyIiB5Mj0iNjQiPjxzdG9wIG9mZnNldD0iMCIgc3RvcC1jb2xvcj0iIzAwNjBGRiIvPjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iIzAwMzNGRiIvPjwvbGluZWFyR3JhZGllbnQ+PC9kZWZzPjwvc3ZnPg=='
    badge_url = f'https://img.shields.io/badge/Dify_Plugin-{total}_downloads-0033ff?style=for-the-badge&logo=data:image/svg+xml;base64,{logo_svg}&logoColor=white'
    badge_html = f'<img src="{badge_url}" alt="Dify Plugin Downloads" />'

    pattern = r'<img src="https://img\.shields\.io/badge/Dify_Plugin-\d+_downloads-[^"]*" alt="Dify Plugin Downloads" />'

    if re.search(pattern, content):
        new_content = re.sub(pattern, badge_html, content)
    else:
        komarev_pattern = r'(<img src="https://komarev\.com/ghpvc/\?username=bdim404&abbreviated=true" alt="Profile Views" />)'
        new_content = re.sub(
            komarev_pattern,
            r'\1 ' + badge_html,
            content
        )

    if new_content != content:
        with open('README.md', 'w') as f:
            f.write(new_content)
        print(f'Updated README.md with total downloads: {total}')
        sys.exit(0)
    else:
        print(f'No changes needed. Total downloads: {total}')
        sys.exit(1)

if __name__ == '__main__':
    main()

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

    logo_svg = 'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdCb3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTYgMzJDMjQuODM2NiAzMiAzMiAyNC44MzY2IDMyIDE2QzMyIDcuMTYzNDQgMjQuODM2NiAwIDE2IDBDNy4xNjM0NCAwIDAgNy4xNjM0NCAwIDE2QzAgMjQuODM2NiA3LjE2MzQ0IDMyIDE2IDMyWiIgZmlsbD0idXJsKCNwYWludDBfbGluZWFyKSIvPjxkZWZzPjxsaW5lYXJHcmFkaWVudCBpZD0icGFpbnQwX2xpbmVhciIgeDE9IjE2IiB5MT0iMCIgeDI9IjE2IiB5Mj0iMzIiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBzdG9wLWNvbG9yPSIjMDA2MEZGIi8+PHN0b3Agb2Zmc2V0PSIxIiBzdG9wLWNvbG9yPSIjMDAzM0ZGIi8+PC9saW5lYXJHcmFkaWVudD48L2RlZnM+PC9zdmc+'
    badge_url = f'https://img.shields.io/badge/dify_plugin-{total}-0033ff?style=flat&logo={logo_svg}&logoColor=white'
    badge_html = f'<img src="{badge_url}" alt="Dify Plugin Downloads" />'

    pattern = r'<img src="https://img\.shields\.io/badge/dify_plugin-\d+-[^"]*" alt="Dify Plugin Downloads" />'

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

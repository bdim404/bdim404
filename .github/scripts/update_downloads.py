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

    badge_url = f'https://img.shields.io/badge/dify_downloads-{total}-blue'
    badge_html = f'<img src="{badge_url}" alt="Dify Downloads" />'

    pattern = r'<img src="https://img\.shields\.io/badge/dify_downloads-\d+-blue" alt="Dify Downloads" />'

    if re.search(pattern, content):
        new_content = re.sub(pattern, badge_html, content)
    else:
        komarev_line = '<img src="https://komarev.com/ghpvc/?username=bdim404&abbreviated=true" alt="Profile Views" />'
        new_content = content.replace(
            komarev_line,
            f'{komarev_line}\n{badge_html}'
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

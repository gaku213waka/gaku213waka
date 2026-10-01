"""Generate a pink isometric SVG from GitHub's actual contribution calendar."""
import argparse
import json
import math
import os
from pathlib import Path
import urllib.request
from html import escape


def fetch_calendar(username):
    query = '''query($login: String!) { user(login: $login) { contributionsCollection { contributionCalendar { totalContributions weeks { contributionDays { date contributionCount } } } } } }'''
    request = urllib.request.Request(
        'https://api.github.com/graphql',
        data=json.dumps({'query': query, 'variables': {'login': username}}).encode(),
        headers={'Authorization': 'Bearer ' + os.environ['GITHUB_TOKEN'],
                 'Content-Type': 'application/json', 'User-Agent': 'profile-skyline'})
    with urllib.request.urlopen(request, timeout=60) as response:
        data = json.load(response)
    if data.get('errors') or not data.get('data', {}).get('user'):
        raise RuntimeError('GitHub contribution calendar request failed')
    return data['data']['user']['contributionsCollection']['contributionCalendar']


def render(calendar):
    weeks = calendar['weeks']
    maximum = max((d['contributionCount'] for w in weeks for d in w['contributionDays']), default=0)
    colors = ['#161b22', '#611332', '#a51c4d', '#ff006e', '#ff4d9d']
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="360" viewBox="0 0 1000 360">',
             '<rect width="1000" height="360" rx="18" fill="#0d1117"/>',
             '<text x="35" y="37" fill="#ff4d9d" font-size="17" font-family="monospace">CONTRIBUTION SKYLINE</text>',
             f'<text x="35" y="61" fill="#c9d1d9" font-size="13" font-family="monospace">{calendar["totalContributions"]} contributions in the calendar returned by GitHub</text>']
    for wi, week in enumerate(weeks):
        for day in week['contributionDays']:
            from datetime import date
            di = (date.fromisoformat(day['date']).weekday() + 1) % 7
            count = day['contributionCount']
            x, y = 110 + wi * 15 - di * 11, 110 + wi * 2.4 + di * 12
            height = 2 if not count else 8 + 58 * math.log1p(count) / math.log1p(maximum)
            color = colors[0 if not count else min(4, 1 + int(3 * count / max(maximum, 1)))]
            pts = lambda coords: ' '.join(f'{a:.1f},{b:.1f}' for a,b in coords)
            parts.append(f'<g><title>{escape(day["date"])}: {count} contributions</title>')
            # Side faces then top; chronological painter order prevents overlap artifacts.
            parts.append(f'<polygon points="{pts([(x,y-height),(x+13,y+3-height),(x+13,y+3),(x,y)])}" fill="{color}" opacity=".55"/>')
            parts.append(f'<polygon points="{pts([(x+13,y+3-height),(x+3,y+11-height),(x+3,y+11),(x+13,y+3)])}" fill="{color}" opacity=".8"/>')
            parts.append(f'<polygon points="{pts([(x,y-height),(x+13,y+3-height),(x+3,y+11-height),(x-10,y+8-height)])}" fill="{color}"/>')
            parts.append('</g>')
    parts.append('<path d="M35 319H965" stroke="#ff006e" stroke-opacity=".35"/><circle cx="40" cy="341" r="3" fill="#ff4d9d"><animate attributeName="opacity" values="1;.25;1" dur="3s" repeatCount="indefinite"/></circle><text x="54" y="345" fill="#999" font-size="12" font-family="monospace">REAL ACTIVITY / DAILY UPDATE / HEIGHT = LOG-SCALED CONTRIBUTIONS</text></svg>')
    return ''.join(parts)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', required=True)
    parser.add_argument('--output', default='assets/generated/profile-3d.svg')
    parser.add_argument('--calendar-json', help='Offline fixture for validation')
    args = parser.parse_args()
    calendar = json.loads(Path(args.calendar_json).read_text()) if args.calendar_json else fetch_calendar(args.username)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render(calendar), encoding='utf-8')

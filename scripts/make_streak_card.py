import json, os

def generate_streak_card():
    json_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'contributions.json')
    out_svg = os.path.join(os.path.dirname(__file__), '..', 'streak-card.svg')

    with open(json_path, 'r') as f:
        data = json.load(f)

    total = data.get('total_contributions', 0)
    current_streak = data.get('current_streak', {}).get('length', 0)
    longest_streak = data.get('longest_streak', {}).get('length', 0)
    start_date = data.get('range', {}).get('start', '2025-08-03')
    end_date = data.get('range', {}).get('end', '2026-08-03')

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 170" width="860" height="170" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
  <!-- © 2026 Bandi Arunkumar (https://github.com/bandiarunkumar). All Rights Reserved. -->
  <defs>
    <linearGradient id="stbg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0d1117"/>
      <stop offset="100%" stop-color="#161b22"/>
    </linearGradient>
    <filter id="stglow">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <rect width="860" height="170" rx="14" fill="url(#stbg)"/>
  <rect x="0.5" y="0.5" width="859" height="169" rx="14" fill="none" stroke="#30363d" stroke-width="1"/>

  <!-- Column 1: Total Contributions -->
  <g transform="translate(140, 85)">
    <text x="0" y="-25" fill="#58a6ff" font-size="28" font-weight="800" text-anchor="middle" filter="url(#stglow)">{total:,}</text>
    <text x="0" y="5" fill="#e6edf3" font-size="12" font-weight="700" text-anchor="middle">Total Contributions</text>
    <text x="0" y="24" fill="#7d8590" font-size="10" text-anchor="middle">{start_date} - Present</text>
  </g>

  <!-- Divider 1 -->
  <line x1="280" y1="35" x2="280" y2="135" stroke="#30363d" stroke-width="1"/>

  <!-- Column 2: Current Streak -->
  <g transform="translate(430, 85)">
    <text x="0" y="-25" fill="#39d353" font-size="34" font-weight="900" text-anchor="middle" filter="url(#stglow)">🔥 {current_streak}</text>
    <text x="0" y="5" fill="#e6edf3" font-size="12" font-weight="700" text-anchor="middle">Current Streak (Days)</text>
    <text x="0" y="24" fill="#39d353" font-size="10" font-weight="700" text-anchor="middle">Active Streak 🟢</text>
  </g>

  <!-- Divider 2 -->
  <line x1="580" y1="35" x2="580" y2="135" stroke="#30363d" stroke-width="1"/>

  <!-- Column 3: Longest Streak -->
  <g transform="translate(720, 85)">
    <text x="0" y="-25" fill="#ffa657" font-size="28" font-weight="800" text-anchor="middle" filter="url(#stglow)">⚡ {longest_streak}</text>
    <text x="0" y="5" fill="#e6edf3" font-size="12" font-weight="700" text-anchor="middle">Longest Streak (Days)</text>
    <text x="0" y="24" fill="#7d8590" font-size="10" text-anchor="middle">All-Time Record</text>
  </g>
</svg>'''

    with open(out_svg, 'w') as f:
        f.write(svg_content)
    print("Generated streak-card.svg successfully!")

if __name__ == '__main__':
    generate_streak_card()

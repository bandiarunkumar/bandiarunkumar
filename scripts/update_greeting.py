#!/usr/bin/env python3
"""
Updates the greeting line in README.md based on current IST time.
Run by .github/workflows/update-profile-art.yml daily.
"""
import datetime
import re
import os

HERE = os.path.dirname(__file__)
README = os.path.join(HERE, "..", "README.md")

ist = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
now = datetime.datetime.now(ist)
hour = now.hour

if 5 <= hour < 12:
    greeting = "Good Morning ☀️"
elif 12 <= hour < 17:
    greeting = "Good Afternoon 🌤️"
elif 17 <= hour < 21:
    greeting = "Good Evening 🌆"
else:
    greeting = "Good Night 🌙"

line = f"<!-- GREETING -->{greeting}, I'm **Bandia Arunkumar**! Welcome to my profile.<!-- /GREETING -->"

with open(README, "r") as f:
    content = f.read()

updated = re.sub(
    r"<!-- GREETING -->.*?<!-- /GREETING -->",
    line,
    content,
    flags=re.DOTALL
)

with open(README, "w") as f:
    f.write(updated)

print(f"Greeting updated to: {greeting}")

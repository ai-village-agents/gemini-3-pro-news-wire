import re
import sys

# Read HTML from standard input or file
try:
    with open('sec_6k_latest.html', 'r') as f:
        content = f.read()
except FileNotFoundError:
    sys.exit(0)

# Regex to find links to text filings
# Looking for pattern: <a href="/Archives/edgar/data/..." ...>[text]</a>
# The SEC listing usually has [html][text] links. We want the text one.
# Format: <a href="/Archives/edgar/data/1996230/000199623024000003/0001996230-24-000003.txt">[text]</a>

links = re.findall(r'href="(/Archives/edgar/data/[0-9]+/[0-9]+/[0-9-]+\.txt)"', content)

# Write unique links to found_links.txt
unique_links = sorted(list(set(links)))

with open('found_links.txt', 'w') as f:
    for link in unique_links:
        f.write(f"https://www.sec.gov{link}\n")

print(f"Found {len(unique_links)} filings.")

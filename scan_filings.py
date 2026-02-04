import requests
import re
import time
import sys

try:
    with open('found_links.txt', 'r') as f:
        links = f.read().splitlines()
except FileNotFoundError:
    print("No found_links.txt")
    sys.exit(0)

print(f"Scanning {len(links)} filings...")

headers = {
    "User-Agent": "Mozilla/5.0 (AgentVillage/1.0; mailto:gemini-3-pro@agentvillage.org)"
}

for url in links:
    try:
        # Rate limit
        time.sleep(0.15)
        
        response = requests.get(url, headers=headers, timeout=10)
        content = response.text
        
        # Extract Company Name
        name_match = re.search(r'COMPANY CONFORMED NAME:\s*(.*)', content)
        company = name_match.group(1).strip() if name_match else "Unknown"
        
        # Extract Items
        # Pattern: "Item X.XX" at start of line or after newline
        items = re.findall(r'Item\s+([0-9]\.[0-9]{2})', content)
        unique_items = sorted(list(set(items)))
        
        priority_items = [i for i in unique_items if i in ['1.01', '1.02', '2.01', '5.02', '8.01']]
        
        if priority_items:
            print(f"MATCH: [{company}] {unique_items} - {url}")
            
    except Exception as e:
        print(f"Error fetching {url}: {e}")


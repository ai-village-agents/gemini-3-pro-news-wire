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
    "User-Agent": "AgentVillage gemini-3-pro@agentvillage.org"
}

for url in links:
    try:
        # Rate limit
        time.sleep(0.2)
        
        response = requests.get(url, headers=headers, timeout=10)
        content = response.text
        
        # Extract Company Name
        name_match = re.search(r'COMPANY CONFORMED NAME:\s*(.*)', content)
        company = name_match.group(1).strip() if name_match else "Unknown"
        
        # Look for offering amount near the "Proposed Maximum Aggregate Offering Price" label
        price_pattern = re.compile(
            r'Proposed\s+Maximum\s+Aggregate\s+Offering\s+Price[^$\d]{0,100}\$?\s*([0-9][0-9,]*\.?[0-9]*)',
            re.IGNORECASE | re.DOTALL
        )
        phrase_pattern = re.compile(r'Proposed\s+Maximum\s+Aggregate\s+Offering\s+Price', re.IGNORECASE)

        price_match = price_pattern.search(content)

        if price_match:
            amount = price_match.group(1).strip()
            print(f"MATCH: [{company}] [{amount}] - {url}")
        elif phrase_pattern.search(content):
            print(f"MATCH: [{company}] [S-1 Filings] - {url}")
            
    except Exception as e:
        print(f"Error fetching {url}: {e}")

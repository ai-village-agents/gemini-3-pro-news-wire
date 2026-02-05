import requests
import re
import time
import sys

try:
    with open('found_links_6k.txt', 'r') as f:
        links = f.read().splitlines()
except FileNotFoundError:
    print("No found_links_6k.txt")
    sys.exit(0)

print(f"Scanning {len(links)} 6-K filings...")

headers = {
    "User-Agent": "AgentVillage gemini-3-pro@agentvillage.org"
}

keywords = [
    "Press Release", "News Release", "Earnings", "Financial Results", 
    "Acquisition", "Merger", "Dividend", "Resignation", "Appointment", 
    "Departure", "Strategic", "Agreement", "Offering", "Private Placement"
]

for url in links:
    try:
        # Rate limit
        time.sleep(0.2)
        
        response = requests.get(url, headers=headers, timeout=10)
        content = response.text
        
        # Extract Company Name
        name_match = re.search(r'COMPANY CONFORMED NAME:\s*(.*)', content)
        company = name_match.group(1).strip() if name_match else "Unknown"
        
        # Search for keywords in the document body (approximate)
        # We'll take the first 10k chars or so to avoid huge processing
        # actually 6-Ks are often just a cover page + exhibit. 
        # We want to see if the keywords appear.
        
        found_keywords = []
        for kw in keywords:
            if re.search(r'\b' + re.escape(kw) + r'\b', content, re.IGNORECASE):
                found_keywords.append(kw)
        
        if found_keywords:
            print(f"MATCH: [{company}] {found_keywords} - {url}")
            
    except Exception as e:
        print(f"Error fetching {url}: {e}")

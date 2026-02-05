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

print(f"Scanning {len(links)} 6-K filings for keywords...")

headers = {
    "User-Agent": "AgentVillage gemini-3-pro@agentvillage.org"
}

keywords = [
    "Press Release", "News Release", "Financial Results", "Earnings", 
    "Dividend", "Acquisition", "Merger", "Resignation", "Appointment",
    "Capital Raise", "Private Placement", "Offering"
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
        
        # Check for keywords (case insensitive)
        found_keywords = []
        lower_content = content.lower()
        
        # Simple heuristic: scan first 5000 chars for keywords to avoid noise in huge exhibits?
        # Or scan whole file? Let's scan headers/description first.
        # Actually 6-K text files often have the full SGML header then the document.
        
        for kw in keywords:
            if kw.lower() in lower_content:
                found_keywords.append(kw)
        
        if found_keywords:
            print(f"MATCH: [{company}] {found_keywords} - {url}")
            
    except Exception as e:
        print(f"Error fetching {url}: {e}")

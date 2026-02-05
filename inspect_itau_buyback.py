import requests
import re

url = "https://www.sec.gov/Archives/edgar/data/1132597/000113259726000054/0001132597-26-000054.txt"
headers = {"User-Agent": "AgentVillage gemini-3-pro@agentvillage.org"}

print(f"--- FETCHING: {url} ---")
try:
    r = requests.get(url, headers=headers, timeout=10)
    content = r.text
    
    clean = re.sub(r'<[^>]+>', ' ', content)
    clean = re.sub(r'\s+', ' ', clean)
    
    # Look for numbers near "buyback" or "shares"
    # "up to X million shares"
    
    idx = clean.lower().find("buyback")
    if idx != -1:
        print(f"CONTEXT: ...{clean[idx:idx+1000]}...")
        
    # Look for "Exhibit 99.1" content again, maybe it's further down
    idx2 = clean.find("Exhibit 99.1")
    if idx2 != -1:
         print(f"EXHIBIT: ...{clean[idx2:idx2+2000]}...")
         
except Exception as e:
    print(e)

import requests
import re

url = "https://www.sec.gov/Archives/edgar/data/845982/000165495426000939/0001654954-26-000939.txt"
headers = {"User-Agent": "AgentVillage gemini-3-pro@agentvillage.org"}

print(f"--- FETCHING: {url} ---")
try:
    r = requests.get(url, headers=headers, timeout=10)
    content = r.text
    
    clean = re.sub(r'<[^>]+>', ' ', content)
    clean = re.sub(r'\s+', ' ', clean)
    
    # Look for the first 1000 characters of the actual body text (after the header)
    # The header usually ends with </SEC-HEADER> or similar, but in the clean text it's just messy.
    # Let's search for "Smith & Nephew" and see what follows.
    
    idx = clean.find("Smith+Nephew")
    if idx != -1:
         print(f"CONTENT: ...{clean[idx:idx+1000]}...")
        
except Exception as e:
    print(e)

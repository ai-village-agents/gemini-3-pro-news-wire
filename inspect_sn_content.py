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
    
    # Print a chunk from the middle/start of body
    idx = clean.find("SIGNATURES")
    if idx != -1:
        print(f"CONTENT BEFORE SIG: ...{clean[idx-2000:idx]}...")
    else:
        print(f"Snippet: {clean[2000:4000]}")
        
except Exception as e:
    print(e)

import requests
import re

url = "https://www.sec.gov/Archives/edgar/data/1098151/000143774926003109/0001437749-26-003109.txt"
headers = {"User-Agent": "AgentVillage gemini-3-pro@agentvillage.org"}

print(f"--- FETCHING: {url} ---")
try:
    r = requests.get(url, headers=headers, timeout=10)
    content = r.text
    
    clean = re.sub(r'<[^>]+>', ' ', content)
    clean = re.sub(r'\s+', ' ', clean)
    
    idx = clean.find("Item 8.01")
    if idx != -1:
        print(f"CONTENT: ...{clean[idx:idx+1000]}...")
    else:
        print("Item 8.01 not found")
        
except Exception as e:
    print(e)

import requests
import re

urls = [
    "https://www.sec.gov/Archives/edgar/data/1160106/000165495426000942/0001654954-26-000942.txt",
    "https://www.sec.gov/Archives/edgar/data/845982/000165495426000939/0001654954-26-000939.txt"
]

headers = {"User-Agent": "AgentVillage gemini-3-pro@agentvillage.org"}

for url in urls:
    print(f"--- FETCHING: {url} ---")
    try:
        r = requests.get(url, headers=headers, timeout=10)
        content = r.text
        
        clean = re.sub(r'<[^>]+>', ' ', content)
        clean = re.sub(r'\s+', ' ', clean)
        
        print(f"START: {clean[:1000]}")
        
    except Exception as e:
        print(e)

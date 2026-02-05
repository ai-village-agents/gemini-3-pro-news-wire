import requests
import re

urls = [
    "https://www.sec.gov/Archives/edgar/data/839923/000165495426000933/0001654954-26-000933.txt",
    "https://www.sec.gov/Archives/edgar/data/924613/000110465926010714/0001104659-26-010714.txt",
    "https://www.sec.gov/Archives/edgar/data/1160106/000165495426000942/0001654954-26-00942.txt"
]

headers = {"User-Agent": "AgentVillage gemini-3-pro@agentvillage.org"}

for url in urls:
    print(f"--- FETCHING: {url} ---")
    try:
        r = requests.get(url, headers=headers, timeout=10)
        content = r.text
        
        clean = re.sub(r'<[^>]+>', ' ', content)
        clean = re.sub(r'\s+', ' ', clean)
        
        for kw in ["Net Income", "Acquisition", "Merger", "Dividend", "Purchase", "agreed"]:
            idx = clean.lower().find(kw.lower())
            if idx != -1:
                print(f"KEYWORD '{kw}': ...{clean[idx-100:idx+400]}...")
                print("")
                
    except Exception as e:
        print(e)

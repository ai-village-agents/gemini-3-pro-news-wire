import requests
import re

urls = [
    "https://www.sec.gov/Archives/edgar/data/1132597/000113259726000041/0001132597-26-000041.txt",
    "https://www.sec.gov/Archives/edgar/data/1160106/000165495426000942/0001654954-26-000942.txt",
    "https://www.sec.gov/Archives/edgar/data/842180/000119312526039000/0001193125-26-039000.txt",
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
        
        # Search for key financial figures or headlines
        for kw in ["Net Income", "Profit", "Revenue", "Acquisition", "Dividend", "agreed to acquire"]:
            idx = clean.lower().find(kw.lower())
            if idx != -1:
                print(f"KEYWORD '{kw}': ...{clean[idx-50:idx+350]}...")
                print("")
                
    except Exception as e:
        print(e)

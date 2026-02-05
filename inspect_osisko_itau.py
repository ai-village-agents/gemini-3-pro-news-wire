import requests
import re

urls = [
    "https://www.sec.gov/Archives/edgar/data/1431852/000110465926010723/0001104659-26-010723.txt",
    "https://www.sec.gov/Archives/edgar/data/1132597/000113259726000040/0001132597-26-000040.txt",
    "https://www.sec.gov/Archives/edgar/data/1132597/000113259726000044/0001132597-26-000044.txt"
]

headers = {"User-Agent": "AgentVillage gemini-3-pro@agentvillage.org"}

for url in urls:
    print(f"--- FETCHING: {url} ---")
    try:
        r = requests.get(url, headers=headers, timeout=10)
        content = r.text
        
        clean = re.sub(r'<[^>]+>', ' ', content)
        clean = re.sub(r'\s+', ' ', clean)
        
        # Check for Press Release or Material Fact
        for kw in ["Press Release", "Material Fact", "Exhibit 99.1"]:
            idx = clean.find(kw)
            if idx != -1:
                print(f"CONTEXT ({kw}): ...{clean[idx:idx+1000]}...")
                
    except Exception as e:
        print(e)

import requests
import re

urls = [
    "https://www.sec.gov/Archives/edgar/data/1334388/000119312526038933/0001193125-26-038933.txt",
    "https://www.sec.gov/Archives/edgar/data/1431852/000110465926010723/0001104659-26-010723.txt",
    "https://www.sec.gov/Archives/edgar/data/1681348/000149315226005214/0001493152-26-005214.txt"
]

headers = {"User-Agent": "AgentVillage gemini-3-pro@agentvillage.org"}

for url in urls:
    print(f"--- FETCHING: {url} ---")
    try:
        r = requests.get(url, headers=headers, timeout=10)
        content = r.text
        
        clean = re.sub(r'<[^>]+>', ' ', content)
        clean = re.sub(r'\s+', ' ', clean)
        
        # Search for key terms
        for kw in ["Net Income", "Production", "Acquisition", "Offering", "Private Placement", "Drilling"]:
            idx = clean.lower().find(kw.lower())
            if idx != -1:
                print(f"KEYWORD '{kw}': ...{clean[idx-100:idx+400]}...")
                print("")
                
    except Exception as e:
        print(e)

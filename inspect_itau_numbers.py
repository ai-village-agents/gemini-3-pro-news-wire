import requests
import re

urls = [
    "https://www.sec.gov/Archives/edgar/data/1132597/000113259726000054/0001132597-26-000054.txt",
    "https://www.sec.gov/Archives/edgar/data/1132597/000113259726000055/0001132597-26-000055.txt"
]

headers = {"User-Agent": "AgentVillage gemini-3-pro@agentvillage.org"}

for url in urls:
    print(f"--- FETCHING: {url} ---")
    try:
        r = requests.get(url, headers=headers, timeout=10)
        content = r.text
        
        clean = re.sub(r'<[^>]+>', ' ', content)
        clean = re.sub(r'\s+', ' ', clean)
        
        # Buyback details
        if "000054" in url:
            for kw in ["buyback", "repurchase", "million shares", "billion reais", "program"]:
                idx = clean.lower().find(kw)
                if idx != -1:
                    print(f"BUYBACK ({kw}): ...{clean[idx-100:idx+400]}...")
        
        # Earnings details
        if "000055" in url:
             for kw in ["Net Income", "Recurring Managerial Result", "ROE", "Return on Equity"]:
                idx = clean.lower().find(kw.lower())
                if idx != -1:
                    print(f"EARNINGS ({kw}): ...{clean[idx-100:idx+400]}...")

    except Exception as e:
        print(e)

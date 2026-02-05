import requests
import re

urls = [
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
        
        # Search for "Exhibit 99.1" and print text around/after it
        idx = clean.find("Exhibit 99.1")
        if idx != -1:
            print(f"EXHIBIT 99.1 CONTEXT: ...{clean[idx:idx+2000]}...")
        else:
             print(f"Snippet: {clean[:1000]}")

    except Exception as e:
        print(e)

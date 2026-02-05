import requests
import re

urls = [
    "https://www.sec.gov/Archives/edgar/data/1692345/000110465926010843/0001104659-26-010843.txt",
    "https://www.sec.gov/Archives/edgar/data/1093691/000110465926010793/0001104659-26-010793.txt"
]

headers = {"User-Agent": "AgentVillage gemini-3-pro@agentvillage.org"}

for url in urls:
    print(f"--- FETCHING: {url} ---")
    try:
        r = requests.get(url, headers=headers, timeout=10)
        content = r.text
        
        # Simple extraction of Item 8.01 text
        # Look for "Item 8.01" and print following text
        clean = re.sub(r'<[^>]+>', ' ', content)
        clean = re.sub(r'\s+', ' ', clean)
        
        idx = clean.find("Item 8.01")
        if idx != -1:
            print(f"CONTENT: ...{clean[idx:idx+1000]}...")
        else:
            print("Item 8.01 not found in text (might be in header or complex format)")
            print(f"Snippet: {clean[:500]}")
            
    except Exception as e:
        print(e)

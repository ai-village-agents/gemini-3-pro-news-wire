import requests
import re

urls = [
    "https://www.sec.gov/Archives/edgar/data/863064/000086306426000010/0000863064-26-000010.txt",
    "https://www.sec.gov/Archives/edgar/data/1243429/000124342926000011/0001243429-26-000011.txt",
    "https://www.sec.gov/Archives/edgar/data/1306965/000117184326000645/0001171843-26-000645.txt",
    "https://www.sec.gov/Archives/edgar/data/1681348/000149315226005214/0001493152-26-005214.txt"
]

headers = {"User-Agent": "AgentVillage gemini-3-pro@agentvillage.org"}

for url in urls:
    print(f"--- FETCHING: {url} ---")
    try:
        r = requests.get(url, headers=headers, timeout=10)
        content = r.text
        # Try to find the start of the actual document, often after <TEXT> or similar
        # But 6-Ks are messy. Let's just print a chunk from the middle or search for the "News Release"
        
        # Look for the press release body roughly
        clean_text = re.sub(r'<[^>]+>', ' ', content)
        clean_text = re.sub(r'\s+', ' ', clean_text)
        
        # Print a window around keywords
        for kw in ["Net Income", "Acquisition", "Merger", "Dividend", "offering"]:
            idx = clean_text.lower().find(kw.lower())
            if idx != -1:
                print(f"KEYWORD '{kw}': ...{clean_text[idx-100:idx+400]}...")
                print("")
                
    except Exception as e:
        print(e)

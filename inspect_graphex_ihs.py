import requests
import re

urls = [
    "https://www.sec.gov/Archives/edgar/data/1816723/000149315226005220/0001493152-26-005220.txt",
    "https://www.sec.gov/Archives/edgar/data/1876183/000110465926010739/0001104659-26-010739.txt"
]

headers = {"User-Agent": "AgentVillage gemini-3-pro@agentvillage.org"}

for url in urls:
    print(f"--- FETCHING: {url} ---")
    try:
        r = requests.get(url, headers=headers, timeout=10)
        content = r.text
        
        clean = re.sub(r'<[^>]+>', ' ', content)
        clean = re.sub(r'\s+', ' ', clean)
        
        # Search for Exhibit 99.1 or press release content
        idx = clean.find("Exhibit 99.1")
        if idx != -1:
            print(f"EXHIBIT 99.1 CONTEXT: ...{clean[idx:idx+1500]}...")
        else:
             print(f"Snippet: {clean[:1000]}")
             
        # Look for specific keywords context
        for kw in ["Resignation", "appoint", "acquire", "offering"]:
             idx_kw = clean.lower().find(kw.lower())
             if idx_kw != -1:
                 print(f"KEYWORD '{kw}': ...{clean[idx_kw-50:idx_kw+250]}...")

    except Exception as e:
        print(e)

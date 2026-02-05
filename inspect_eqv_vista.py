import requests
import re

urls = [
    "https://www.sec.gov/Archives/edgar/data/2021042/000121390026012569/0001213900-26-012569.txt",
    "https://www.sec.gov/Archives/edgar/data/1919369/000119312526037368/0001193125-26-037368.txt"
]

headers = {"User-Agent": "AgentVillage gemini-3-pro@agentvillage.org"}

for url in urls:
    print(f"--- FETCHING: {url} ---")
    try:
        r = requests.get(url, headers=headers, timeout=10)
        content = r.text
        
        clean = re.sub(r'<[^>]+>', ' ', content)
        clean = re.sub(r'\s+', ' ', clean)
        
        # Print a chunk of the text to identify the event
        # Skip the header junk
        idx = clean.find("Item ")
        if idx != -1:
            print(f"CONTENT: ...{clean[idx:idx+1500]}...")
        else:
            print(f"Snippet: {clean[5000:6500]}")
            
    except Exception as e:
        print(e)

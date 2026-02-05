import requests
import re

urls = [
    "https://www.sec.gov/Archives/edgar/data/1132597/000113259726000040/0001132597-26-000040.txt",
    "https://www.sec.gov/Archives/edgar/data/1132597/000113259726000044/0001132597-26-000044.txt",
    "https://www.sec.gov/Archives/edgar/data/1132597/000113259726000048/0001132597-26-000048.txt",
    "https://www.sec.gov/Archives/edgar/data/1132597/000113259726000050/0001132597-26-000050.txt",
    "https://www.sec.gov/Archives/edgar/data/1132597/000113259726000052/0001132597-26-000052.txt",
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
        
        # Try to find title or summary in the body
        # Itau usually puts "Material Fact" or "Notice to the Market" or "News Release"
        
        found = False
        for tag in ["Material Fact", "Notice to the Market", "News Release", "Announcement"]:
            idx = clean.find(tag)
            if idx != -1:
                print(f"TYPE: {tag}")
                print(f"CONTENT: ...{clean[idx:idx+400]}...")
                found = True
                break
        
        if not found:
            # Look for Exhibit description
            idx = clean.find("Exhibit 99.1")
            if idx != -1:
                print(f"EXHIBIT: ...{clean[idx:idx+300]}...")
            else:
                 print(f"Snippet: {clean[5000:5500]}")

    except Exception as e:
        print(e)

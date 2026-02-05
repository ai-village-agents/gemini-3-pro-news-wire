import requests
import time
import sys

headers = {
    "User-Agent": "AgentVillage gemini-3-pro@agentvillage.org"
}

urls = {
    "doximity": "https://www.sec.gov/Archives/edgar/data/1516513/000151651326000004/0001516513-26-000004.txt",
    "lulus": "https://www.sec.gov/Archives/edgar/data/1780201/000110465926010874/0001104659-26-010874.txt",
    "mcgrath": "https://www.sec.gov/Archives/edgar/data/752714/000119312526039337/0001193125-26-039337.txt",
    "opentext": "https://www.sec.gov/Archives/edgar/data/1002638/000100263826000020/0001002638-26-000020.txt",
    "artelo": "https://www.sec.gov/Archives/edgar/data/1621221/000164033426000227/0001640334-26-000227.txt"
}

for name, url in urls.items():
    print(f"Fetching {name}...")
    try:
        r = requests.get(url, headers=headers, timeout=15)
        if r.status_code == 200:
            with open(f"{name}_8k.txt", "w") as f:
                f.write(r.text)
            print(f"Saved {name}_8k.txt")
        else:
            print(f"Failed {name}: {r.status_code}")
    except Exception as e:
        print(f"Error {name}: {e}")
    
    time.sleep(2) # Politeness delay

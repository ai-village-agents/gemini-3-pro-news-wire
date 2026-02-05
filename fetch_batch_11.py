import requests
import time

headers = {
    "User-Agent": "AgentVillage gemini-3-pro@agentvillage.org"
}

urls = {
    "superx": "https://www.sec.gov/Archives/edgar/data/1897087/000121390026012758/0001213900-26-012758.txt",
    "kanzhun": "https://www.sec.gov/Archives/edgar/data/1842827/000110465926010880/0001104659-26-010880.txt",
    "kidoz": "https://www.sec.gov/Archives/edgar/data/1318482/000149315226005256/0001493152-26-005256.txt",
    "brbi": "https://www.sec.gov/Archives/edgar/data/2058601/000121390026012757/0001213900-26-012757.txt"
}

for name, url in urls.items():
    print(f"Fetching {name}...")
    try:
        r = requests.get(url, headers=headers, timeout=15)
        with open(f"{name}_6k.txt", "w") as f:
            f.write(r.text)
    except Exception as e:
        print(f"Error {name}: {e}")
    time.sleep(1)

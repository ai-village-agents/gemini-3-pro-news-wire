import requests
import time

headers = {
    "User-Agent": "AgentVillage gemini-3-pro@agentvillage.org"
}

urls = {
    "greenlight": "https://www.sec.gov/Archives/edgar/data/1385613/000138561326000003/0001385613-26-000003.txt",
    "i3verticals": "https://www.sec.gov/Archives/edgar/data/1728688/000172868826000017/0001728688-26-000017.txt",
    "rayonier": "https://www.sec.gov/Archives/edgar/data/1806931/000005282726000021/0000052827-26-000021.txt",
    "lexeo": "https://www.sec.gov/Archives/edgar/data/1907108/000119312526039425/0001193125-26-039425.txt",
    "curiosity": "https://www.sec.gov/Archives/edgar/data/1776909/000162828026005796/0001628280-26-005796.txt"
}

for name, url in urls.items():
    print(f"Fetching {name}...")
    try:
        r = requests.get(url, headers=headers, timeout=15)
        with open(f"{name}_8k.txt", "w") as f:
            f.write(r.text)
    except Exception as e:
        print(f"Error {name}: {e}")
    time.sleep(1)

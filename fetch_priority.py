import requests
import time

urls = {
    "BAM": "https://www.sec.gov/Archives/edgar/data/1937926/000110465926010078/0001104659-26-010078.txt",
    "NRG": "https://www.sec.gov/Archives/edgar/data/1013871/000110465926010079/0001104659-26-010079.txt",
    "PIPR": "https://www.sec.gov/Archives/edgar/data/1230245/000123024526000005/0001230245-26-000005.txt"
}

headers = {
    "User-Agent": "AgentVillage gemini-3-pro@agentvillage.org"
}

for ticker, url in urls.items():
    try:
        print(f"Fetching {ticker}...")
        time.sleep(0.2)
        response = requests.get(url, headers=headers, timeout=10)
        filename = f"{ticker}_8k.txt"
        with open(filename, 'w') as f:
            f.write(response.text)
        print(f"Saved {ticker} to {filename}")
    except Exception as e:
        print(f"Error fetching {ticker}: {e}")

import requests

url = "https://www.sec.gov/Archives/edgar/data/1725057/000114036126003628/0001140361-26-003628.txt"
headers = {
    "User-Agent": "AgentVillage gemini-3-pro@agentvillage.org"
}

try:
    response = requests.get(url, headers=headers)
    print(response.text[:2000]) # Print first 2000 chars to check
    with open('dayforce_8k.txt', 'w') as f:
        f.write(response.text)
except Exception as e:
    print(f"Error: {e}")

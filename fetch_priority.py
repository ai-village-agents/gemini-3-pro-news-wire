import sys
import time
import requests
from bs4 import BeautifulSoup
import re

urls = [
    "https://www.sec.gov/Archives/edgar/data/1473490/000149315226005096/0001493152-26-005096.txt",
    "https://www.sec.gov/Archives/edgar/data/946644/000149315226005208/0001493152-26-005208.txt"
]

headers = {'User-Agent': 'AgentVillage gemini-3-pro@agentvillage.org'}

for url in urls:
    try:
        print(f"Fetching {url}...")
        time.sleep(0.2)
        response = requests.get(url, headers=headers, timeout=10)
        content = response.text
        
        soup = BeautifulSoup(content, 'html.parser')
        clean_text = soup.get_text(separator='\n')
        
        filename = "global_ai_content.txt" if "1473490" in url else "aim_content.txt"
        
        with open(filename, 'w') as f:
            f.write(clean_text)
            
        print(f"Saved to {filename}")
        
        # Quick summary check
        print("--- SUMMARY PREVIEW ---")
        lines = clean_text.split('\n')
        for i, line in enumerate(lines):
            if "Item " in line:
                print(line)
                # Print next few lines
                for j in range(1, 15):
                    if i+j < len(lines):
                        print(lines[i+j].strip())
        print("-----------------------")

    except Exception as e:
        print(f"Error: {e}")

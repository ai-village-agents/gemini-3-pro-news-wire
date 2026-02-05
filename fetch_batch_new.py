import time
import requests
from bs4 import BeautifulSoup
import re

targets = [
    ("MKS Instruments", "https://www.sec.gov/Archives/edgar/data/1049502/000119312526038565/0001193125-26-038565.txt"),
    ("Plug Power", "https://www.sec.gov/Archives/edgar/data/1093691/000110465926010793/0001104659-26-010793.txt"),
    ("AMN Healthcare", "https://www.sec.gov/Archives/edgar/data/1142750/000095014226000299/0000950142-26-000299.txt"),
    ("Strata Critical", "https://www.sec.gov/Archives/edgar/data/1779128/000110465926010689/0001104659-26-010689.txt"),
    ("ECB Bancorp", "https://www.sec.gov/Archives/edgar/data/1914605/000143774926003106/0001437749-26-003106.txt")
]

headers = {'User-Agent': 'AgentVillage gemini-3-pro@agentvillage.org'}

for company, url in targets:
    print(f"\nFetching {company}...")
    try:
        time.sleep(0.2)
        response = requests.get(url, headers=headers, timeout=10)
        content = response.text
        
        # Simple extraction of the 8-K body text
        # Remove XML tags to get raw text
        soup = BeautifulSoup(content, 'html.parser')
        text = soup.get_text('\n')
        clean_text = re.sub(r'\n\s*\n', '\n', text)
        
        filename = f"{company.replace(' ', '_').lower()}_content.txt"
        with open(filename, 'w') as f:
            f.write(clean_text)
            
        print(f"Saved to {filename}. Preview:")
        
        # Heuristic to find the "Item" sections
        items = []
        lines = clean_text.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith("Item") and any(x in line for x in ["1.01", "2.02", "5.02", "7.01", "8.01"]):
                items.append((i, line.strip()))
                
        if items:
            for idx, item_header in items:
                print(f"  >>> {item_header}")
                # Print first 300 chars of content
                context = "\n".join(lines[idx+1:idx+20])
                print(f"      {context[:200]}...")
        else:
            print("  No explicit Item headers found in plain text. Dumping first 500 chars:")
            print(clean_text[:500])

    except Exception as e:
        print(f"Error fetching {company}: {e}")


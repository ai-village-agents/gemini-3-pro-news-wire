import sys
import time
import requests
import re
from bs4 import BeautifulSoup

def get_filing_content(url):
    headers = {'User-Agent': 'AgentVillage gemini-3-pro@agentvillage.org'}
    try:
        time.sleep(0.2)
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        text = response.text
        
        # Clean up HTML tags if present, or just process text
        soup = BeautifulSoup(text, 'html.parser')
        clean_text = soup.get_text(separator='\n')
        
        # Look for Item headers
        lines = clean_text.split('\n')
        relevant_lines = []
        capture = False
        buffer_count = 0
        
        for i, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue
                
            # Detect Item Header
            if re.match(r'^Item\s+\d+\.\d+', line, re.IGNORECASE):
                capture = True
                relevant_lines.append(f"\n--- {line} ---\n")
                buffer_count = 0
            
            if capture:
                relevant_lines.append(line)
                buffer_count += 1
                
            # Stop capturing after some lines if we hit a signature or another major section
            if capture and buffer_count > 60: # distinct capture limit per item
                capture = False
                
        return "\n".join(relevant_lines)
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 fetch_details.py <url>")
    else:
        print(get_filing_content(sys.argv[1]))

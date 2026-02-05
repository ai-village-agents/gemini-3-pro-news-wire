import re
from bs4 import BeautifulSoup
import sys

def extract_story(filename, company_name):
    print(f"\n--- Processing {company_name} ({filename}) ---")
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
        sections = re.split(r'<DOCUMENT>', content)
        
        target_section = None
        for section in sections:
            if '<TYPE>8-K' in section:
                target_section = section
                break
                
        if not target_section:
            print("Could not find 8-K document section.")
            # Fallback: just try to find the text in the whole file if it's small or weird
            target_section = content

        text_match = re.search(r'<TEXT>(.*?)</TEXT>', target_section, re.DOTALL)
        if text_match:
            html_content = text_match.group(1)
        else:
            html_content = target_section
            
        soup = BeautifulSoup(html_content, 'html.parser')
        text = soup.get_text('\n')
        
        clean_text = re.sub(r'\n\s*\n', '\n\n', text)
        
        print(f"--- EXTRACTED TEXT FOR {company_name} ---")
        
        lines = clean_text.split('\n')
        printing = False
        item_found = False
        
        for line in lines:
            if "Item" in line and ("5.02" in line or "8.01" in line or "7.01" in line or "1.01" in line or "2.02" in line):
                printing = True
                item_found = True
                print(f"\n>>> {line.strip()} <<<\n")
                continue
            
            if "SIGNATURE" in line or "Item 9.01" in line:
                printing = False
            
            if printing:
                print(line.strip())
                
        if not item_found:
             print("No specific Item headers found. Dumping first 3000 chars:")
             print(clean_text[:3000])

    except Exception as e:
        print(f"Error: {e}")

extract_story('global_ai_content.txt', 'Global AI, Inc.')
extract_story('aim_content.txt', 'AIM ImmunoTech Inc.')

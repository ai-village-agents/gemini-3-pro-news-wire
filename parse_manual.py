import re
from bs4 import BeautifulSoup

files = ['global_ai_content.txt', 'aim_content.txt']

for filename in files:
    print(f"\nProcessing {filename}...")
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
        # Find the 8-K document
        # Usually bounded by <DOCUMENT> <TYPE>8-K ... <TEXT> ... </TEXT> </DOCUMENT>
        
        doc_match = re.search(r'<TYPE>8-K.*?<TEXT>(.*?)</TEXT>', content, re.DOTALL)
        if not doc_match:
             # Try simple text extraction if XML/SGML parsing fails or is weird
             soup = BeautifulSoup(content, 'html.parser')
             text = soup.get_text('\n')
        else:
            html_content = doc_match.group(1)
            soup = BeautifulSoup(html_content, 'html.parser')
            text = soup.get_text('\n')
            
        # Clean up empty lines
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        
        print("--- EXTRACTED CONTENT START ---")
        # Print the first 50 lines to identify items
        for line in lines[:50]:
            print(line)
            
        print("--- SEARCHING FOR ITEMS ---")
        # Search for Item headers specifically
        for i, line in enumerate(lines):
            if line.startswith("Item ") or "Item 5.02" in line or "Item 8.01" in line:
                print(f"FOUND: {line}")
                # Print context
                for j in range(1, 20):
                    if i+j < len(lines):
                        print(f"  {lines[i+j]}")
                print("...")
                
    except Exception as e:
        print(f"Error: {e}")

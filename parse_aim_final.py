import re
from bs4 import BeautifulSoup

filename = 'aim_content.txt'
print(f"--- Processing {filename} ---")

with open(filename, 'r') as f:
    content = f.read()

# Split by <DOCUMENT> tags to isolate the 8-K HTML
documents = content.split('<DOCUMENT>')
print(f"Found {len(documents)} document sections.")

for i, doc in enumerate(documents):
    # Check if this document is the 8-K HTML
    if '<TYPE>8-K' in doc or 'form8-k.htm' in doc:
        print(f"\n--- Document {i} (Likely 8-K) ---")
        
        # Extract text between <TEXT> and </TEXT>
        text_match = re.search(r'<TEXT>(.*?)</TEXT>', doc, re.DOTALL)
        if text_match:
            html = text_match.group(1)
            soup = BeautifulSoup(html, 'html.parser')
            text = soup.get_text('\n')
            
            # Clean up
            clean_text = re.sub(r'\n\s*\n', '\n', text)
            
            # Search for Item 8.01 or 7.01 within this specific document text
            if "Item 8.01" in clean_text or "Item 7.01" in clean_text or "Other Events" in clean_text:
                print(">>> FOUND ITEMS IN THIS DOC <<<")
                # Print a good chunk of text to verify
                print(clean_text[:5000]) # Print first 5000 chars of the cleaned text
            else:
                 print("Items not found in this 8-K doc text. Printing start anyway...")
                 print(clean_text[:2000])
                 
    elif '<TYPE>EX-99.1' in doc:
        print(f"\n--- Document {i} (Exhibit 99.1 - Press Release?) ---")
        text_match = re.search(r'<TEXT>(.*?)</TEXT>', doc, re.DOTALL)
        if text_match:
            html = text_match.group(1)
            soup = BeautifulSoup(html, 'html.parser')
            text = soup.get_text('\n')
            clean_text = re.sub(r'\n\s*\n', '\n', text)
            print(clean_text[:3000])


import re
from bs4 import BeautifulSoup

filename = 'aim_content.txt'
print(f"--- Extracting AIM Body from {filename} ---")

with open(filename, 'r') as f:
    content = f.read()

soup = BeautifulSoup(content, 'html.parser')
text = soup.get_text('\n')
clean_text = re.sub(r'\n\s*\n', '\n', text)

# Find the end of the cover page
# "Securities registered pursuant to Section 12(b)" is a good anchor
anchor = "Securities registered pursuant to Section 12(b)"
idx = clean_text.find(anchor)

if idx != -1:
    print(f"Found anchor '{anchor}' at index {idx}")
    # Print the text following this anchor
    # usually there's a table, then the Items
    start_idx = idx + len(anchor)
    print(clean_text[start_idx:start_idx+5000])
else:
    print("Anchor not found. Searching for 'Item 8.01' again in the whole text...")
    idx_801 = clean_text.find("Item 8.01")
    if idx_801 != -1:
         # Find the SECOND occurrence? The first might be the header.
         idx_801_2 = clean_text.find("Item 8.01", idx_801 + 100)
         if idx_801_2 != -1:
             print("Found second occurrence of Item 8.01:")
             print(clean_text[idx_801_2:idx_801_2+2000])
         else:
             print("Only one occurrence of Item 8.01 found:")
             print(clean_text[idx_801:idx_801+2000])


import re
from bs4 import BeautifulSoup

filename = 'aim_content.txt'
print(f"--- Processing {filename} ---")

with open(filename, 'r') as f:
    content = f.read()

# Strategy: Find "Item 7.01" or "Item 8.01" loosely
# The grep showed "Regulation FD Disclosure" and "Other Events"
# Let's find those strings and print the next 2000 characters

# Remove all HTML tags first to make searching easier
soup = BeautifulSoup(content, 'html.parser')
text = soup.get_text('\n')
# Clean excessive newlines
clean_text = re.sub(r'\n\s*\n', '\n', text)

item_701_idx = clean_text.find("Regulation FD Disclosure")
if item_701_idx != -1:
    print("\n>>> FOUND ITEM 7.01 (Regulation FD Disclosure) <<<")
    print(clean_text[item_701_idx:item_701_idx+1500])

item_801_idx = clean_text.find("Other Events")
if item_801_idx != -1:
    print("\n>>> FOUND ITEM 8.01 (Other Events) <<<")
    print(clean_text[item_801_idx:item_801_idx+1500])
    
# Also check for "Item 8.01" string directly
item_801_direct = clean_text.find("Item 8.01")
if item_801_direct != -1:
    print("\n>>> FOUND 'Item 8.01' DIRECTLY <<<")
    print(clean_text[item_801_direct:item_801_direct+1500])


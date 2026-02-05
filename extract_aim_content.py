import re
from bs4 import BeautifulSoup

filename = 'aim_content.txt'
print(f"--- Extracting AIM Content from {filename} ---")

with open(filename, 'r') as f:
    content = f.read()

# Remove SGML tags to make it cleaner text
# We'll just look for the text block that contains Item 8.01
# It's likely within an <HTML> block inside <TEXT>

soup = BeautifulSoup(content, 'html.parser')
text = soup.get_text('\n')

# Normalize whitespace
clean_text = re.sub(r'\n\s*\n', '\n', text)

# Find Item 8.01
idx_801 = clean_text.find("Item 8.01")
if idx_801 == -1:
    idx_801 = clean_text.find("Other Events")

if idx_801 != -1:
    print("\n>>> FOUND ITEM 8.01 BLOCK <<<")
    # Print the next 2000 chars
    print(clean_text[idx_801:idx_801+3000])
else:
    print("Could not find Item 8.01 text.")

# Check for Item 7.01
idx_701 = clean_text.find("Item 7.01")
if idx_701 == -1:
    idx_701 = clean_text.find("Regulation FD Disclosure")

if idx_701 != -1:
    print("\n>>> FOUND ITEM 7.01 BLOCK <<<")
    print(clean_text[idx_701:idx_701+3000])


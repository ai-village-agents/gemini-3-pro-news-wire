import re
from bs4 import BeautifulSoup

filename = 'aim_content.txt'

print(f"\n--- Parsing AIM ImmunoTech Deep Dive ({filename}) ---")
try:
    with open(filename, 'r') as f:
        content = f.read()

    # Look for "Item" followed by numbers
    # The regex r'Item\s*[0-9]\.[0-9]{2}' might be split across lines or tags
    
    # Let's try to find "Regulation FD Disclosure" which is usually Item 7.01
    if "Regulation FD Disclosure" in content:
         print("Found 'Regulation FD Disclosure'. Extracting...")
         start = content.find("Regulation FD Disclosure")
         end = start + 3000
         chunk = content[start:end]
         soup = BeautifulSoup(chunk, 'html.parser')
         print(soup.get_text('\n'))
         
    # Let's try "Other Events" which is Item 8.01
    if "Other Events" in content:
         print("\nFound 'Other Events'. Extracting...")
         start = content.find("Other Events")
         end = start + 3000
         chunk = content[start:end]
         soup = BeautifulSoup(chunk, 'html.parser')
         print(soup.get_text('\n'))

except Exception as e:
    print(f"Error: {e}")

import re
import sys

def parse_filing(filename, ticker):
    print(f"\n--- PROCESSING {ticker} ({filename}) ---")
    try:
        with open(filename, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print("File not found.")
        return

    # Item 5.01 Change in Control
    item_501 = re.search(r'Item\s+5\.01(.*?)(Item\s+\d+\.\d+|SIGNATURE)', content, re.DOTALL | re.IGNORECASE)
    if item_501:
        print(">>> FOUND ITEM 5.01 (Change in Control):")
        print(item_501.group(1)[:1500].strip())

    # Item 5.02 Departure/Election
    item_502 = re.search(r'Item\s+5\.02(.*?)(Item\s+\d+\.\d+|SIGNATURE)', content, re.DOTALL | re.IGNORECASE)
    if item_502:
        print(">>> FOUND ITEM 5.02 (Departure/Election):")
        print(item_502.group(1)[:1500].strip())

    # Item 1.01 Entry into Material Agreement
    item_101 = re.search(r'Item\s+1\.01(.*?)(Item\s+\d+\.\d+|SIGNATURE)', content, re.DOTALL | re.IGNORECASE)
    if item_101:
        print(">>> FOUND ITEM 1.01 (Material Agreement):")
        print(item_101.group(1)[:1500].strip())

parse_filing('aquabounty.txt', 'AQB')
parse_filing('firefly.txt', 'AIFF')
parse_filing('lipella.txt', 'LIPO')

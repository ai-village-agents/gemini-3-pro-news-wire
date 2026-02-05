import re
from bs4 import BeautifulSoup
import sys

def parse_global_ai(filename):
    print(f"\n--- Parsing Global AI Specifics ({filename}) ---")
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
        # We know from the grep earlier that "Item" headers are missing or weird in the first pass
        # But let's look for "Item 5.02" specifically in the whole file
        
        if "Item 5.02" in content:
            print("Found 'Item 5.02' in raw text.")
            # Extract the paragraph around it
            start = content.find("Item 5.02")
            end = start + 5000 # Grab a big chunk
            chunk = content[start:end]
            
            # Clean HTML if present
            soup = BeautifulSoup(chunk, 'html.parser')
            text = soup.get_text('\n')
            
            print("--- GLOBAL AI ITEM 5.02 CONTENT ---")
            print(text)
            
            # Extract specific details
            # Look for "2026 Global Equity Incentive Plan"
            if "2026 Global Equity Incentive Plan" in text:
                 print("\n>>> CONFIRMED: 2026 Global Equity Incentive Plan mentioned.")
        else:
            print("'Item 5.02' NOT found in raw text. Checking for 'Equity Incentive Plan' directly...")
            if "Equity Incentive Plan" in content:
                 print("Found 'Equity Incentive Plan'. Extracting context...")
                 start = content.find("Equity Incentive Plan") - 200
                 end = start + 2000
                 chunk = content[start:end]
                 soup = BeautifulSoup(chunk, 'html.parser')
                 print(soup.get_text('\n'))

    except Exception as e:
        print(f"Error: {e}")

def parse_aim(filename):
    print(f"\n--- Parsing AIM ImmunoTech Specifics ({filename}) ---")
    try:
        with open(filename, 'r') as f:
            content = f.read()

        # Check for Item 8.01 or 7.01
        if "Item 8.01" in content:
             print("Found 'Item 8.01'. Extracting...")
             start = content.find("Item 8.01")
             end = start + 3000
             chunk = content[start:end]
             soup = BeautifulSoup(chunk, 'html.parser')
             print(soup.get_text('\n'))
        elif "Item 7.01" in content:
             print("Found 'Item 7.01'. Extracting...")
             start = content.find("Item 7.01")
             end = start + 3000
             chunk = content[start:end]
             soup = BeautifulSoup(chunk, 'html.parser')
             print(soup.get_text('\n'))
        else:
             print("No standard Items found. Checking for 'Press Release' or content...")
             # Look for typical 8-K intro text
             if "On February 5, 2026" in content or "On February 4, 2026" in content:
                 print("Found date pattern. Extracting...")
                 idx = content.find("On February")
                 chunk = content[idx:idx+2000]
                 soup = BeautifulSoup(chunk, 'html.parser')
                 print(soup.get_text('\n'))

    except Exception as e:
        print(f"Error: {e}")

parse_global_ai('global_ai_content.txt')
parse_aim('aim_content.txt')

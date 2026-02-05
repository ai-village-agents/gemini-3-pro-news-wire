import re

files = ["superx_6k.txt", "kanzhun_6k.txt", "kidoz_6k.txt", "brbi_6k.txt"]

for filename in files:
    print(f"\n=== {filename} ===")
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
        # Look for the start of the actual report or press release
        # Often "Exhibit 99.1" or just search for keywords
        
        if "superx" in filename:
             print(re.findall(r'(placement|offering|shares|price|proceeds).{0,100}', content[:10000], re.IGNORECASE)[:5])
             
        if "kanzhun" in filename:
             print(re.findall(r'(dividend|record date|payable|distribution).{0,100}', content[:5000], re.IGNORECASE)[:5])
             
        if "kidoz" in filename:
             # Look for revenue or net income
             print(re.findall(r'(revenue|income|profit|loss|EBITDA).{0,50}', content[:5000], re.IGNORECASE)[:5])

        if "brbi" in filename:
             print(re.findall(r'(net income|dividend|R$|million|billion).{0,50}', content[:5000], re.IGNORECASE)[:5])

    except Exception as e:
        print(f"Error: {e}")

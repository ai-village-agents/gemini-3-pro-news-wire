import re

files = ["superx_6k.txt", "kanzhun_6k.txt", "kidoz_6k.txt", "brbi_6k.txt"]

for filename in files:
    print(f"\n=== {filename} ===")
    try:
        with open(filename, 'r') as f:
            content = f.read()
        
        # SuperX: Look for "Placement", "$", "shares"
        if "superx" in filename:
            # Simple regex to find amounts
            amounts = re.findall(r'$[\d,]+(?:\.\d+)?\s*(?:million|billion)?', content)
            print(f"Amounts found: {amounts[:5]}")
            # Look for context around "placement"
            match = re.search(r'(.{100}private placement.{100})', content, re.IGNORECASE | re.DOTALL)
            if match:
                print(f"Placement Context: ...{match.group(1)}...")

        # Kidoz: Look for "Revenue", "Net Income"
        if "kidoz" in filename:
            match = re.search(r'(.{100}revenue.{100})', content, re.IGNORECASE | re.DOTALL)
            if match:
                 print(f"Revenue Context: ...{match.group(1)}...")

        # BRBI: Look for Portuguese terms if english absent, or "Dividend"
        if "brbi" in filename:
             match = re.search(r'(.{100}dividend.{100})', content, re.IGNORECASE | re.DOTALL)
             if match:
                 print(f"Dividend Context: ...{match.group(1)}...")

    except Exception as e:
        print(f"Error: {e}")

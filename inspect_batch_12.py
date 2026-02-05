import re

files = ["stonepeak_8k.txt", "sunshine_8k.txt"]

for filename in files:
    print(f"\n=== {filename} ===")
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
        if "stonepeak" in filename:
            # Look for amount sold
            print(re.findall(r'($[\d,]+(?:\.\d+)?\s*(?:million|billion)?)', content[:5000]))
            print(re.search(r'Item 3.02.*?Item', content, re.DOTALL | re.IGNORECASE))

        if "sunshine" in filename:
            # Look for officer name
            print(re.search(r'Item 5.02.*?Item', content, re.DOTALL | re.IGNORECASE))
            
    except Exception as e:
        print(e)

import re

try:
    with open('lee_enterprises_8k.txt', 'r') as f:
        content = f.read()
    
    # Check for SEC block
    if "Undeclared Automated Tool" in content:
        print("BLOCKED")
    else:
        # Item 5.01 Change in Control
        print("--- Item 5.01 Change in Control ---")
        match = re.search(r'Item 5.01.*?Control(.*?)Item', content, re.DOTALL | re.IGNORECASE)
        if match:
            print(match.group(1)[:500])
        else:
            # Fallback search
            print(re.search(r'Change in Control.{0,500}', content, re.DOTALL | re.IGNORECASE))

        # Item 5.02 Departure
        print("\n--- Item 5.02 Departure ---")
        match = re.search(r'Item 5.02.*?Departure(.*?)Item', content, re.DOTALL | re.IGNORECASE)
        if match:
             print(match.group(1)[:500])
             
        # Item 3.02 Unregistered Sales
        print("\n--- Item 3.02 Unregistered Sales ---")
        match = re.search(r'Item 3.02.*?Unregistered(.*?)Item', content, re.DOTALL | re.IGNORECASE)
        if match:
             print(match.group(1)[:500])

except Exception as e:
    print(e)

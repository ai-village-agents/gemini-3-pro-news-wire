import re

files = ["greenlight_8k.txt", "i3verticals_8k.txt", "rayonier_8k.txt", "lexeo_8k.txt", "curiosity_8k.txt"]

for filename in files:
    print(f"\n=== {filename} ===")
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
        # Clean tags
        clean = re.sub(r'<[^>]+>', ' ', content)
        clean = re.sub(r'\s+', ' ', clean)
        
        if "greenlight" in filename:
            print(re.search(r'Item 5.02.*?Item', clean, re.IGNORECASE))
            print(re.search(r'(resign|appoint|elect|depart).{0,100}(director|officer)', clean, re.IGNORECASE))

        if "i3verticals" in filename:
            print(re.search(r'Item 2.02.*?Item', clean, re.IGNORECASE))
            print(re.search(r'Item 7.01.*?Item', clean, re.IGNORECASE))

        if "rayonier" in filename:
            print(re.search(r'Item 5.02.*?Item', clean, re.IGNORECASE))

        if "lexeo" in filename:
            print(re.search(r'Item 5.02.*?Item', clean, re.IGNORECASE))
            
        if "curiosity" in filename:
            print(re.search(r'Item 8.01.*?Item', clean, re.IGNORECASE))

    except Exception as e:
        print(e)

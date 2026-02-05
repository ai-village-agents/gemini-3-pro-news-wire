import re

files = {
    "rayonier_8k.txt": "Rayonier",
    "lexeo_8k.txt": "Lexeo",
    "greenlight_8k.txt": "Greenlight",
    "i3verticals_8k.txt": "i3 Verticals",
    "curiosity_8k.txt": "CuriosityStream"
}

for filename, company in files.items():
    print(f"\n=== {company} ({filename}) ===")
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
        # Clean tags broadly
        clean = re.sub(r'<[^>]+>', ' ', content)
        clean = re.sub(r'\s+', ' ', clean)
        
        if company == "Rayonier":
            # Find 5.02 text
            match = re.search(r'Item 5.02(.*?)Item', clean, re.IGNORECASE)
            if match:
                print(match.group(1)[:1000])
        
        if company == "Lexeo":
            match = re.search(r'Item 5.02(.*?)Item', clean, re.IGNORECASE)
            if match:
                print(match.group(1)[:1000])

        if company == "Greenlight":
            match = re.search(r'Item 5.02(.*?)Item', clean, re.IGNORECASE)
            if match:
                print(match.group(1)[:1000])

        if company == "i3 Verticals":
            # Earnings numbers?
            match = re.search(r'Item 2.02(.*?)Item', clean, re.IGNORECASE)
            if match:
                print(match.group(1)[:1000])
            # Check for revenue/income figures in the whole text
            print(re.findall(r'$[\d\.]+\s*(?:million|billion)', clean)[:5])

        if company == "CuriosityStream":
            match = re.search(r'Item 8.01(.*?)Item', clean, re.IGNORECASE)
            if match:
                print(match.group(1)[:1000])

    except Exception as e:
        print(e)

import os
import re

def get_story_number(filename):
    match = re.search(r'story_(\d+)\.txt', filename)
    if match:
        return int(match.group(1))
    return 0

def main():
    # Get all story files
    files = [f for f in os.listdir('.') if f.startswith('story_') and f.endswith('.txt')]
    # Sort by story number descending (newest first)
    files.sort(key=get_story_number, reverse=True)

    with open('index.html', 'r') as f:
        content = f.read()

    # Find insertion point
    marker = '<div id="news-feed">'
    if marker not in content:
        print("Error: Marker not found")
        return

    insert_pos = content.find(marker) + len(marker)
    
    new_html = ""
    count = 0
    
    for filename in files:
        with open(filename, 'r') as f:
            story_content = f.read()
            
        # Check if this story is already in index.html
        # A simple check is to look for the title or a unique substring
        # Let's extract the title <h2>...</h2>
        title_match = re.search(r'<h2>(.*?)</h2>', story_content)
        if title_match:
            title = title_match.group(1)
            if title in content:
                print(f"Skipping {filename} (already present)")
                continue
        
        print(f"Queueing {filename} for insertion")
        new_html += "\n" + story_content
        count += 1

    if new_html:
        updated_content = content[:insert_pos] + new_html + content[insert_pos:]
        with open('index.html', 'w') as f:
            f.write(updated_content)
        print(f"Successfully inserted {count} new stories.")
    else:
        print("No new stories to insert.")

if __name__ == "__main__":
    main()

import os
import datetime

# Define the new content to be inserted
new_content = """
<div class="news-item breaking">
    <div class="news-meta">
        <span class="news-source">SEC EDGAR (8-K)</span>
        <span class="news-time">1:25 PM PT</span>
    </div>
    <div class="news-content">
        <h3>LifeVantage (LFVN) CEO Steven Fife to Retire; Reports Q2 Fiscal 2026 Results</h3>
        <p>Steven R. Fife has notified the Board of his decision to retire as President and CEO, effective April 2026. The company confirmed the departure is not due to any disagreement regarding operations or financial policies. Simultaneously, LifeVantage released its Q2 Fiscal 2026 financial results.</p>
    </div>
</div>
"""

# Path to the index.html file
file_path = 'index.html'

# Read the existing content
with open(file_path, 'r') as file:
    lines = file.readlines()

# Find the insertion point (after the "news-feed" div start)
insertion_index = -1
for i, line in enumerate(lines):
    if '<div id="news-feed">' in line:
        insertion_index = i + 1
        break

# Insert the new content if the insertion point was found
if insertion_index != -1:
    lines.insert(insertion_index, new_content)
    
    # Write the updated content back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)
    print("Successfully inserted LFVN story.")
else:
    print("Error: Could not find the insertion point in index.html.")

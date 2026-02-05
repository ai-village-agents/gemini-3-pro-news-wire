import os
import datetime

# Define the new content to be inserted
new_content = """
<div class="news-item breaking">
    <div class="news-meta">
        <span class="news-source">SEC EDGAR (8-K)</span>
        <span class="news-time">10:20 AM PT</span>
    </div>
    <div class="news-content">
        <h3>Target Corp (TGT) CEO Succession & Comp</h3>
        <p>Target finalizes compensation for incoming CEO Michael J. Fiddelke (effective Feb 1, 2026): .3M base, 200% target bonus, 2.1M LTI. Former CEO Brian Cornell transitions to Executive Chair (.12M salary, M LTI).</p>
    </div>
</div>

<div class="news-item breaking">
    <div class="news-meta">
        <span class="news-source">SEC EDGAR (8-K)</span>
        <span class="news-time">10:20 AM PT</span>
    </div>
    <div class="news-content">
        <h3>3M Co (MMM) Appoints RTX CFO to Board</h3>
        <p>3M elects Neil G. Mitchill, Jr. (CFO of RTX Corp) to Board of Directors, effective Feb 6, 2026. He will serve on the Audit and Nominating/Governance Committees.</p>
    </div>
</div>

<div class="news-item breaking">
    <div class="news-meta">
        <span class="news-source">SEC EDGAR (8-K)</span>
        <span class="news-time">10:20 AM PT</span>
    </div>
    <div class="news-content">
        <h3>Amphenol (APH) Chairman Retiring; CEO to Assume Role</h3>
        <p>Amphenol Chairman Martin H. Loeffler to retire in May 2026 after 50+ years with the company. CEO R. Adam Norwitt appointed to the additional role of Chairman effective upon the annual meeting.</p>
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
    print("Successfully inserted TGT, MMM, and APH stories.")
else:
    print("Error: Could not find the insertion point in index.html.")

import os

stories = [
    {
        "id": 97,
        "title": "Restructuring (POWI)",
        "content": """<div class="news-item breaking">
            <div class="timestamp">Just now</div>
            <h2>Power Integrations Cuts 7% of Workforce; Chair Steps Down</h2>
            <p><strong>Power Integrations (NASDAQ: POWI)</strong> has implemented a reduction in force affecting approximately <strong>7% of its global workforce</strong> to improve efficiency. The company expects to incur .5-.0 million in severance costs. Separately, <strong>Balu Balakrishnan</strong> has stepped down as Chairman, succeeded by <strong>Balakrishnan S. Iyer</strong>.</p>
            <span class="tag">Layoffs</span>
            <span class="tag">POWI</span>
            <span class="tag">Governance</span>
        </div>"""
    },
    {
        "id": 96,
        "title": "Layoffs/Buyback (MITK)",
        "content": """<div class="news-item breaking">
            <div class="timestamp">Just now</div>
            <h2>Mitek Systems Announces 7% Layoffs; Authorizes $50M Buyback</h2>
            <p><strong>Mitek Systems (NASDAQ: MITK)</strong> is reducing its workforce by <strong>7%</strong> as part of a restructuring plan (Item 2.05). Concurrently, the Board authorized a new <strong>$50 Million Share Repurchase Program</strong>. The company also appointed <strong>Eric Bell</strong> as Chief Accounting Officer and repaid its 2026 Convertible Notes.</p>
            <span class="tag">Layoffs</span>
            <span class="tag">MITK</span>
            <span class="tag">Buyback</span>
        </div>"""
    },
    {
        "id": 95,
        "title": "Change in Control/CEO (LEE)",
        "content": """<div class="news-item breaking">
            <div class="timestamp">Just now</div>
            <h2>Lee Enterprises Shakeup: CEO Retires, $50M Investment, Hoffmann Named Chair</h2>
            <p><strong>Lee Enterprises (NASDAQ: LEE)</strong> closed a <strong>$50 Million private placement</strong> led by <strong>David Hoffmann</strong>, who has been appointed Chairman of the Board. CEO <strong>Kevin Mowbray</strong> has retired; <strong>Nathan Bekke</strong> is named Interim CEO. CFO <strong>Timothy Millage</strong> also resigned, replaced by <strong>Josh Rinehults</strong> as Interim CFO.</p>
            <span class="tag">Management Change</span>
            <span class="tag">LEE</span>
            <span class="tag">M&A</span>
        </div>"""
    }
]

for story in stories:
    filename = f"story_{story['id']}.txt"
    with open(filename, "w") as f:
        f.write(story['content'])
    print(f"Created {filename}")

# Append to index.html manually
with open("gemini-3-pro-news-wire/index.html", "r") as f:
    content = f.read()

marker = '<div id="news-feed">'
if marker in content:
    insert_pos = content.find(marker) + len(marker)
    new_html = ""
    for story in stories:
        new_html += "\n" + story['content']
    
    final_html = content[:insert_pos] + new_html + content[insert_pos:]
    
    with open("gemini-3-pro-news-wire/index.html", "w") as f:
        f.write(final_html)
    print("Updated index.html")
else:
    print("Marker not found in index.html")

import os

stories = [
    {
        "id": 101,
        "title": "M&A Close (RYN)",
        "content": """<div class="news-item">
            <div class="timestamp">Just now</div>
            <h2>Rayonier Completes Merger with PotlatchDeltic</h2>
            <p><strong>Rayonier Inc. (NYSE: RYN)</strong> has completed its previously announced merger-of-equals with <strong>PotlatchDeltic</strong>. The transaction, effective Jan 30, 2026, creates a premier timberland REIT. The 8-K details the closing and subsequent leadership integration.</p>
            <span class="tag">Merger Complete</span>
            <span class="tag">RYN</span>
            <span class="tag">REIT</span>
        </div>"""
    },
    {
        "id": 100,
        "title": "Executive Change (CURI)",
        "content": """<div class="news-item">
            <div class="timestamp">Just now</div>
            <h2>CuriosityStream Appoints John Vilade as CCO</h2>
            <p><strong>CuriosityStream (NASDAQ: CURI)</strong> has appointed <strong>John T. Vilade</strong> as Chief Commercial Officer. Vilade, formerly of NBCUniversal and Hulu, will lead sales and business development, focusing on expanding AI licensing and global distribution partnerships.</p>
            <span class="tag">Executive Hire</span>
            <span class="tag">CURI</span>
            <span class="tag">Streaming</span>
        </div>"""
    },
    {
        "id": 99,
        "title": "Officer Resignation (GLRE)",
        "content": """<div class="news-item">
            <div class="timestamp">Just now</div>
            <h2>Greenlight Capital Re General Counsel to Resign</h2>
            <p><strong>Greenlight Capital Re (NASDAQ: GLRE)</strong> announced that General Counsel and CCO <strong>David Sigmon</strong> will resign effective May 1, 2026. The departure is not due to any disagreement with the company.</p>
            <span class="tag">Governance</span>
            <span class="tag">GLRE</span>
        </div>"""
    },
    {
        "id": 98,
        "title": "Transition (LXEO)",
        "content": """<div class="news-item">
            <div class="timestamp">Just now</div>
            <h2>Lexeo Therapeutics Head of Research Steps Down</h2>
            <p><strong>Lexeo Therapeutics (NASDAQ: LXEO)</strong> disclosed that <strong>Dr. Adler</strong>, Head of Research, has stepped down effective Feb 1, 2026. He will continue as a consultant through July 2026.</p>
            <span class="tag">Management Change</span>
            <span class="tag">LXEO</span>
            <span class="tag">Biotech</span>
        </div>"""
    }
]

for story in stories:
    filename = f"story_{story['id']}.txt"
    with open(filename, "w") as f:
        f.write(story['content'])
    print(f"Created {filename}")

# Append to index.html manually
with open("index.html", "r") as f:
    content = f.read()

marker = '<div id="news-feed">'
if marker in content:
    insert_pos = content.find(marker) + len(marker)
    new_html = ""
    for story in stories:
        new_html += "\n" + story['content']
    
    final_html = content[:insert_pos] + new_html + content[insert_pos:]
    
    with open("index.html", "w") as f:
        f.write(final_html)
    print("Updated index.html")
else:
    print("Marker not found in index.html")

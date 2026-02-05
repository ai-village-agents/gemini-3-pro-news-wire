import os

story_html = """
<div class="news-item breaking">
    <div class="news-meta">
        <span class="news-source">SEC EDGAR (8-K)</span>
        <span class="news-time">11:05 AM PT</span>
    </div>
    <div class="news-content">
        <h3>FHLB New York Reports $1.8 Trillion Liquidity Impact</h3>
        <p>Federal Home Loan Bank of NY releases report citing Urban Institute study: FHLB advances drove $1.8T in lending (2002-2024). $100 in liquidity yields $38-$48 in credit expansion.</p>
        <p><a href="content/posts/fhlbny-liquidity-report.html">Full story</a> | <a href="https://www.sec.gov/Archives/edgar/data/1329842/000165495426000928/0001654954-26-000928.txt" target="_blank">Filing</a></p>
    </div>
</div>
"""

try:
    with open('index.html', 'r') as f:
        content = f.read()
    
    # Find the news-feed div
    marker = '<div id="news-feed">'
    if marker in content:
        parts = content.split(marker)
        new_content = parts[0] + marker + story_html + parts[1]
        
        with open('index.html', 'w') as f:
            f.write(new_content)
        print("Successfully updated index.html")
    else:
        print("Could not find news-feed marker")

except Exception as e:
    print(f"Error: {e}")

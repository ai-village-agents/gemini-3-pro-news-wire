import requests
from datetime import datetime, timezone

def check_usgs():
    try:
        # USGS Significant Earthquakes past hour
        url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_hour.geojson"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data['features']:
                print(f"[{datetime.now()}] USGS ALERT: {len(data['features'])} moderate (M4.5+) earthquakes detected.")
                for feature in data['features']:
                    print(f" - {feature['properties']['title']} (Mag: {feature['properties']['mag']})")
                    print(f" - URL: {feature['properties']['url']}")
            else:
                print(f"[{datetime.now()}] USGS: No moderate (M4.5+) earthquakes in the past hour.")
    except Exception as e:
        print(f"USGS Error: {e}")

def check_noaa():
    try:
        # NOAA Space Weather - Current Space Weather Conditions
        # Note: NOAA SWPC JSON feeds are less standardized, using text scales often. 
        # Checking for Alerts/Warnings
        url = "https://services.swpc.noaa.gov/products/alerts.json"
        response = requests.get(url)
        if response.status_code == 200:
            alerts = response.json()
            if alerts:
                # Filter for very recent alerts (last 15 mins to catch breaking)
                # For now just print the latest to see format
                print(f"[{datetime.now()}] NOAA: {len(alerts)} active alerts.")
                if len(alerts) > 0:
                    latest = alerts[0]
                    message = latest.get('message', '').strip()
                    issue_time_raw = latest.get('issue_datetime') or latest.get('issue_time')

                    if not issue_time_raw and message:
                        # Try to scrape "Issue Time:" line from message body if needed.
                        for line in message.splitlines():
                            if line.lower().startswith("issue time:"):
                                issue_time_raw = line.split(":", 1)[1].strip()
                                break

                    parsed_time = None
                    if issue_time_raw:
                        for fmt in ("%Y-%m-%d %H:%M:%S.%f", "%Y-%m-%d %H:%M:%S", "%Y %b %d %H%M %Z"):
                            try:
                                parsed_time = datetime.strptime(issue_time_raw, fmt)
                                break
                            except ValueError:
                                continue

                    is_recent = False
                    if parsed_time:
                        if parsed_time.tzinfo is None:
                            parsed_time = parsed_time.replace(tzinfo=timezone.utc)
                        now_utc = datetime.now(timezone.utc)
                        delta_hours = abs((now_utc - parsed_time).total_seconds()) / 3600
                        is_recent = delta_hours <= 2
                        readable_time = parsed_time.isoformat()
                    else:
                        readable_time = "Unknown"

                    print(" - LATEST NOAA ALERT")
                    print(f"   Issue Time (UTC): {readable_time}")
                    if parsed_time:
                        recency_status = "within last 2 hours" if is_recent else "older than 2 hours"
                        print(f"   Recency: {recency_status}")
                    print(f"   Message: {message if message else 'No message text available.'}")
            else:
                print(f"[{datetime.now()}] NOAA: No active alerts.")
    except Exception as e:
        print(f"NOAA Error: {e}")

def check_cisa():
    try:
        timestamp = datetime.now()
        kev_url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
        response = requests.get(kev_url, timeout=10)

        if response.status_code == 200:
            data = response.json()
            vulns = data.get("vulnerabilities", [])
            if vulns:
                sorted_vulns = sorted(vulns, key=lambda v: v.get("dateAdded", ""), reverse=True)
                latest = sorted_vulns[:5]
                print(f"[{timestamp}] CISA Known Exploited Vulnerabilities (latest 3)")
                for vuln in latest:
                    date_added = vuln.get("dateAdded", "Unknown")
                    cve = vuln.get("cveID", "No CVE")
                    desc = vuln.get("shortDescription", "No description")
                    print(f" - {date_added} | {cve} | {desc}")
                return
            else:
                print(f"[{timestamp}] CISA: KEV feed returned no vulnerabilities.")
        else:
            print(f"[{timestamp}] CISA: KEV feed HTTP {response.status_code}. Trying summary page.")
    except Exception as e:
        print(f"[{datetime.now()}] CISA KEV feed error: {e}. Trying summary page.")

    # Fallback: grab a snippet from the current activity summary page
    try:
        summary_url = "https://www.cisa.gov/uscert/ncas/current-activity/summary"
        resp = requests.get(summary_url, timeout=10)
        if resp.status_code == 200:
            snippet = resp.text[:500].replace("\n", " ").strip()
            print(f"[{datetime.now()}] CISA Current Activity snippet (first 500 chars):")
            print(f" {snippet}")
        else:
            print(f"[{datetime.now()}] CISA summary fallback error: HTTP {resp.status_code}")
    except Exception as e:
        print(f"[{datetime.now()}] CISA summary fallback error: {e}")

def check_fda():
    try:
        url = "https://api.fda.gov/food/enforcement.json?limit=1&sort=recall_initiation_date:desc"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])
            if results:
                latest = results[0]
                recall_date = latest.get("recall_initiation_date", "Unknown")
                product = latest.get("product_description", "No description")
                reason = latest.get("reason_for_recall", "No reason provided")
                print(f"[{datetime.now()}] FDA Latest Food Recall")
                print(f" - Recall Initiation Date: {recall_date}")
                print(f" - Product: {product}")
                print(f" - Reason: {reason}")
            else:
                print(f"[{datetime.now()}] FDA: No recall data returned.")
        else:
            print(f"[{datetime.now()}] FDA Error: HTTP {response.status_code}")
    except Exception as e:
        print(f"FDA Error: {e}")

def check_sec_halts():
    try:
        url = "https://www.nyse.com/api/trade-halts/current"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            trade_halts = data.get("results", {}).get("tradeHalts", []) or data.get("data", [])
            if trade_halts:
                print(f"[{datetime.now()}] SEC/NYSE Trade Halts: {len(trade_halts)} currently listed.")
                for halt in trade_halts[:3]:
                    halt_date = halt.get("formatedHaltDate") or halt.get("haltDate") or "Unknown date"
                    halt_time = halt.get("formatedHaltTime") or halt.get("haltTime") or "Unknown time"
                    symbol = halt.get("symbol", "Unknown symbol")
                    reason = halt.get("reason", "No reason provided")
                    print(f" - {halt_date} {halt_time} | {symbol} | {reason}")
                return
            else:
                print(f"[{datetime.now()}] SEC/NYSE Trade Halts: No active halts reported.")
        else:
            print(f"[{datetime.now()}] SEC/NYSE Trade Halts error: HTTP {response.status_code}")
    except Exception as e:
        print(f"SEC/NYSE Trade Halts Error: {e}")

if __name__ == "__main__":
    print("Starting Day 308 Global Monitor...\n")
    check_usgs()
    print("-" * 60)
    check_noaa()
    print("-" * 60)
    check_cisa()
    print("-" * 60)
    check_fda()
    print("-" * 60)
    check_sec_halts()

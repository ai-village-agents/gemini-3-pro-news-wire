import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

# Shared headers for all requests
HEADERS = {"User-Agent": "Mozilla/5.0"}


def current_ts():
    return datetime.now(timezone.utc)


def check_usgs():
    try:
        url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_hour.geojson"
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data["features"]:
                print(f"[{current_ts()}] USGS ALERT: {len(data['features'])} moderate (M4.5+) earthquakes detected.")
                for feature in data["features"]:
                    props = feature.get("properties", {})
                    print(f" - {props.get('title', 'No title')} (Mag: {props.get('mag')})")
                    print(f"   URL: {props.get('url', '')}")
            else:
                print(f"[{current_ts()}] USGS: No moderate (M4.5+) earthquakes in the past hour.")
        else:
            print(f"[{current_ts()}] USGS error: HTTP {response.status_code}")
    except Exception as e:
        print(f"USGS Error: {e}")


def check_noaa():
    try:
        url = "https://services.swpc.noaa.gov/products/alerts.json"
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code == 200:
            alerts = response.json()
            if alerts:
                print(f"[{current_ts()}] NOAA: {len(alerts)} active alerts.")
                latest = alerts[0]
                message = latest.get("message", "").strip()
                issue_time_raw = latest.get("issue_datetime") or latest.get("issue_time")

                if not issue_time_raw and message:
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
                print(f"[{current_ts()}] NOAA: No active alerts.")
        else:
            print(f"[{current_ts()}] NOAA error: HTTP {response.status_code}")
    except Exception as e:
        print(f"NOAA Error: {e}")


def check_cisa():
    try:
        timestamp = current_ts()
        kev_url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
        response = requests.get(kev_url, headers=HEADERS, timeout=10)

        if response.status_code == 200:
            data = response.json()
            vulns = data.get("vulnerabilities", [])
            if vulns:
                sorted_vulns = sorted(vulns, key=lambda v: v.get("dateAdded", ""), reverse=True)
                latest = sorted_vulns[:3]
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
        print(f"[{current_ts()}] CISA KEV feed error: {e}. Trying summary page.")

    try:
        summary_url = "https://www.cisa.gov/uscert/ncas/current-activity/summary"
        resp = requests.get(summary_url, headers=HEADERS, timeout=10)
        timestamp = current_ts()
        if resp.status_code == 200:
            snippet = resp.text[:500].replace("\n", " ").strip()
            print(f"[{timestamp}] CISA Current Activity snippet (first 500 chars):")
            print(f" {snippet}")
        else:
            print(f"[{timestamp}] CISA summary fallback error: HTTP {resp.status_code}")
    except Exception as e:
        print(f"[{current_ts()}] CISA summary fallback error: {e}")


def check_sec_halts():
    try:
        url = "https://www.nyse.com/api/trade-halts/current"
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code == 200:
            data = response.json()
            trade_halts = data.get("results", {}).get("tradeHalts", []) or data.get("data", [])
            if trade_halts:
                print(f"[{current_ts()}] SEC/NYSE Trade Halts: {len(trade_halts)} currently listed.")
                for halt in trade_halts[:3]:
                    halt_date = halt.get("formatedHaltDate") or halt.get("haltDate") or "Unknown date"
                    halt_time = halt.get("formatedHaltTime") or halt.get("haltTime") or "Unknown time"
                    symbol = halt.get("symbol", "Unknown symbol")
                    reason = halt.get("reason", "No reason provided")
                    print(f" - {halt_date} {halt_time} | {symbol} | {reason}")
                return
            else:
                print(f"[{current_ts()}] SEC/NYSE Trade Halts: No active halts reported.")
        else:
            print(f"[{current_ts()}] SEC/NYSE Trade Halts error: HTTP {response.status_code}")
    except Exception as e:
        print(f"SEC/NYSE Trade Halts Error: {e}")


def check_uk_government():
    try:
        url = "https://www.gov.uk/api/search.json?count=3&order=-public_timestamp&filter_content_store_document_type=news_story"
        resp = requests.get(url, headers=HEADERS, timeout=10)
        timestamp = current_ts()
        if resp.status_code == 200:
            data = resp.json()
            results = data.get("results", [])
            if results:
                print(f"[{timestamp}] UK Government News (latest 3)")
                for item in results[:3]:
                    title = item.get("title", "No title")
                    published = item.get("public_timestamp", "Unknown time")
                    link = item.get("link", "")
                    full_link = f"https://www.gov.uk{link}" if link and link.startswith("/") else link
                    print(f" - {published} | {title}")
                    print(f"   {full_link}")
            else:
                print(f"[{timestamp}] UK Government: No news items returned.")
        else:
            print(f"[{timestamp}] UK Government error: HTTP {resp.status_code}")
    except Exception as e:
        print(f"UK Government Error: {e}")


def check_investing_rss():
    try:
        url = "https://www.investing.com/rss/news.rss"
        resp = requests.get(url, headers=HEADERS, timeout=10)
        timestamp = current_ts()
        if resp.status_code == 200:
            try:
                root = ET.fromstring(resp.content)
            except ET.ParseError as pe:
                print(f"[{timestamp}] Investing.com RSS parse error: {pe}")
                return

            channel = root.find("channel")
            items = channel.findall("item") if channel is not None else []
            print(f"[{timestamp}] Investing.com News (top 3)")
            if not items:
                print(" - No items found.")
                return

            for item in items[:3]:
                title = item.findtext("title", default="No title")
                pub_date = item.findtext("pubDate", default="Unknown date")
                link = item.findtext("link", default="")
                print(f" - {pub_date} | {title}")
                print(f"   {link}")
        else:
            print(f"[{timestamp}] Investing.com RSS error: HTTP {resp.status_code}")
    except Exception as e:
        print(f"Investing.com RSS Error: {e}")


def check_bank_of_england():
    try:
        url = "https://www.bankofengland.co.uk/rss/news"
        resp = requests.get(url, headers=HEADERS, timeout=10)
        timestamp = current_ts()
        if resp.status_code == 200:
            root = ET.fromstring(resp.content)
            channel = root.find("channel")
            items = channel.findall("item") if channel is not None else []
            print(f"[{timestamp}] Bank of England News (latest 3)")
            if not items:
                print(" - No items found.")
                return

            for item in items[:3]:
                title = item.findtext("title", default="No title")
                pub_date = item.findtext("pubDate", default="Unknown date")
                link = item.findtext("link", default="")
                print(f" - {pub_date} | {title}")
                print(f"   {link}")
        else:
            print(f"[{timestamp}] Bank of England error: HTTP {resp.status_code}")
    except Exception as e:
        print(f"Bank of England Error: {e}")


if __name__ == "__main__":
    print("Starting Day 309 Global Monitor...\n")
    check_usgs()
    print("-" * 60)
    check_noaa()
    print("-" * 60)
    check_cisa()
    print("-" * 60)
    check_sec_halts()
    print("-" * 60)
    check_uk_government()
    print("-" * 60)
    check_investing_rss()
    print("-" * 60)
    check_bank_of_england()

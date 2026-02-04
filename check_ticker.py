import argparse
import re
from html import unescape

import requests

try:
    from bs4 import BeautifulSoup  # type: ignore
except ImportError:
    BeautifulSoup = None

# Browser-like headers help some sites serve the full page instead of a bot block.
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

KEYWORDS = ("webster", "wbs")


def fetch_html(url: str) -> str:
    response = requests.get(url, headers=HEADERS, timeout=15)
    response.raise_for_status()
    return response.text


def clean_text(text: str) -> str:
    return " ".join(unescape(text).split())


def bs4_headlines(html: str, selectors: list[str]) -> set[str]:
    soup = BeautifulSoup(html, "html.parser")
    headlines: set[str] = set()

    for selector in selectors:
        for node in soup.select(selector):
            text = clean_text(node.get_text(" ", strip=True))
            if text:
                headlines.add(text)

    if not headlines:
        for tag in soup.find_all(["h1", "h2", "h3", "h4"]):
            text = clean_text(tag.get_text(" ", strip=True))
            if text:
                headlines.add(text)

    return headlines


def regex_headlines(html: str) -> set[str]:
    headlines: set[str] = set()
    for match in re.findall(r"<h[1-6][^>]*>(.*?)</h[1-6]>", html, flags=re.I | re.S):
        text = clean_text(re.sub(r"<[^>]+>", " ", match))
        if text:
            headlines.add(text)

    for match in re.findall(r"<a[^>]*>([^<]{5,140})</a>", html, flags=re.I | re.S):
        text = clean_text(match)
        if text:
            headlines.add(text)

    return headlines


def extract_headlines(html: str, selectors: list[str]) -> set[str]:
    if BeautifulSoup:
        return bs4_headlines(html, selectors)
    return regex_headlines(html)


def filter_for_keywords(headlines: set[str]) -> list[str]:
    return [
        h
        for h in headlines
        if any(keyword in h.lower() for keyword in KEYWORDS)
    ]


def check_source(name: str, url: str, selectors: list[str]) -> None:
    print(f"\n{name}: {url}")
    try:
        html = fetch_html(url)
        headlines = extract_headlines(html, selectors)
        matches = filter_for_keywords(headlines)

        if matches:
            for headline in sorted(matches):
                print(f"- {headline}")
        else:
            print("- No matching headlines found.")
    except Exception as exc:  # pragma: no cover - defensive logging
        print(f"- Error fetching/parsing {name}: {exc}")


def parse_args() -> str:
    parser = argparse.ArgumentParser(description="Check headlines for a ticker symbol.")
    parser.add_argument(
        "ticker",
        nargs="?",
        default="WBS",
        help="Ticker symbol to query (default: WBS)",
    )
    args = parser.parse_args()
    return args.ticker.upper()


def main() -> None:
    ticker = parse_args()
    sources = [
        (
            "Yahoo Finance",
            f"https://finance.yahoo.com/quote/{ticker}",
            [
                "h1",
                "h2",
                "h3",
                "h4",
                "a.js-content-viewer",
                "a[title]",
                "a[aria-label]",
            ],
        ),
        (
            "CNBC",
            f"https://www.cnbc.com/quotes/{ticker}",
            [
                "h1",
                "h2",
                "h3",
                ".Card-title",
                "a.Card-title",
                "a[title]",
                "a[aria-label]",
            ],
        ),
    ]

    for name, url, selectors in sources:
        check_source(name, url, selectors)


if __name__ == "__main__":
    main()

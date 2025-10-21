# Polite crawler with visible text extraction
!pip install requests beautifulsoup4 --quiet

import requests
from urllib.parse import urljoin, urlparse
import urllib.robotparser
from bs4 import BeautifulSoup
import time, re

USER_AGENT = 'EduCrawler/1.0 (+your-email@example.com)'
HEADERS = {'User-Agent': USER_AGENT}
RATE = 1.0  # seconds between requests
MAX_LINKS = 10

seed = 'https://smcolab2007-dotcom.github.io/demo-crawler-site/'  # <-- replace with GitHub Pages URL

# robots.txt check
rp = urllib.robotparser.RobotFileParser()
rp.set_url(urljoin(seed, 'robots.txt'))
rp.read()

def allowed(url):
    return rp.can_fetch(USER_AGENT, url)

def fetch(url):
    print("\nGET:", url)
    r = requests.get(url, headers=HEADERS, timeout=10)
    r.raise_for_status()
    return r.text

def extract_links_and_text(html, base):
    soup = BeautifulSoup(html, "html.parser")
    title = (soup.title.string or "").strip()
    # Extract visible text (skip scripts, styles, hidden tags)
    for s in soup(["script", "style", "noscript"]):
        s.decompose()
    text = " ".join(soup.stripped_strings)
    # Extract links (same host only)
    links = set()
    for a in soup.find_all("a", href=True):
        href = urljoin(base, a["href"])
        if urlparse(href).netloc == urlparse(base).netloc:
            links.add(href)
    return title, text, links

seen, queue, results = set(), [seed], {}

while queue and len(seen) < MAX_LINKS:
    url = queue.pop(0)
    if url in seen or not allowed(url):
        continue
    try:
        html = fetch(url)
        title, text, links = extract_links_and_text(html, url)
        results[url] = {"title": title, "text": text[:250] + "..."}  # limit output for brevity
        queue.extend(links - seen)
    except Exception as e:
        results[url] = {"title": "ERROR", "text": str(e)}
    seen.add(url)
    time.sleep(RATE)

print("\nCrawl results (title + body preview):")
for u, data in results.items():
    print(f"\n{u}\nTitle: {data['title']}\nText: {data['text']}")

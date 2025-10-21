# Polite crawler (paste into Colab)
!pip install requests beautifulsoup4 --quiet

import requests
from urllib.parse import urljoin, urlparse
import urllib.robotparser
from bs4 import BeautifulSoup
import time

USER_AGENT = 'EduCrawler/1.0 (+your-email@example.com)'
HEADERS = {'User-Agent': USER_AGENT}
RATE = 1.0  # seconds between requests
MAX_LINKS = 30

seed = 'repo:smcolab2007-dotcom/demo-crawler-site/'  # <-- GitHub Pages URL

# robots.txt check
rp = urllib.robotparser.RobotFileParser()
rp.set_url(urljoin(seed, 'robots.txt'))
rp.read()

def allowed(url):
    try:
        return rp.can_fetch(USER_AGENT, url)
    except Exception:
        return False

def fetch(url):
    print('GET', url)
    r = requests.get(url, headers=HEADERS, timeout=10)
    r.raise_for_status()
    return r.text

def extract_links(html, base):
    soup = BeautifulSoup(html, 'html.parser')
    title = (soup.title.string or '').strip()
    links = set()
    for a in soup.find_all('a', href=True):
        href = urljoin(base, a['href'])
        parsed_seed = urlparse(seed)
        parsed_href = urlparse(href)
        # only keep links within same host
        if parsed_href.netloc == parsed_seed.netloc:
            links.add(href.split('#')[0])
    return title, links

# Crawl seed and first-level links
if not allowed(seed):
    raise SystemExit('Crawling disallowed by robots.txt for seed URL. Change seed or robots.txt.')

seen = set()
queue = [seed]
results = {}

while queue and len(seen) < MAX_LINKS:
    url = queue.pop(0)
    if url in seen: continue
    if not allowed(url):
        print('Skipping (robots):', url)
        seen.add(url)
        continue
    try:
        html = fetch(url)
        title, links = extract_links(html, url)
        results[url] = title
        for L in sorted(links):
            if L not in seen and L not in queue and len(seen) + len(queue) < MAX_LINKS:
                queue.append(L)
    except Exception as e:
        results[url] = f'ERROR: {e}'
    seen.add(url)
    time.sleep(RATE)

print('\nCrawl results:')
for u, t in results.items():
    print('-', u, '->', t)

# Note: This crawler only fetches public HTML. It will not bypass logins or access protected endpoints.

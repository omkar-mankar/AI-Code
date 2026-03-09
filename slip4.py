#1A. Develop a Web Crawler to Fetch and Index Web Pages
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

visited = set()
to_visit = ["https://example.com"]

index = {}

while to_visit:
    url = to_visit.pop(0)

    if url in visited:
        continue

    visited.add(url)

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        text = soup.get_text()
        index[url] = text

        for link in soup.find_all("a", href=True):
            new_url = urljoin(url, link["href"])

            if new_url not in visited:
                to_visit.append(new_url)

    except:
        pass

print("Indexed Pages:", len(index))

#1B. Handle Challenges such as robots.txt, Dynamic Content, and Crawling Delays
import time
from bs4 import BeautifulSoup

robots_txt = """
User-agent: *
Disallow: /private
"""

url = "/home"

if "Disallow: /" in robots_txt and url.startswith("/"):
    print("Crawling not allowed by robots.txt")
else:
    html = """
    <html>
    <head><title>Sample Page</title></head>
    <body>
        <a href="page1.html">Page 1</a>
        <a href="page2.html">Page 2</a>
        <a href="page3.html">Page 3</a>
    </body>
    </html>
    """

    soup = BeautifulSoup(html, "html.parser")

    print("Page Title:", soup.title.string)

    print("\nLinks Found:")
    for link in soup.find_all("a"):
        print(link.get("href"))

    time.sleep(2)
    print("\nCrawling delay applied")

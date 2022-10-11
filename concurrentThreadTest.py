import requests
from bs4 import BeautifulSoup
import time
import concurrent.futures

MAX_THREADS = 30
BASE_URL = "https://news.ycombinator.com/"
STORY_LINKS = []

for i in range(10):
    resp = requests.get(f"{BASE_URL}news?p={i}")
    soup = BeautifulSoup(resp.content, "html.parser")
    stories = soup.find_all("a")
    links = [x["href"] for x in stories if "http" in x["href"]]
    STORY_LINKS += links
    time.sleep(0.25)


def download_url(url):
    print(url)
    resp = requests.get(url)
    title = ''.join(x for x in url if x.isalpha()) + "html"

    with open(title, "wb") as fh:
        fh.write(resp.content)

    time.sleep(0.25)


def download_stories(story_urls):
    threads = min(MAX_THREADS, len(story_urls))
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(download_url, story_urls)


def main(story_urls):
    t0 = time.time()
    download_stories(story_urls)
    t1 = time.time()
    print(f"{t1 - t0} seconds to download {len(story_urls)} stories.")

main(STORY_LINKS[:5])


import requests
import time
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urljoin
BASE_URL = "https://books.toscrape.com/catalogue/page-1.html"

CACHE_DIR = Path("cache")
CACHE_FILE = CACHE_DIR / "catalogue-page-1.html"

HEADERS = {
    "User-Agent": "FlyRankInternship A9/1.0 (+https://github.com/abhisek0407/FlyRank_AI)"
}

TIMEOUT = 10


def fetch_and_cache():

    # Check whether cached HTML already exists
    if CACHE_FILE.exists():

        html = CACHE_FILE.read_text(encoding="utf-8")

        print(f"CACHE: {CACHE_FILE}")
        print(f"Response size: {len(html.encode('utf-8'))} bytes")

        return html

    # Fetch from website
    print(f"FETCH: {BASE_URL}")

    response = requests.get(
        BASE_URL,
        headers=HEADERS,
        timeout=TIMEOUT
    )

    # Only HTTP 200 is considered successful
    if response.status_code != 200:
        raise RuntimeError(
            f"Fetch failed. HTTP status: {response.status_code}"
        )

    html = response.text

    # Create cache directory
    CACHE_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    # Save HTML
    CACHE_FILE.write_text(
        html,
        encoding="utf-8"
    )

    print(f"Status: {response.status_code}")
    print(f"Response size: {len(response.content)} bytes")
    print(f"Saved: {CACHE_FILE}")

    return html

def stage2():
    page_url=BASE_URL
    html = CACHE_FILE.read_text(encoding="utf-8")
    book_urls=[]
    catalouge_pages=0
    while catalouge_pages<3:
        catalouge_pages+=1
        print(f"\nProcessing catalogue page {catalouge_pages}")
        print(f"URL: {page_url}")
        soup=BeautifulSoup(html, "html.parser")
        links=soup.select("article.product_pod div a")
        print(f"Books found: {len(links)}")
        for link in links:
            href=link.get("href")
            if href:
                absolute_url=urljoin(page_url,href)
                book_urls.append(absolute_url)

        if catalouge_pages==3:
            break
        next_page=soup.select_one("li.next a")

        if next_page is None:
            raise RuntimeError(
                "Next page link not found"
            )
        next_url=urljoin(page_url,next_page.get("href"))
        time.sleep(0.5)
        print(f"FETCH: {next_url}")

        response = requests.get(
            next_url,
            headers=HEADERS,
            timeout=TIMEOUT
        )
        if response.status_code != 200:
            raise RuntimeError(
            f"Fetch failed. HTTP status: "
            f"{response.status_code}"
        )

        html = response.text
        cache_file=CACHE_DIR/f"catalogue-page-{catalouge_pages+1}.html"
        cache_file.write_text(html,encoding="utf-8")
        print(
        f"Saved: {cache_file}"
        )
        page_url = next_url
    unique_urls = list(
        dict.fromkeys(book_urls)
    )
    print("\n-----------------------------")
    print("STAGE 2 CHECKPOINT")
    print("-----------------------------")

    print(
        f"catalogue_pages={catalouge_pages}"
    )

    print(
        f"discovered={len(book_urls)}"
    )

    print(
        f"unique_urls={len(unique_urls)}"
   )

    return unique_urls



if __name__ == "__main__":
    fetch_and_cache()
    stage2()

    
    
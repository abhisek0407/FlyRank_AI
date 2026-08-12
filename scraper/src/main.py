# import requests
# from pathlib import Path
# URL="https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"

# CACHE_DIR=Path("cache")
# CACHE_FILE=CACHE_DIR/"catalogue-page-1.html"

# HEADERS={
#     "user-Agent":"FlyRankInternship A9/1.0 (+https://github.com/abhisek0407/FlyRank_AI)"
# }
# TIMEOUT=10

# def fetch_and_cache():
#     if CACHE_FILE.exists():
#         html=CACHE_FILE.read_text(encoding="utf-8")
#         print(f"CACHE: {CACHE_FILE}")
#         print(f"Response size: {len(html.encode('utf-8'))} bytes")

#         return html
#     print(f"FETCH: {URL}")

#     response=requests.get(
#         URL,
#         headers=HEADERS,
#         timeout=TIMEOUT
#     )

#     if response.status_code!=200:
#         raise RuntimeError(
#             f"Fetch failed. HTTP status: {response.status_code}"
#         )
#     html=response.text
#     CACHE_DIR.mkdir(parents=True,exist_ok=True)

#     CACHE_FILE.write_text(
#         html,
#         encoding="utf-8"
#     )
#     print(f"Status: {response.status_code}")
#     print(f"Response size: {len(response.content)} bytes")
#     print(f"Saved: {CACHE_FILE}")

#     return html

# import requests
# from pathlib import Path
# URL="https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"

# CACHE_DIR=Path("cache")
# CACHE_FILE=CACHE_DIR/"catalogue-page-1.html"

# HEADERS={
#     "user-Agent":"FlyRankInternship A9/1.0 (+https://github.com/abhisek0407/FlyRank_AI)"
# }
# TIMEOUT=10

# def fetch_and_cache():
#     if CACHE_FILE.exists():
#         html=CACHE_FILE.read_text(encoding="utf-8")
#         print(f"CACHE: {CACHE_FILE}")
#         print(f"Response size: {len(html.encode('utf-8'))} bytes")

#         return html
#     print(f"FETCH: {URL}")

#     response=requests.get(
#         URL,
#         headers=HEADERS,
#         timeout=TIMEOUT
#     )

#     if response.status_code!=200:
#         raise RuntimeError(
#             f"Fetch failed. HTTP status: {response.status_code}"
#         )
#     html=response.text
#     CACHE_DIR.mkdir(parents=True,exist_ok=True)

#     CACHE_FILE.write_text(
#         html,
#         encoding="utf-8"
#     )
#     print(f"Status: {response.status_code}")
#     print(f"Response size: {len(response.content)} bytes")
#     print(f"Saved: {CACHE_FILE}")

#     return html

# if __name__=="_main_":
#     fetch_and_cache()

import requests
from pathlib import Path

URL = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"

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
    print(f"FETCH: {URL}")

    response = requests.get(
        URL,
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


if __name__ == "__main__":
    fetch_and_cache()
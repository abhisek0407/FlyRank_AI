
import requests
import time
import json
from pydantic import BaseModel,HttpUrl
from typing import Optional
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from datetime import datetime,timezone
BASE_URL = "https://books.toscrape.com/catalogue/page-1.html"

CACHE_DIR = Path("cache")
CACHE_FILE = CACHE_DIR / "catalogue-page-1.html"

HEADERS = {
    "User-Agent": "FlyRankInternship A9/1.0 (+https://github.com/abhisek0407/FlyRank_AI)"
}

TIMEOUT = 10
REQUEST_DELAY=0.5

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
                book_urls.append({
                    "product_url":absolute_url,
                    "source_page":page_url
                })

        if catalouge_pages==3:
            break
        next_page=soup.select_one("li.next a")

        if next_page is None:
            raise RuntimeError(
                "Next page link not found"
            )
        next_url=urljoin(page_url,next_page.get("href"))
        time.sleep(REQUEST_DELAY)
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
    unique_records = []
    seen_urls = set()

    for record in book_urls:
        if record["product_url"] not in seen_urls:
            seen_urls.add(record["product_url"])
            unique_records.append(record)
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
        f"unique_urls={len(unique_records)}"
   )

    return unique_records


def fetch_book_page(
    product_url,
    cache_file
):

   

    if cache_file.exists():

        html = cache_file.read_text(
            encoding="utf-8"
        )

        print(
            f"CACHE: {cache_file}"
        )

        print(
            f"Response size: "
            f"{len(html.encode('utf-8'))} bytes"
        )

        return html

   

    print(
        f"FETCH: {product_url}"
    )

    response = requests.get(
        product_url,
        headers=HEADERS,
        timeout=TIMEOUT
    )

    # Only HTTP 200 is accepted
    if response.status_code != 200:

        raise RuntimeError(
            f"Fetch failed for {product_url}. "
            f"HTTP status: {response.status_code}"
        )

    html = response.text


    CACHE_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    cache_file.write_text(
        html,
        encoding="utf-8"
    )

    print(
        f"Saved: {cache_file}"
    )

    print(
        f"Response size: "
        f"{len(response.content)} bytes"
    )

    return html

def stage3(book_records):
    raw_records=[]
    total_books=len(book_records)
    print("\n=============================")
    print("STAGE 3: EXTRACT BOOK DETAILS")
    print("=============================")
    for index,book_record in enumerate(book_records,start=1):
        product_url = book_record[
            "product_url"
        ]

        source_page = book_record[
            "source_page"
        ]

        print(
            f"\nProcessing book "
            f"{index}/{total_books}"
        )


        cache_file = (
            CACHE_DIR /
            f"book-{index}.html"
        )


        html = fetch_book_page(
            product_url,
            cache_file
        )
        soup=BeautifulSoup(html,"html.parser")
        product = soup.select_one(
            "article.product_page"
        )

        if product is None:
            raise RuntimeError(
                f"Product area not found: "
                f"{product_url}"
            )
        title_element = product.select_one(
            "h1"
        )

        title = (
            title_element.get_text(
                strip=True
            )
            if title_element
            else None
        )

        # ----------------------------------------------------
        # Price
        # ----------------------------------------------------

        price_element = product.select_one(
            ".price_color"
        )

        price_text = (
            price_element.get_text(
                " ",
                strip=True
            )
            if price_element
            else None
        )

        # ----------------------------------------------------
        # Availability
        # ----------------------------------------------------

        availability_element = product.select_one(
            ".availability"
        )

        availability_text = (
            availability_element.get_text(
                " ",
                strip=True
            )
            if availability_element
            else None
        )

        # ----------------------------------------------------
        # Rating
        # ----------------------------------------------------

        rating_element = product.select_one(
            "p.star-rating"
        )

        rating_text = None

        if rating_element:

            classes = rating_element.get(
                "class",
                []
            )

            rating_names = {
                "One",
                "Two",
                "Three",
                "Four",
                "Five"
            }

            for class_name in classes:

                if class_name in rating_names:

                    rating_text = class_name
                    break

        # ----------------------------------------------------
        # Description
        # ----------------------------------------------------

        description = None

        description_heading = product.select_one(
            "#product_description"
        )

        if description_heading:

            description_element = (
                description_heading.find_next_sibling(
                    "p"
                )
            )

            if description_element:

                description = (
                    description_element.get_text(
                        " ",
                        strip=True
                    )
                )

        # ----------------------------------------------------
        # Timestamp
        # ----------------------------------------------------

        fetched_at = (
            datetime.now(timezone.utc)
            .isoformat()
            .replace("+00:00", "Z")
        )

        # ----------------------------------------------------
        # Raw record
        # ----------------------------------------------------

        record = {
            "title": title,
            "product_url": product_url,
            "price_text": price_text,
            "availability_text": availability_text,
            "rating_text": rating_text,
            "description": description,
            "source_page": source_page,
            "fetched_at": fetched_at
        }

        raw_records.append(record)

        # ----------------------------------------------------
        # Delay before next network request
        # ----------------------------------------------------

        time.sleep(REQUEST_DELAY)

    # ========================================================
    # STAGE 3 CHECKPOINT
    # ========================================================

    print("\n=============================")
    print("STAGE 3 CHECKPOINT")
    print("=============================")

    print(
        f"records={len(raw_records)}"
    )

    print(
        f"successful_records="
        f"{sum(1 for r in raw_records if r['title'])}"
    )

    print(
        "\nComplete raw record:"
    )

    if raw_records:

        print(
            json.dumps(
                raw_records[0],
                indent=2,
                ensure_ascii=False
            )
        )

    return raw_records
class BookRecord(BaseModel):
    title: str
    product_url: HttpUrl
    price_text: str
    price_gbp: float
    availability_text: str
    rating_text: str
    description: Optional[str] = None
    source_page: HttpUrl
    fetched_at: str
def normalize_price(price_text):
    if not price_text:
        raise ValueError("Price_text is missing")
    cleaned_price=(
        price_text
        .replace("Â£", "")
        .replace("£", "")
        .strip()
    )
    try:
        return float(cleaned_price)
    except ValueError:
        raise ValueError(
            f"Invalid price_text:{price_text}"
        )
def stage4(raw_records):
    print("\n=============================")
    print("STAGE 4: VALIDATE NORMALIZED RECORDS")
    print("=============================")
    output_dir=Path("output")
    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )
    books_file=output_dir/"books.json"
    errors_file=output_dir/"errors.json"

    valid_records=[]
    errors=[]

    seen_urls=set()
    for record in raw_records:
        product_url=record.get("product_url")
        try:
            if product_url in seen_urls:
                continue
            seen_urls.add(product_url)
            price_gbp=normalize_price(record.get("price_text"))

            normalized_record = {
                "title": record.get("title"),
                "product_url": product_url,
                "price_text": record.get("price_text"),
                "price_gbp": price_gbp,
                "availability_text": record.get(
                    "availability_text"
                ),
                "rating_text": record.get(
                    "rating_text"
                ),
                "description": record.get(
                    "description"
                ),
                "source_page": record.get(
                    "source_page"
                ),
                "fetched_at": record.get(
                    "fetched_at"
                )
            }

            validate_record=BookRecord(**normalized_record)
            valid_records.append(validate_record.model_dump(mode="json"))
        except Exception as error:
            errors.append({
                "product_url":product_url,
                "reason":str(error)
            })

    with open(books_file,"w",encoding="utf-8") as file:
        json.dump(
            valid_records,
            file,
            indent=2,
            ensure_ascii=False
        )
    with open(errors_file,"w",encoding="utf-8") as file:
        json.dump(
            errors,
            file,
            indent=2,
            ensure_ascii=False
        )
    print("\n=============================")
    print("STAGE 4 CHECKPOINT")
    print("=============================")

    print(
        f"input_records={len(raw_records)}"
    )

    print(
        f"valid_records={len(valid_records)}"
    )

    print(
        f"errors={len(errors)}"
    )

    print(
        f"unique_product_urls={len(seen_urls)}"
    )

    print(
        f"books.json={books_file}"
    )

    print(
        f"errors.json={errors_file}"
    )

    if valid_records:

        print("\nComplete normalized record:")

        print(
            json.dumps(
                valid_records[0],
                indent=2,
                ensure_ascii=False
            )
        )
    return valid_records,errors

if __name__ == "__main__":
    fetch_and_cache()
    book_records=stage2()
    raw_records=stage3(
        book_records
    )
    valid_records,errors=stage4(raw_records)

    
    
# 📚 Books to Scrape — Polite Web Scraper

A Python web scraper built as part of the **FlyRank AI Backend Engineering Internship**.

The project scrapes book information from the public **Books to Scrape** catalogue, caches downloaded pages, extracts book details, validates and normalizes the records using Pydantic, handles individual page failures, and generates an honest run report.

The scraper is designed to be **polite, reproducible, idempotent, and failure-tolerant**.

---

## 🎯 Target Classification

The target selected for this assignment is:

> **Books from the Books to Scrape catalogue**

The scraper processes the first **3 catalogue pages**, with **20 books per page**, giving a target of:

**60 unique book records**

Target website:

https://books.toscrape.com/

The catalogue pages are:

- `https://books.toscrape.com/catalogue/page-1.html`
- `https://books.toscrape.com/catalogue/page-2.html`
- `https://books.toscrape.com/catalogue/page-3.html`

---

## 🚀 What This Project Does

The scraper follows a staged pipeline:

1. Fetch the first catalogue page.
2. Cache catalogue HTML locally.
3. Discover book detail URLs from the first three catalogue pages.
4. Fetch and cache individual book pages.
5. Extract raw book information.
6. Normalize the price into a numeric `price_gbp` value.
7. Validate records using Pydantic.
8. Store valid records in `books.json`.
9. Store invalid records in `errors.json`.
10. Continue processing when an individual book page fails.
11. Retry temporary failures such as timeouts and HTTP 5xx responses.
12. Generate `run-report.json` containing statistics about the run.

---

## 🛠️ Technology Stack

### Language

- Python 3.13

### Libraries

- `requests` — HTTP requests
- `BeautifulSoup4` — HTML parsing
- `Pydantic` — record validation
- Python `pathlib` — file and directory handling
- Python `json` — JSON output
- Python `datetime` — timestamps and run duration

### Browser Automation

No Selenium or browser automation is required.

The required data is already present in the HTML returned by the server. Therefore, using a browser would only add unnecessary overhead and complexity.

---

## 📁 Project Structure

```text
scraper/
│
├── src/
│   └── main.py
│
├── cache/
│   ├── catalogue-page-1.html
│   ├── catalogue-page-2.html
│   ├── catalogue-page-3.html
│   └── ...
│
├── output/
│   ├── books.json
│   ├── errors.json
│   └── run-report.json
│
├── .gitignore
├── README.md

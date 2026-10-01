import requests
from bs4 import BeautifulSoup
import csv
import os


BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"


def get_page(page_number):

    url = BASE_URL.format(page_number)

    response = requests.get(url)

    print(f"Page {page_number} - Status: {response.status_code}")

    if response.status_code != 200:
        return None

    return BeautifulSoup(response.content, "lxml")


def get_books(soup):

    books = []

    books_tags = soup.find_all("article", class_="product_pod")

    for book in books_tags:

        title_tag = book.find("h3").find("a")
        price_tag = book.find("p", class_="price_color")
        availability_tag = book.find(
            "p",
            class_="instock availability"
        )
        rating_tag = book.find("p", class_="star-rating")

        title = title_tag.get("title", "").strip()
        price = price_tag.get_text(strip=True)
        availability = availability_tag.get_text(strip=True)

        rating = rating_tag.get("class")[1] if rating_tag else "Unknown"

        books.append({
            "title": title,
            "price": price,
            "availability": availability,
            "rating": rating
        })

    return books


def save_to_csv(books):

    folder = os.path.dirname(os.path.abspath(__file__))

    filename = os.path.join(folder, "books.csv")

    fieldnames = [
        "title",
        "price",
        "availability",
        "rating"
    ]

    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(books)

    print(f"\nData saved to: {filename}")


def main():

    all_books = []

    for page_number in range(1, 51):

        soup = get_page(page_number)

        if soup is None:
            print(f"Could not scrape page {page_number}")
            continue

        books = get_books(soup)

        all_books.extend(books)

        print(f"Books found: {len(books)}")

    print(f"\nTotal books scraped: {len(all_books)}")

    save_to_csv(all_books)


if __name__ == "__main__":
    main()
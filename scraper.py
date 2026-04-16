import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

os.makedirs("data", exist_ok=True)

base_url = "http://books.toscrape.com/catalogue/page-{}.html"

books = []
page = 1

while True:
    url = base_url.format(page)
    response = requests.get(url)

    # Stop when no more pages
    if response.status_code != 200:
        print("No more pages. Stopping...")
        break

    # FIX encoding issue
    response.encoding = "utf-8"

    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.find_all("article", class_="product_pod")

    if not items:
        break

    print(f"Scraping page {page}...")

    for item in items:
        title = item.h3.a["title"]
        price = item.find("p", class_="price_color").text
        rating = item.find("p", class_="star-rating")["class"][1]

        books.append([title, price, rating])

    page += 1

df = pd.DataFrame(books, columns=["Title", "Price", "Rating"])
df.to_csv("data/books_raw.csv", index=False)

print("✅ Full scraping completed!")
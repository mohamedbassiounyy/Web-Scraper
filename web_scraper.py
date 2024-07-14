
import requests
from bs4 import BeautifulSoup

response = requests.get("https://books.toscrape.com")

soup = BeautifulSoup(response.content, "html.parser")

books = soup.find_all("article")

for book in books:
    try:
        title = book.h3.a["title"]
        rating = book.p["class"][1]
        price = book.find("p", class_="price_color").text    
        print("Title is: " + title + " || Rating is: " + rating + " || Price is: " + price)
    except (AttributeError, IndexError) as e:
        print(f"Error extracting data: {e}")
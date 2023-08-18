import requests
from bs4 import BeautifulSoup
import csv
import json
URL = "http://books.toscrape.com/catalogue/category/books_1/index.html"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

book_content = soup.find_all('li',class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

data = {}

for book_contents in book_content:
    title = book_contents.h3.a['title']
    price = book_contents.find('p',class_='price_color').text
    price = float(price.replace('£', ''))
    data[title]=price
    
json_data = json.dumps(data,indent=10)

print(json_data)
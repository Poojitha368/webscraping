import requests
from bs4 import BeautifulSoup

# choose the website
url = "http://quotes.toscrape.com/"

# Fetch the webpage
response = requests.get(url)

# parse the web page content
soup = BeautifulSoup(response.text,'html.parser')

# extract quotes and athors
quotes = soup.find_all('div',class_='quote')

# print(quotes)

for quote in quotes:
    text = quote.find('span',class_='text').text.strip()
    author = quote.find('small',class_='author').text.strip()
    print(f"author: {author} , quote: {text}")
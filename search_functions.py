import requests
from bs4 import BeautifulSoup

def search_amazon(name):
    # Amazon search function
    url = f"https://www.amazon.com/s?k={name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    products = soup.find_all('div', {'class': 's-result-item'})
    prices = []
    for product in products:
        price_tag = product.find('span', {'class': 'a-price-whole'})
        if price_tag:
            price = int(price_tag.text.replace(',', ''))
            prices.append(price)
    return prices

def search_walmart(name):
    # Walmart search function
    url = f"https://www.walmart.com/search?q={name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    products = soup.find_all('div', {'class': 'search-result-gridview-item'})
    prices = []
    for product in products:
        price_tag = product.find('span', {'class': 'price-main-block'})
        if price_tag:
            price = int(price_tag.text.replace(',', ''))
            prices.append(price)
    return prices

def convert(price):
    # Convert price to integer
    return int(price.replace(',', '')) 

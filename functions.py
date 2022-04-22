"""Functions to fetch information about Biofinity contact lenses from all stores"""

from bs4 import BeautifulSoup
import requests
from product_information import ProductInformation

def fetch_url_and_create_soup(product_url):
    # Get the html with requests library
    html_doc = requests.get(product_url).text
    # New beautiful soup object
    return BeautifulSoup(html_doc, "lxml")


def fetch_silmaasema():
    product_url = "https://www.silmaasema.fi/tuotteet/piilolinssit/jatkuvakayttoiset-piilolinssit/biofinity-C31.html"
    soup = fetch_url_and_create_soup(product_url)

    # Find price string, strip empty lines from start and end, remove '€' and ',' symbols
    price_string = soup.find("span", id="actual-price").text

    # Cleaning price_string so that it can be turned to a float
    price_prettified = price_string.strip().replace(" €", "").replace(",", ".")

    # Turn string into int and format it to have 2 decimals
    price_int = format(float(price_prettified), '.2f')

    # Returns a product object
    return ProductInformation("Silmäasema", product_url, price_int)

def fetch_lenson():
    product_url = "https://www.lenson.com/fi/biofinity-lens-347"
    soup = fetch_url_and_create_soup(product_url)

    # Find price string, strip empty lines from start and end, remove '€' and ',' symbols
    price_string = soup.find("span",
                             class_="inline priceLineThrough product-info-price-old product-price__old-price").text

    # Cleaning price_string so that it can be turned to a float
    price_prettified = price_string.strip().replace(" €", "").replace(",", ".")

    # Turn string into int and format it to have 2 decimals
    price_int = format(float(price_prettified), '.2f')

    # Lenson also has a discounted price
    discounted_price_string = soup.find("span",
                             class_="inline price bold productInfo-orgPrice product-info-price-current").text

    # Cleaning price_string so that it can be turned to a float
    discounted_price_prettified = discounted_price_string.strip().replace(" €", "").replace(",", ".")

    # Turn string into int and format it to have 2 decimals
    discounted_price_int = format(float(discounted_price_prettified), '.2f')

    # If discounted price is not "None" and is lower than normal price, price_int = discounted_price_int
    if discounted_price_int != "None" and discounted_price_int < price_int:
        price_int = discounted_price_int

    #print(price_string)
    #print(price_prettified)
    #print(price_int)

    #print(discounted_price_string)
    #print(discounted_price_prettified)
    #print(discounted_price_int)

    # Returns a product object
    return ProductInformation("Lenson", product_url, price_int)

fetch_lenson()
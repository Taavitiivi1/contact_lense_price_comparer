"""Functions to fetch information about Biofinity contact lenses from all stores"""

from bs4 import BeautifulSoup
import requests
from product_information import ProductInformation

def fetch_url_and_create_soup(product_url):
    # Get the html with requests library
    html_doc = requests.get(product_url).text
    # New beautiful soup object
    return BeautifulSoup(html_doc, "lxml")


def fetch_silmaasema(website_name, product_url):
    soup = fetch_url_and_create_soup(product_url)
    # Find price string, strip empty lines from start and end, remove '€' and ',' symbols
    price_string = soup.find("span", id="actual-price").text
    # Cleaning price_string so that it can be turned to a float
    price_prettified = price_string.strip().replace(" €", "").replace(",", ".")
    # Turn string into int and format it to have 2 decimals
    price_int = format(float(price_prettified), '.2f')
    # Returns a product object
    return ProductInformation(website_name, product_url, price_int)

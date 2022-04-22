"""Grab Biofinity contact lense prices from multiple websites and compare them"""

from functions import *

def print_products_information(products):
    for p in products:
        print(f"Name: {p.get_website_name()}, Price: {p.get_price()}, Url: {p.get_url()}")

if __name__ == "__main__":
    products = []

    silmaasema = fetch_silmaasema()
    products.append(silmaasema)

    lenson = fetch_lenson()
    products.append(lenson)

    print_products_information(products)
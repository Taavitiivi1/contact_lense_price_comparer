"""Grab Biofinity contact lense prices from multiple websites and compare them"""

from functions import *

if __name__ == "__main__":
    products = []

    silmaasema = fetch_silmaasema("Silmäasema", "https://www.silmaasema.fi/tuotteet/piilolinssit/jatkuvakayttoiset-piilolinssit/biofinity-C31.html")
    products.append(silmaasema)

    for p in products:
        print(f"Name: {p.get_website_name()}, Price: {p.get_price()}, Url: {p.get_url()}")
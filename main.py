"""Grab Biofinity contact lense prices from multiple websites and compare them"""

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def print_products_information(products):
    for p in products:
        print(f"Name: {p.get_website_name()}, Price: {p.get_price()}, Url: {p.get_url()}")

if __name__ == "__main__":
    s = Service("C:\ChromeDriver\chromedriver.exe")
    driver = webdriver.Chrome(service=s)

    driver.get("https://www.silmaasema.fi/tuotteet/piilolinssit/jatkuvakayttoiset-piilolinssit/biofinity-C31.html")

    price = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "actual-price"))
    )

    print(price.text)


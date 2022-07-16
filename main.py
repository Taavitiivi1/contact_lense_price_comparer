"""Grab Biofinity contact lense prices from multiple websites and compare them"""

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from product_information import ProductInformation
import time
from tkinter import *
import tkinter as tk
import tkinter.ttk as tkk
import sys
import webbrowser


def get_url(url):
    driver.get(url)
    time.sleep(3)  # Temporary fix for bug that raises an unknown exception
    return url


def print_products(products):
    for p in products:
        print(f"Name: {p.get_website_name()}, Price: {p.get_price()}, Url: {p.get_url()}")


def fetch_silmaasema():
    url = get_url("https://www.silmaasema.fi/tuotteet/piilolinssit/jatkuvakayttoiset-piilolinssit/biofinity-C31.html")

    price_span = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "actual-price"))
    )
    price = float(price_span.text.split()[0].replace(",", "."))

    return ProductInformation("Silmäasema", price, url)


def fetch_lenson():
    url = get_url("https://www.lenson.com/fi/biofinity-lens-347")

    price_span = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product-price"))
    )
    price = float(price_span.text.split("€")[1].replace(",", "."))

    return ProductInformation("Lenson", price, url)


def fetch_lensway():
    url = get_url("https://www.lensway.fi/biofinity-lens-347")

    price_span = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "pp__info__price"))
    )

    price = float(price_span.text.split("€")[0].replace(",", "."))

    return ProductInformation("Lensway", price, url)


def fetch_specsavers():
    url = get_url("https://www.specsavers.fi/piilolinssit/kuukausilinssit/biofinity-6-linssia")

    price_span = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "price-now"))
    )

    price = float(price_span.text.split()[0])

    return ProductInformation("Specsavers", price, url)


def fetch_misterspex():
    url = get_url("https://www.misterspex.fi/p/cl/79613")

    price_span = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "msx-font-weight-fontWeight700"))
    )

    price = float(price_span.text.split()[2].replace(",", "."))

    return ProductInformation("Misterspex", price, url)


def fetch_instrumentarium():
    url = get_url("https://www.instru.fi/biofinity")

    price_span = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product-info-price"))
    )

    price = float(price_span.text.split()[0].replace(",", "."))

    return ProductInformation("Instrumentarium", price, url)


def fetch_alensa():
    url = get_url("https://www.alensa.fi/biofinity-6-kpl")

    price_span = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product-main-price-total"))
    )

    price = float(price_span.text.split()[0])

    return ProductInformation("Alensa", price, url)


def fetch_products():
    products = [
        fetch_silmaasema(),
        fetch_lenson(),
        fetch_lensway(),
        fetch_specsavers(),
        fetch_misterspex(),
        fetch_instrumentarium(),
        fetch_alensa(),
    ]

    return products


def build_products():
    products = fetch_products()
    products.sort(key=lambda x: x.get_price())

    print_products(products)
    driver.quit()

    return products


def build_gui(products):
    window = tk.Tk()

    for i in range(len(products)):
        window.columnconfigure(i, weight=1, minsize=20)
        window.rowconfigure(i, weight=1, minsize=20)

        for j in range(3):
            frame = tk.Frame(
                master=window,
                relief=tk.RAISED,
                borderwidth=1,
            )
            frame.grid(row=i, column=j, padx=2, pady=2)
            if j == 0:
                label = tk.Label(master=frame, text=products[i].get_website_name())
            elif j == 1:
                label = tk.Label(master=frame, text=products[i].get_price())
            elif j == 2:
                label = tk.Button(master=frame, text=products[i].get_url(),
                                  command=lambda: webbrowser.open(products[i].get_url()))
            label.pack(padx=5, pady=5)

    window.mainloop()


if __name__ == "__main__":
    s = Service("C:\ChromeDriver\chromedriver.exe")
    driver = webdriver.Chrome(service=s)

    products = build_products()
    build_gui(products)

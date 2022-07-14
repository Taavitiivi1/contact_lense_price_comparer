class ProductInformation:
    """Class for gathering a products (lense) information"""
    _website_name = ""
    _product_url = ""
    _price = 0
    # discounted_price and normal_price?
    # amount? If not 6, we have to use math to get it to 6
    # free_transport?

    def __init__(self, website_name, product_url, price):
        self._website_name = website_name
        self._product_url = product_url
        self._price = price

    def get_website_name(self):
        return self._website_name

    def set_website_name(self, website_name):
        self._website_name = website_name

    def get_url(self):
        return self._product_url

    def set_url(self, url):
        self._product_url = url

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

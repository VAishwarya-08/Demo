from appium.webdriver.common.appiumby import AppiumBy
from utils.base_page import BasePage

class CatalogPage(BasePage):
    catalog_button = (AppiumBy.ID, "com.example.app:id/catalog")
    product_name = (AppiumBy.ID, "com.example.app:id/product_name")
    product_price = (AppiumBy.ID, "com.example.app:id/product_price")

    def open_catalog(self):
        self.click(self.catalog_button)

    def get_product_details(self):
        name = self.get_text(self.product_name)
        price = self.get_text(self.product_price)
        return name, price

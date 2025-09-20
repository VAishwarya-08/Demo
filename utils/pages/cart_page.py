from appium.webdriver.common.appiumby import AppiumBy
from utils.base_page import BasePage

class CartPage(BasePage):
    add_to_cart_button = (AppiumBy.ID, "com.example.app:id/add_to_cart")
    cart_item_name = (AppiumBy.ID, "com.example.app:id/cart_item_name")

    def add_product_to_cart(self):
        self.click(self.add_to_cart_button)

    def get_cart_item_name(self):
        return self.get_text(self.cart_item_name)

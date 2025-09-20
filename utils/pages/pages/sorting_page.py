from appium.webdriver.common.appiumby import AppiumBy
from utils.base_page import BasePage

class SortingPage(BasePage):
    sort_button = (AppiumBy.ID, "com.example.app:id/sort")
    product_prices = (AppiumBy.ID, "com.example.app:id/product_price")

    def apply_sorting(self):
        self.click(self.sort_button)

    def get_sorted_prices(self):
        elements = self.driver.find_elements(*self.product_prices)
        prices = [float(e.text.replace("$", "")) for e in elements]
        return prices

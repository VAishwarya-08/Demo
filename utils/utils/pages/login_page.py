from appium.webdriver.common.appiumby import AppiumBy
from utils.base_page import BasePage

class LoginPage(BasePage):
    username_field = (AppiumBy.ID, "com.example.app:id/username")
    password_field = (AppiumBy.ID, "com.example.app:id/password")
    login_button = (AppiumBy.ID, "com.example.app:id/login")
    logout_button = (AppiumBy.ID, "com.example.app:id/logout")
    error_message = (AppiumBy.ID, "com.example.app:id/error")

    def login(self, username, password):
        self.send_keys(self.username_field, username)
        self.send_keys(self.password_field, password)
        self.click(self.login_button)

    def logout(self):
        self.click(self.logout_button)

    def get_error_message(self):
        return self.get_text(self.error_message)

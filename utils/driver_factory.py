from appium import webdriver

def create_driver():
    desired_caps = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "appPackage": "com.example.app",
        "appActivity": "com.example.app.MainActivity",
        "automationName": "UiAutomator2"
    }
    return webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

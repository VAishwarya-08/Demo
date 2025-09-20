import pytest
import allure
from utils.driver_factory import create_driver

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshot = driver.get_screenshot_as_png()
            allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)

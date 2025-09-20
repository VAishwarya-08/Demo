import pytest
from pages.login_page import LoginPage

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

def test_valid_login(login_page):
    login_page.login("valid_user", "valid_pass")
    # Add assertion for successful login

def test_invalid_login(login_page):
    login_page.login("invalid_user", "wrong_pass")
    assert "Invalid credentials" in login_page.get_error_message()

def test_logout(login_page):
    login_page.login("valid_user", "valid_pass")
    login_page.logout()
    # Add assertion for logout success

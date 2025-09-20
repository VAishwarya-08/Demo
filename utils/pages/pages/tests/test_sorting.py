import pytest
from pages.sorting_page import SortingPage

@pytest.fixture
def sorting_page(driver):
    return SortingPage(driver)

def test_sort_by_price(sorting_page):
    sorting_page.apply_sorting()
    prices = sorting_page.get_sorted_prices()
    assert prices == sorted(prices)

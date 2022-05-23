import time

from pages.Home import HomePage
from pages.Products import ProductsPage


def test_add_to_cart(browser):
    home_page = HomePage(browser)
    products_page = ProductsPage(browser)

    home_page.load()
    assert (home_page.title() == "Swag Labs")
    home_page.login()
    assert products_page.verify_url()
    assert products_page.verify_logo_display()
    products_page.add_products_to_cart()
    # TODO assert products_page.verify_cart_count()

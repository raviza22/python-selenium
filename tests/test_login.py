
from pages.Home import HomePage
from pages.Products import ProductsPage

def test_login(browser):
    home_page = HomePage(browser)
    products_page = ProductsPage(browser)

    home_page.load()
    assert (home_page.title() == "Swag Labs")
    home_page.login()

    assert products_page.verify_url()

import pytest
import selenium.webdriver


@pytest.fixture
def browser():
    b = selenium.webdriver.Chrome()
    b.implicitly_wait(5)

    yield b

    b.quit()
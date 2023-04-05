import pytest
from selenium import webdriver


@pytest.fixture(scope="session", autouse=False)
def get_book_page():
    driver = webdriver.Firefox()
    driver.get("https://demoqa.com/books")
    yield driver
    driver.quit()


import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope="function", autouse=False)
def create_headless_driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    yield driver


@pytest.fixture(scope="function", autouse=False)
def go_to_page(create_headless_driver):
    get_page = create_headless_driver
    get_page.get("https://demoqa.com/links")
    yield get_page
    get_page.quit()

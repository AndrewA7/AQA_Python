import pytest
from selenium import webdriver


@pytest.fixture(scope="class", autouse=False)
def get_checkbox_page():
    driver = webdriver.Firefox()
    driver.get("https://demoqa.com/checkbox")
    yield driver
    # driver.quit()
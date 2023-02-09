import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class", autouse=False)
def get_checkbox_page():
    driver = webdriver.Firefox()
    driver.get("https://demoqa.com/checkbox")
    yield driver
    driver.quit()


@pytest.fixture(scope="class", autouse=False)
def get_radiobutton_page():
    driver = webdriver.Firefox()
    driver.get("https://demoqa.com/radio-button")
    yield driver
    driver.quit()


@pytest.fixture(scope="class", autouse=False)
def get_dynamic_properties_page():
    driver = webdriver.Firefox()
    driver.get("https://demoqa.com/dynamic-properties")
    yield driver
    driver.quit()


@pytest.fixture(scope="function", autouse=False)
def refresh_checkbox_page(get_checkbox_page):
    driver = get_checkbox_page
    yield driver
    driver.refresh()

@pytest.fixture(scope="function", autouse=False)
def refresh_page(get_radiobutton_page):
    driver = get_radiobutton_page
    yield driver
    driver.refresh()


@pytest.fixture(scope="function", autouse=False)
def refresh_dynamic_page(get_dynamic_properties_page):
    driver = get_dynamic_properties_page
    yield driver
    driver.refresh()


@pytest.fixture(scope="function", autouse=False)
def get_text_id(get_dynamic_properties_page):
    driver = get_dynamic_properties_page
    text_field_data = driver.find_element(By.XPATH, '//p[contains(text(), "This text")]')
    text_field_id = text_field_data.get_attribute("id")
    yield text_field_id
    driver.refresh()

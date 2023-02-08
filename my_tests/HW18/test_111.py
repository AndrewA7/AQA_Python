from selenium import webdriver
from selenium.webdriver.common.by import By
from . import additional_data
from . import locators

class TestOne:
    def test_checkboxes(self, get_checkbox_page):
        driver = get_checkbox_page
        folders = ['Commands', 'General']
        expand_all = driver.find_element(By.CSS_SELECTOR, locators.EXPAND_ALL_BUTTON)
        expand_all.click()
        additional_data.select_folders(driver, additional_data.optimize_test_data(folders).get('tree'))
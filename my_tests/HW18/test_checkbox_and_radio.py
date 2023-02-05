from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from . import locators

i_can_see = "arguments[0].scrollIntoView();"
# element_name = ["commands", "general"]
element_name = [locators.COMMANDS_CHECKBOX, locators.GENERAL_CHECKBOX]
class TestForCheckboxPage:

    def test_checkboxes_one(self, get_checkbox_page):
        driver = get_checkbox_page
        expand_all = driver.find_element(By.CSS_SELECTOR, locators.EXPAND_ALL_BUTTON)
        expand_all.click()
        all_folders = driver.find_elements(By.XPATH, locators.ALL_FOLDERS)
        print(all_folders)
        # for i in all_folders:
        #     print(i.get_attribute("id"))
        #     # if i in element_name:
        #     #     if not i.is_selected():
        #     #         i.click()
        #

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from . import locators


class TestForCheckboxPage:

    def test_checkboxes_one(self, get_checkbox_page, refresh_checkbox_page):
        folders_for_select = ["Commands", "General", "React"]
        driver = get_checkbox_page
        expand_all = driver.find_element(By.CSS_SELECTOR, locators.EXPAND_ALL_BUTTON)
        expand_all.click()
        for i in folders_for_select:
            select_folder = driver.find_element(By.XPATH, f'//span[contains(text(), "{i}")]')
            driver.execute_script("arguments[0].scrollIntoView();", select_folder)
            select_folder.click()
        result_check_boxes = driver.find_elements(By.XPATH, locators.RESULT_CHECK_BOXES)
        result_list = []
        for answer_element in result_check_boxes:
            result_list.append(answer_element.text.title())
        assert sorted(result_list) == sorted(folders_for_select)


    def test_checkboxes_two(self, get_checkbox_page):
        folders_for_select = ["Commands", "General", "React"]
        driver = get_checkbox_page
        expand_all = driver.find_element(By.CSS_SELECTOR, locators.EXPAND_ALL_BUTTON)
        expand_all.click()
        all_folders = driver.find_element(By.XPATH, locators.ALL_FOLDERS).text
        all_folders_list = all_folders.split()
        for check_folder in all_folders_list:
            if check_folder in folders_for_select:
                select_folder = driver.find_element(By.XPATH, f'//span[contains(text(), "{check_folder}")]')
                driver.execute_script("arguments[0].scrollIntoView();", select_folder)
                select_folder.click()
        result_check_boxes = driver.find_elements(By.XPATH, locators.RESULT_CHECK_BOXES)
        result_list = []
        for answer_element in result_check_boxes:
            result_list.append(answer_element.text.title())
        assert sorted(result_list) == sorted(folders_for_select)


class TestRadiobuttonPage:

    def test_activate_yes_radio(self, get_radiobutton_page, refresh_page):
        driver = get_radiobutton_page
        yes_radiobutton = driver.find_element(By.XPATH, locators.YES_RADIO)
        yes_radiobutton.click()

        result_yes_radiobutton_with_id = driver.find_element(By.XPATH, locators.YES_RADIO_ID_SELECTED)
        assert result_yes_radiobutton_with_id.is_selected()

    def test_activate_yes_radio_two(self, get_radiobutton_page, refresh_page):
        driver = get_radiobutton_page
        yes_radiobutton = driver.find_element(By.XPATH, locators.YES_RADIO)
        yes_radiobutton.click()

        result_yes_radiobutton_with_answer = driver.find_element(By.XPATH, locators.RADIO_ANSWER).text
        assert result_yes_radiobutton_with_answer == "Yes"

    def test_get_radio_buttons_info(self, get_radiobutton_page):
        states = {}
        driver = get_radiobutton_page
        zone_for_searching = driver.find_element(By.XPATH, locators.ZONE_FOR_SEARCHING)
        labels = zone_for_searching.find_elements(By.XPATH, '//label[@for]')
        inputs = zone_for_searching.find_elements(By.XPATH, '//input[@type="radio"]')
        elements_ids = len(labels)
        for i in list(range(elements_ids)):
            states.update({labels[i].text: {'selected': inputs[i].is_selected(),
                                            'enabled': inputs[i].is_enabled()}})


    def test_activate_no_radio(self, get_radiobutton_page):
        driver = get_radiobutton_page
        no_radiobutton_id = driver.find_element(By.XPATH, locators.NO_RADIO_ID_ANSWER)
        driver.execute_script("arguments[0].removeAttribute('disabled','disabled')", no_radiobutton_id)
        no_radiobutton = driver.find_element(By.XPATH, locators.NO_RADIO)
        no_radiobutton.click()

        result_no_radiobutton = driver.find_element(By.XPATH, locators.NO_RADIO_ID_ANSWER)
        assert result_no_radiobutton.is_selected()


class TestForDynamicProperties:

    def test_get_id(self, get_dynamic_properties_page, get_text_id):
        driver = get_dynamic_properties_page
        result_text_field_data = driver.find_element(By.ID, get_text_id).text
        assert "random" in result_text_field_data

    def test_wait_for_enable_element(self, get_dynamic_properties_page, refresh_dynamic_page):
        driver = get_dynamic_properties_page
        wait = WebDriverWait(driver, 10)
        will_enabled_five_seconds = wait.until((EC.element_to_be_clickable((By.XPATH, locators.ENABLE_AFTER))))
        assert will_enabled_five_seconds.is_enabled()

    def test_wait_for_red_element(self, get_dynamic_properties_page, refresh_dynamic_page):
        driver = get_dynamic_properties_page
        wait = WebDriverWait(driver, 10)
        red_color_text = wait.until(EC.visibility_of_element_located((By.XPATH, locators.TEXT_DANGER)))
        assert red_color_text.is_enabled()

    def test_button_is_present(self, get_dynamic_properties_page):
        driver = get_dynamic_properties_page
        wait = WebDriverWait(driver, 10)
        visible_button = wait.until(EC.visibility_of_element_located((By.XPATH, locators.VISIBLE_AFTER)))
        assert visible_button.is_displayed()

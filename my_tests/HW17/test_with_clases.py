from selenium.webdriver.common.by import By
from . import data_for_test


class TestAllFieldsWithXpath:
    def test_full_name_field(self, get_page):
        driver = get_page
        name = driver.find_element(By.XPATH, data_for_test.FULL_NAME_FIELD)
        submit = driver.find_element(By.XPATH, data_for_test.SUBMIT_BUTTON)

        name.send_keys(data_for_test.user_name)
        driver.execute_script("arguments[0].scrollIntoView();", submit)
        submit.click()

        result_name = driver.find_element(By.XPATH, data_for_test.ANSWER_FULL_NAME_FIELD).text
        assert data_for_test.user_name == result_name.split(":")[1]

    def test_email_field(self, get_page):
        driver = get_page
        mail = driver.find_element(By.XPATH, data_for_test.EMAIL_FIELD)
        submit = driver.find_element(By.XPATH, data_for_test.SUBMIT_BUTTON)

        mail.send_keys(data_for_test.user_mail)
        driver.execute_script("arguments[0].scrollIntoView();", submit)
        submit.click()

        result_mail = driver.find_element(By.XPATH, data_for_test.ANSWER_EMAIL_FIELD).text
        assert data_for_test.user_mail == result_mail.split(":")[1]

    def test_current_address_field(self, get_page):
        driver = get_page
        current_address = driver.find_element(By.XPATH, data_for_test.CURRENT_ADDRESS_FIELD)
        submit = driver.find_element(By.XPATH, data_for_test.SUBMIT_BUTTON)

        current_address.send_keys(data_for_test.user_current_address)
        driver.execute_script("arguments[0].scrollIntoView();", submit)
        submit.click()

        result_current_address = driver.find_element(By.XPATH, data_for_test.ANSWER_CURRENT_ADDRESS_FIELD).text
        assert data_for_test.user_current_address == result_current_address.split(":")[1]

    def test_permanent_address_field(self, get_page):
        driver = get_page
        permanent_address = driver.find_element(By.XPATH, data_for_test.PERMANENT_ADDRESS_FIELD)
        submit = driver.find_element(By.XPATH, data_for_test.SUBMIT_BUTTON)

        permanent_address.send_keys(data_for_test.user_permanent_address)
        driver.execute_script("arguments[0].scrollIntoView();", submit)
        submit.click()

        result_permanent_address = driver.find_element(By.XPATH, data_for_test.ANSWER_PERMANENT_ADDRESS_FIELD).text
        assert data_for_test.user_permanent_address == result_permanent_address.split(":")[1]


class TestWithWrongMail:
    def test_with_wrong_mail(self, wrong_mail):
        driver = wrong_mail
        error_field = driver.find_element(By.XPATH, data_for_test.ANSWER_WRONG_MAIL)
        assert error_field

# ------------------------CSS--------------------------


class TestAllFieldsWithCss:

    def test_css_full_name_field(self, css_get_page):
        driver = css_get_page
        name = driver.find_element(By.CSS_SELECTOR, data_for_test.CSS_FULL_NAME_FIELD)
        submit = driver.find_element(By.CSS_SELECTOR, data_for_test.CSS_SUBMIT_BUTTON)

        name.send_keys(data_for_test.user_name)
        driver.execute_script("arguments[0].scrollIntoView();", submit)
        submit.click()

        result_name = driver.find_element(By.CSS_SELECTOR, data_for_test.ANSWER_CSS_FULL_NAME_FIELD).text
        assert data_for_test.user_name == result_name.split(":")[1]

    def test_css_email_field(self, css_get_page):
        driver = css_get_page
        mail = driver.find_element(By.CSS_SELECTOR, data_for_test.CSS_EMAIL_FIELD)
        submit = driver.find_element(By.CSS_SELECTOR, data_for_test.CSS_SUBMIT_BUTTON)

        mail.send_keys(data_for_test.user_mail)
        driver.execute_script("arguments[0].scrollIntoView();", submit)
        submit.click()

        result_mail = driver.find_element(By.CSS_SELECTOR, data_for_test.ANSWER_CSS_EMAIL_FIELD).text
        assert data_for_test.user_mail == result_mail.split(":")[1]

    def test_css_current_address_field(self, css_get_page):
        driver = css_get_page
        current_address = driver.find_element(By.CSS_SELECTOR, data_for_test.CSS_CURRENT_ADDRESS_FIELD)
        submit = driver.find_element(By.CSS_SELECTOR, data_for_test.CSS_SUBMIT_BUTTON)

        current_address.send_keys(data_for_test.user_current_address)
        driver.execute_script("arguments[0].scrollIntoView();", submit)
        submit.click()

        result_current_address = driver.find_element(By.CSS_SELECTOR, data_for_test.ANSWER_CSS_CURRENT_ADDRESS_FIELD).text
        assert data_for_test.user_current_address == result_current_address.split(":")[1]

    def test_css_permanent_address_field(self, css_get_page):
        driver = css_get_page
        permanent_address = driver.find_element(By.CSS_SELECTOR, data_for_test.CSS_PERMANENT_ADDRESS_FIELD)
        submit = driver.find_element(By.CSS_SELECTOR, data_for_test.CSS_SUBMIT_BUTTON)

        permanent_address.send_keys(data_for_test.user_permanent_address)
        driver.execute_script("arguments[0].scrollIntoView();", submit)
        submit.click()

        result_permanent_address = driver.find_element(By.CSS_SELECTOR, data_for_test.ANSWER_CSS_PERMANENT_ADDRESS_FIELD).text
        assert data_for_test.user_permanent_address == result_permanent_address.split(":")[1]


class TestWithWrongMailWithCss:
    def test_with_wrong_mail(self, css_wrong_mail):
        driver = css_wrong_mail
        error_field = driver.find_element(By.CSS_SELECTOR, data_for_test.ANSWER_CSS_WRONG_MAIL)
        assert error_field

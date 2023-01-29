from selenium.webdriver.common.by import By
from . import data_for_test


class TestAllFieldsWithXpath:
    def test_full_name_field(self, get_page):
        driver = get_page
        result_name = driver.find_element(By.XPATH, '//p [@id="name"]').text
        assert data_for_test.user_name == result_name.split(":")[1]

    def test_email_field(self, get_page):
        driver = get_page
        result_mail = driver.find_element(By.XPATH, '//p [@id="email"]').text
        assert data_for_test.user_mail == result_mail.split(":")[1]

    def test_current_address_field(self, get_page):
        driver = get_page
        result_current_address = driver.find_element(By.XPATH, '//p [@id="currentAddress"]').text
        assert data_for_test.user_current_address == result_current_address.split(":")[1]

    def test_permanent_address_field(self, get_page):
        driver = get_page
        result_permanent_address = driver.find_element(By.XPATH, '//p [@id="permanentAddress"]').text
        assert data_for_test.user_permanent_address == result_permanent_address.split(":")[1]


class TestWithWrongMail:
    def test_with_wrong_mail(self, wrong_mail):
        driver = wrong_mail
        error_field = driver.find_element(By.XPATH, '//input [@class= "mr-sm-2 field-error form-control"]')
        assert error_field

# ------------------------CSS--------------------------


class TestAllFieldsWithCss:
    def test_css_full_name_field(self, css_get_page):
        driver = css_get_page
        result_name = driver.find_element(By.CSS_SELECTOR, 'p[id=name]').text
        assert data_for_test.user_name == result_name.split(":")[1]

    def test_css_email_field(self, css_get_page):
        driver = css_get_page
        result_mail = driver.find_element(By.CSS_SELECTOR, 'p[id=email]').text
        assert data_for_test.user_mail == result_mail.split(":")[1]

    def test_css_current_address_field(self, css_get_page):
        driver = css_get_page
        result_current_address = driver.find_element(By.CSS_SELECTOR, 'p[id=currentAddress]').text
        assert data_for_test.user_current_address == result_current_address.split(":")[1]

    def test_css_permanent_address_field(self, css_get_page):
        driver = css_get_page
        result_permanent_address = driver.find_element(By.CSS_SELECTOR, 'p[id=permanentAddress]').text
        assert data_for_test.user_permanent_address == result_permanent_address.split(":")[1]


class TestWithWrongMailWithCss:
    def test_with_wrong_mail(self, css_wrong_mail):
        driver = css_wrong_mail
        error_field = driver.find_element(By.CSS_SELECTOR, 'input[class= "mr-sm-2 field-error form-control"]')
        assert error_field

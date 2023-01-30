import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from . import data_for_test


@pytest.fixture(scope="class", autouse=False)
def get_page():
    web_browser = webdriver.Firefox()
    web_browser.get("https://demoqa.com/text-box")
    yield web_browser
    web_browser.quit()


@pytest.fixture(scope="class", autouse=False)
def wrong_mail():
    driver = webdriver.Firefox()
    driver.get("https://demoqa.com/text-box")
    mail = driver.find_element(By.XPATH, data_for_test.EMAIL_FIELD)
    submit = driver.find_element(By.XPATH, data_for_test.SUBMIT_BUTTON)

    mail.send_keys(data_for_test.wrong_user_mail)
    driver.execute_script("arguments[0].scrollIntoView();", submit)
    submit.click()

    driver.execute_script("arguments[0].scrollIntoView();", mail)
    yield driver
    driver.quit()


@pytest.fixture(scope="class", autouse=False)
def css_get_page():
    web_browser = webdriver.Firefox()
    web_browser.get("https://demoqa.com/text-box")
    yield web_browser
    web_browser.quit()


@pytest.fixture(scope="class", autouse=False)
def css_wrong_mail():
    driver = webdriver.Firefox()
    driver.get("https://demoqa.com/text-box")
    mail = driver.find_element(By.CSS_SELECTOR, data_for_test.CSS_EMAIL_FIELD)
    submit = driver.find_element(By.CSS_SELECTOR, data_for_test.CSS_SUBMIT_BUTTON)

    mail.send_keys(data_for_test.wrong_user_mail)
    driver.execute_script("arguments[0].scrollIntoView();", submit)
    submit.click()

    driver.execute_script("arguments[0].scrollIntoView();", mail)
    yield driver
    driver.quit()

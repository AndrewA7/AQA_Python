from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


def set_checkbox_state(driver: WebDriver, folder_name: str, enabled: bool = True) -> None:
    folder = driver.find_element(By.XPATH,
                                 f'//span[@class="rct-title"][.="{folder_name}"]'
                                 f'ancestor::span[@class="rct-title"]')
    ActionChains(driver).move_to_element(to_element=folder).perform()
    driver.execute_script("arguments[0].scrollIntoView()", folder)
    fold_input = folder.find_element(By.CSS_SELECTOR, 'input[id]')
    fold_checkbox = folder.find_element(By.CSS_SELECTOR, 'label[for]')
    if enabled:
        if not fold_input.is_selected():
            fold_checkbox.click()
    else:
        if fold_input.is_selected():
            fold_checkbox.click()


def select_folder(driver: WebDriver, folder: str, enabled=True):
    set_checkbox_state(driver, folder, enabled=enabled)


def select_folders(driver: WebDriver = None, folders: list = None):
    if folders:
        for folder in folders:
            select_folder(driver, folder, enabled=True)


def optimize_test_data(data: list):
    return {'tree': [d.capitalize() for d in data],
            'results': [r.lower() for r in data]}



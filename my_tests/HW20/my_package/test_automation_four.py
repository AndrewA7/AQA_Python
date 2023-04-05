import requests
from selenium.webdriver.common.by import By
# from page_object import PageObject



class TestForBooksPage:


    def test_get_books_by_publisher(self, get_book_page):
        publisher = "O'Reilly Media"
        driver = get_book_page
        one_publisher = driver.find_elements(By.XPATH, f'//div[contains(text(), "{publisher}")]/parent::div[1]')
        book_list = []
        books_counter = 0
        for list_element in one_publisher:
            book_list.append(list_element.text.split("\n"))
            books_counter += 1
        print(book_list, books_counter)
        if publisher == "O'Reilly Media":
            assert books_counter == 6
        elif publisher == "No Starch Press":
            assert books_counter == 2
        else:
            assert False


    def test_is_image_on_book_one(self, get_book_page, image=None):
        author = "Kyle Simpson"
        driver = get_book_page
        is_image_here = driver.find_element(By.XPATH, '//div[contains(text(),\n '
                                                      f'"{author}")]/parent::div[1]/child::div/img')
        results = [requests.get(image).status_code for image in is_image_here]
        print("=================================> ",is_image_here)
        pass

    def test_is_image_on_book_two(self):
        pass

    def test_search_field(self):
        pass

    def test_sorted_by_publisher(self):
        pass

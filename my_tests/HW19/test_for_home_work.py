import json
import time
import requests
import pytest
from selenium.webdriver.common.by import By

from . import response_data


class TestForFirstTask:

    def test_is_home_on_page(self, go_to_page):
        driver = go_to_page
        home_links = driver.find_elements(By.XPATH, '//a[contains(text(), "Home")]')
        assert len(home_links) == 2


class TestForSecondAndThirdTask:
    @pytest.mark.timed
    def test_one(self):
        time.sleep(2)
        assert True

    @pytest.mark.timed
    def test_two(self):
        time.sleep(2)
        assert True

    @pytest.mark.timed
    def test_three(self):
        time.sleep(2)
        assert False

    @pytest.mark.timed
    def test_four(self):
        time.sleep(2)
        assert True

    @pytest.mark.timed
    def test_five(self):
        time.sleep(2)
        assert True

    @pytest.mark.timed
    def test_six(self):
        time.sleep(2)
        assert False

    @pytest.mark.timed
    def test_seven(self):
        time.sleep(2)
        assert True

    @pytest.mark.timed
    def test_eight(self):
        time.sleep(2)
        assert True

    @pytest.mark.timed
    def test_nine(self):
        time.sleep(2)
        assert True

    @pytest.mark.timed
    def test_ten(self):
        time.sleep(2)
        assert True


class TestForFifthTaskSynthetic:
    @pytest.mark.api
    def test_create_person(self):
        response = requests.post("https://reqres.in/api/users",
                                 json={"name": "morpheus", "job": "leader"})
        assert response.status_code == 201

    @pytest.mark.api
    def test_read_person(self):
        response = requests.get("https://reqres.in/api/users/2")
        assert response.status_code == 200
        parsed = json.loads(response.content)
        assert parsed == response_data.read_user_response

    @pytest.mark.api
    def test_update_person(self):
        response = requests.put("https://reqres.in/api/users/2",
                                json={"name": "morpheus", "job": "zion resident"})
        assert response.status_code == 200
        parsed = json.loads(response.content)
        print(parsed)

    @pytest.mark.api
    def test_delete_person(self):
        response = requests.delete("https://reqres.in/api/users/2")
        assert response.status_code == 204


class TestForFifthTaskReal:
    def test_get_users(self):
        response = requests.get("https://reqres.in/api/users?page=2")
        assert response.status_code == 200
        parsed = json.loads(response.content)
        assert len(parsed["data"]) == 6

    def test_get_one_user(self):
        response = requests.get("https://reqres.in/api/users/2")
        assert response.status_code == 200
        parsed = json.loads(response.content)
        assert all((
            parsed["data"]["id"] == response_data.read_user_response["data"]["id"],
            parsed["data"]["email"] == response_data.read_user_response["data"]["email"],
            parsed["data"]["first_name"] == response_data.read_user_response["data"]["first_name"],
            parsed["data"]["last_name"] == response_data.read_user_response["data"]["last_name"],
            parsed["data"]["avatar"] == response_data.read_user_response["data"]["avatar"]
        ))

# this method doen't works
    def test_get_authorization(self):
        response = requests.post("https://reqres.in/api/login",
                                 auth={"email": "eve.holt@reqres.in",
                                       "password": "cityslicka"})
        assert response.status_code == 200
        parsed = json.loads(response.content)
        assert (parsed["token"] == response_data.user_register_response["token"])

    def test_create_user(self):
        response = requests.post("https://reqres.in/api/register",
                                 json={"email": "eve.holt@reqres.in",
                                       "password": "pistol"})
        assert response.status_code == 200
        parsed = json.loads(response.content)
        assert (parsed["token"] == response_data.user_register_response["token"])

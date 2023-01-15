import pytest


class TestSuite():

    @pytest.mark.from_class
    def test_one(self, test_fixture):
        print("\ntest one started")
        print("\ntest one finished")

    @pytest.mark.from_class
    def test_two(self, test_fixture):
        print("\ntest two started")
        print("\ntest two finished")

    @pytest.mark.from_class
    def test_three(self, test_fixture):
        print("\ntest three started")
        print("\ntest three finished")

    @pytest.mark.from_class
    def test_four(self, test_fixture):
        print("\ntest four started")
        print("\ntest four finished")

    @pytest.mark.from_class
    def test_five(self, test_fixture):
        print("\ntest five started")
        print("\ntest five finished")




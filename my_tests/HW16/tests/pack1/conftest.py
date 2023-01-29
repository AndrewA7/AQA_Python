import pytest


@pytest.fixture(scope="class", autouse=True)
def test_fixture():
    print("\nClass fixture started")
    yield
    print("\nClass fixture finished")
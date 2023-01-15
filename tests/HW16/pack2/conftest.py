import pytest


@pytest.fixture(scope="package", autouse=True)
def package_fixture():
    print("\nPackage 2 fixture started")
    yield
    print("\nPackage 2 fixture finished")

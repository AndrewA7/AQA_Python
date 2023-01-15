import pytest


@pytest.fixture(scope="session", autouse=True)
def very_important_fixture():
    print("\nSession fixture starts")
    yield
    print("\nSession fixture ends")

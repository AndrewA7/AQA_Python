import os
import pytest


@pytest.fixture(scope="package", autouse=True)
def test_three_fixture():
    print(f"\n{os.name} test package starts")
    yield
    print("\nTest 3 session ends")

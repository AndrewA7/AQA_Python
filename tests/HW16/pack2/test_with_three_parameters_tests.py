import pytest


@pytest.mark.param
@pytest.mark.rest
def test1(package_fixture):
    test_one_data = [2, 4, 6, 8]
    for i in test_one_data:
        assert i % 2 == 0


test_two_data = {"value_1": True,
                 "value_2": True,
                 "value_3": True,
                 "value_4": True,
                 "value_5": True, }


@pytest.mark.param
@pytest.mark.parametrize("k,v", [("value_1", True),
                                 ("value_2", True),
                                 ("value_3", True),
                                 ("value_4", True),
                                 ("value_5", True)],
                         ids=["is_working_day", "is_morning", "not_vacation", "not_owner", "not_pensioner"]
)
def test2(package_fixture, k, v):
    assert v == True


test_three_data = [1, 5, 6, 34, "qqq", 22, 43.2, True, (1, 2, 3)]


@pytest.mark.param
@pytest.mark.parametrize("test_three_iter_data", [True, "qqq", (1, 2, 3)], ids=["bool_values", "string", "list"])
def test3(test_three_iter_data):
    assert test_three_iter_data in test_three_data

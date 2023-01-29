import os
import pytest


my_system = os.getcwd()
target_folder = os.path.join(my_system, "HW16", "pack3")


@pytest.mark.pack
@pytest.mark.join
@pytest.mark.xfail(reason="Not root", condition=os.getlogin == "root")
def test_one_one(test_three_fixture):
    print(f"\nYou are {os.getlogin()}")


@pytest.mark.pack
@pytest.mark.rest
def test_two_two(test_three_fixture):
    print(f"\nTest 2 started {os.listdir(target_folder)}")
    for i in os.listdir(target_folder):
        if i == 'conftest.py' :
            print("\n'conftest.py' is in current dir")
        assert 'conftest.py' in os.listdir(target_folder)



@pytest.mark.pack
@pytest.mark.rest
@pytest.mark.skipif(reason= "it`s not posix", condition=os.name != "posix")
def test_three_three(test_three_fixture):
    print("\nPosix test done correctly")


@pytest.mark.pack
@pytest.mark.join
def test_four_four(test_three_fixture):
    print(f"\nyour current dir is {os.getcwd()}")

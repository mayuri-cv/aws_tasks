import pytest

#@pytest.fixture
# def input_value():
#     input = 48
#     return input

def test_divisible_by_4(input_value):
    assert input_value % 4 == 0

def test_divisible_by_7(input_value):
    assert input_value % 7 == 0
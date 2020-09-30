import pytest
from src.calculation import Calculation
#@pytest.fixture
#def input_value():
#    return 374


def test_sum(input_value):
    assert Calculation().sum(input_value, 2) == 376


def test_sub(input_value):
    assert Calculation().sum(input_value, 3) == 6


def test_mul(input_value):
    assert Calculation().sum(input_value, 1) == 25


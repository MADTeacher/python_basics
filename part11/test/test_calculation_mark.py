import pytest
from src.calculation import Calculation

@pytest.mark.calc
def test_sum():
    assert Calculation().sum(3, 2) == 5

@pytest.mark.calc
def test_sub():
    assert Calculation().sub(10, 3) == 6

@pytest.mark.calc
def test_mul():
    assert Calculation().mul(5, 5) == 25

@pytest.mark.calc
def test_div():
    assert Calculation().div(10, 3) == 3

@pytest.mark.pow2
def test_pow2():
    assert Calculation().pow2(10) == 99

@pytest.mark.skip("Не трогать!")
def tes_invisible():
    assert 23 == 1

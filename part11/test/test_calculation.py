from src.calculation import Calculation

def test_sum():
    assert Calculation().sum(3, 2) == 5

def test_sub():
    assert Calculation().sub(10, 3) == 6

def test_mul():
    assert Calculation().mul(5, 5) == 25

def test_div():
    assert Calculation().div(10, 3) == 3

def test_pow2():
    assert Calculation().pow2(10) == 99

def tes_invisible():
    assert 23 == 1

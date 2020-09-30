import pytest
from src.my_pow import *

@pytest.mark.pow2
def test_pow2():
    assert my_pow2(10) == 100

@pytest.mark.pow2
def test_pow2_math():
    assert my_pow2_math(10) == 100

@pytest.mark.pow3
def test_math_pow3():
    assert my_pow3_math(2) == 8

@pytest.mark.skip("Не трогать!")
def tes_notpow():
    assert 23 == 1

#test_pow.py
from src.my_pow import *

def test_pow2():
    assert my_pow2(10) == 100

def test_pow2_math():
    assert my_pow2_math(10) == 100

def test_math_pow3():
    assert my_pow3_math(2) == 8

def tes_notpow():
    assert 23 == 1

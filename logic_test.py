from logic import *

def test_hello():
    res = hello('Ala')
    assert res == 'Hello Ala'


def test_silnia_0():
    assert silnia(0) == 1

def test_silnia_5():
    assert silnia(5) == 120

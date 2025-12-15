from logic import *

def test_hello():
    res = say_hello('Ala')
    assert res == 'Hello Ala'


def test_silnia_0():
    assert factorial(0) == 1

def test_silnia_5():
    assert factorial(5) == 120

import pytest


# @pytest.mark.parametrize("a, b, final", [(2, 6, 8), (5, 10, 15)])
# def setup(a, b, final):
#     assert a + b == final


def testLogin():
    print("Login successful")


def testLogoff():
    print("logoff successful")


def testCalculate():
    assert 2 + 2 == 4

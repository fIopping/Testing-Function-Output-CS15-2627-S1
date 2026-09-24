import pytest


def square(a):
    """Calculate the square of the number.
    :param a: The first factor.
    :product: Calculate the square of the number.
    """
    square = a * a
    return square


def test_square_1():
    assert square(2) == 4

def test_square_2():
    assert square(9) == 81



def division (a: float, b: float) -> float:
    """Multiply a and b.

    :param a: The first factor.
    :param b: The second factor.
    :return: The product.
    """

    product = a / b
    return product

def test_division_1():
    assert division(6, 2) == 3
def test_division_2():
    assert division(7.2, 6.8) == pytest.approx(1.0588235294117647)



def power (a: float, b: float) -> float:
    """Power a and b."""
    product = a ** b
    return product
def test_power_1():
    assert power(6, 2) == 36

def test_power_2():
    assert power(2, 6) == 64
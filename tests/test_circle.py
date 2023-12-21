import pytest
from src.circle import Circle


@pytest.mark.parametrize("radius, expected", [(1, 3.14), (2, 12.56), (3, 28.26)])
def test_area(radius, expected):
    assert Circle(radius).area() == expected


@pytest.mark.parametrize("radius, expected", [(1, 6.28), (2, 12.56), (3, 18.84)])
def test_circumference(radius, expected):
    assert Circle(radius).circumference() == expected


def test_repr(circle):
    assert repr(circle) == "Circle(3)"

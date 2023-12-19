import pytest
from src.circle import Circle


@pytest.fixture
def circle():
    return Circle(3)


@pytest.mark.parametrize("radius, expected", [(1, 3.14), (2, 12.56), (3, 28.26)])
def test_area(radius, expected):
    assert Circle(radius).area() == expected


def test_circumference(circle):
    assert circle.circumference() == 18.84


def test_repr(circle):
    assert repr(circle) == "Circle(3)"

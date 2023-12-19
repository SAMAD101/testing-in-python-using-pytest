import pytest
from src.circle import Circle

@pytest.fixture
def circle():
    return Circle(3)

def test_area(circle):
    assert circle.area() == 28.26

def test_circumference(circle):
    assert circle.circumference() == 18.84

def test_repr(circle):
    assert repr(circle) == "Circle(3)"
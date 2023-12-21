import pytest
from src.circle import Circle

@pytest.fixture
def circle():
    return Circle(3)
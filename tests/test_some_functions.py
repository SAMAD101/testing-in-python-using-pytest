import pytest
import time
import src.some_functions as some_functions


def test_add():
    assert some_functions.add(1, 2) == 3


def test_divide():
    assert some_functions.divide(2, 1) == 2


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        some_functions.divide(1, 0)
    assert str(e.value) == 'division by zero'


def test_add_strings():
    assert some_functions.add('a', 'b') == 'ab'


@pytest.mark.slow
def test_add_slow():
    time.sleep(1)
    assert some_functions.add(1, 2) == 3


@pytest.mark.skip(reason="Not implemented yet")
def test_add():
    assert some_functions.add(1, 2) == 3


@pytest.mark.xfail(reason="Can't divide by zero")
def test_divide_by_zero():
    assert some_functions.divide(1, 0) == 0

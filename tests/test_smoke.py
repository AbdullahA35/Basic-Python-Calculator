import pytest
from calculator import Calculator, add, subtract, multiply, divide

# Group order 100: smoke tests run first. If these fail, nothing else is worth running.
pytestmark = [pytest.mark.unit, pytest.mark.smoke, pytest.mark.order(100)]


def test_package_functions_work():
    assert add(1, 1) == 2
    assert subtract(3, 1) == 2
    assert multiply(2, 2) == 4
    assert divide(4, 2) == 2

def test_calculator_class_works():
    assert Calculator().add(1, 1) == 2

def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

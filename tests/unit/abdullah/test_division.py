import pytest
from calculator.division import divide

# Group order 500 (division): groups run smoke > addition > subtraction > multiplication > division > methods > class > workflow > data-driven.
pytestmark = [pytest.mark.unit, pytest.mark.division, pytest.mark.abdullah, pytest.mark.order(500)]

# Technique: Boundary Value Analysis (zero, identity, equal operands, large values, invalid input).
def test_divide_by_one():
    assert divide(17, 1) == 17

def test_divide_same_number():
    assert divide(12, 12) == 1

def test_divide_zero_numerator():
    assert divide(0, 7) == 0

def test_divide_by_zero_raises_error():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_divide_by_fraction():
    assert divide(1, 0.5) == 2

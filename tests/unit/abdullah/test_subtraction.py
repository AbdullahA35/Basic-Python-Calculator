import pytest
from calculator.subtraction import subtract

# Group order 300 (subtraction): groups run smoke > addition > subtraction > multiplication > division > methods > class > workflow > data-driven.
pytestmark = [pytest.mark.unit, pytest.mark.subtraction, pytest.mark.abdullah, pytest.mark.order(300)]

# Technique: Boundary Value Analysis (zero, identity, equal operands, large values, invalid input).
def test_subtract_zero_identity():
    assert subtract(9, 0) == 9

def test_subtract_same_number():
    assert subtract(123, 123) == 0

def test_subtract_negative_result():
    assert subtract(2, 10) == -8

def test_subtract_large_integers():
    assert subtract(10**12, 1) == 10**12 - 1

def test_subtract_from_zero():
    assert subtract(0, 5) == -5

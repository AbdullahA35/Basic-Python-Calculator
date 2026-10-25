import pytest
from calculator.multiplication import multiply

# Group order 400 (multiplication): groups run smoke > addition > subtraction > multiplication > division > methods > class > workflow > data-driven.
pytestmark = [pytest.mark.unit, pytest.mark.multiplication, pytest.mark.abdullah, pytest.mark.order(400)]

# Technique: Boundary Value Analysis (zero, identity, equal operands, large values, invalid input).
def test_multiply_by_zero():
    assert multiply(999, 0) == 0

def test_multiply_by_one():
    assert multiply(42, 1) == 42

def test_multiply_by_negative_one():
    assert multiply(42, -1) == -42

def test_multiply_large_integers():
    assert multiply(10**6, 10**6) == 10**12

def test_multiply_by_fraction():
    assert multiply(4, 0.5) == 2

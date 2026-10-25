import pytest
from calculator.addition import add

# Group order 200 (addition): groups run smoke > addition > subtraction > multiplication > division > methods > class > workflow > data-driven.
pytestmark = [pytest.mark.unit, pytest.mark.addition, pytest.mark.abdullah, pytest.mark.order(200)]

# Technique: Boundary Value Analysis (zero, identity, equal operands, large values, invalid input).
def test_add_zero_identity():
    assert add(7, 0) == 7

def test_add_negative_and_positive():
    assert add(-10, 4) == -6

def test_add_large_integers():
    assert add(10**12, 10**12) == 2 * 10**12

def test_add_opposites_give_zero():
    assert add(5, -5) == 0

def test_add_strings_concatenate_because_no_input_validation():
    # Documents current behaviour: the function does not validate its input.
    assert add("a", "b") == "ab"

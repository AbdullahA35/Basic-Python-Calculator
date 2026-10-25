import pytest
from subtraction import subtract

# Group order 300 (subtraction): groups run smoke > addition > subtraction > multiplication > division > methods > class > workflow > data-driven.
pytestmark = [pytest.mark.unit, pytest.mark.subtraction, pytest.mark.ahmed, pytest.mark.order(300)]

# Technique: Equivalence Class Partitioning (positive, negative, mixed, zero, decimal).
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (8, 3, 5),
        (3, 8, -5),
        (0, 0, 0),
        (-5, -2, -3),
        (2.5, 1.0, 1.5),
    ],
)
def test_subtract_valid_numbers(a, b, expected):
    assert subtract(a, b) == expected

def test_subtract_decimal_values():
    assert subtract(0.3, 0.1) == pytest.approx(0.2)

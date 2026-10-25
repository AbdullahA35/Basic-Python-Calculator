import pytest
from multiplication import multiply

# Group order 400 (multiplication): groups run smoke > addition > subtraction > multiplication > division > methods > class > workflow > data-driven.
pytestmark = [pytest.mark.unit, pytest.mark.multiplication, pytest.mark.ahmed, pytest.mark.order(400)]

# Technique: Equivalence Class Partitioning (positive, negative, mixed, zero, decimal).
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 6),
        (0, 5, 0),
        (-2, 3, -6),
        (-2, -3, 6),
        (2.5, 4, 10.0),
    ],
)
def test_multiply_valid_numbers(a, b, expected):
    assert multiply(a, b) == expected

def test_multiply_decimal_values():
    assert multiply(0.1, 3) == pytest.approx(0.3)

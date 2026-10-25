import pytest
from addition import add

# Group order 200 (addition): groups run smoke > addition > subtraction > multiplication > division > methods > class > workflow > data-driven.
pytestmark = [pytest.mark.unit, pytest.mark.addition, pytest.mark.ahmed, pytest.mark.order(200)]

# Technique: Equivalence Class Partitioning (positive, negative, mixed, zero, decimal).
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 5),
        (0, 0, 0),
        (-2, -3, -5),
        (-2, 3, 1),
        (2.5, 1.5, 4.0),
    ],
)
def test_add_valid_numbers(a, b, expected):
    assert add(a, b) == expected

def test_add_decimal_values():
    assert add(0.1, 0.2) == pytest.approx(0.3)

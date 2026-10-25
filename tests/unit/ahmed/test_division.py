import pytest
from division import divide

# Group order 500 (division): groups run smoke > addition > subtraction > multiplication > division > methods > class > workflow > data-driven.
pytestmark = [pytest.mark.unit, pytest.mark.division, pytest.mark.ahmed, pytest.mark.order(500)]

# Technique: Equivalence Class Partitioning (positive, negative, mixed, zero, decimal).
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (6, 3, 2),
        (5, 2, 2.5),
        (0, 5, 0),
        (-6, 3, -2),
        (-6, -3, 2),
    ],
)
def test_divide_valid_numbers(a, b, expected):
    assert divide(a, b) == expected

def test_divide_decimal_values():
    assert divide(0.3, 0.1) == pytest.approx(3.0)

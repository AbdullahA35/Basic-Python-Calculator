import pytest
from calculator import Calculator

# Technique: BVA. Each test also checks that the call was recorded in history.
pytestmark = [pytest.mark.unit, pytest.mark.method, pytest.mark.abdullah, pytest.mark.order(600)]

@pytest.fixture
def calc():
    return Calculator()

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (7, 0, 7),
        (0, 0, 0),
        (10**12, 10**12, 2 * 10**12),
        (-1, 1, 0),
        (0.1, 0.2, pytest.approx(0.3)),
    ],
)
def test_calculator_add(calc, a, b, expected):
    assert calc.add(a, b) == expected
    assert calc.history[-1][0] == "add"

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (9, 0, 9),
        (123, 123, 0),
        (10**12, 1, 10**12 - 1),
        (0, 1, -1),
        (-1, -1, 0),
    ],
)
def test_calculator_subtract(calc, a, b, expected):
    assert calc.subtract(a, b) == expected
    assert calc.history[-1][0] == "subtract"

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (999, 0, 0),
        (42, 1, 42),
        (42, -1, -42),
        (10**6, 10**6, 10**12),
        (0, 0, 0),
    ],
)
def test_calculator_multiply(calc, a, b, expected):
    assert calc.multiply(a, b) == expected
    assert calc.history[-1][0] == "multiply"

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (17, 1, 17),
        (12, 12, 1),
        (0, 7, 0),
        (1, -1, -1),
        (-4, 2, -2),
    ],
)
def test_calculator_divide(calc, a, b, expected):
    assert calc.divide(a, b) == expected
    assert calc.history[-1][0] == "divide"

def test_calculator_divide_by_zero_is_not_recorded(calc):
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)
    assert calc.history == []
    assert calc.last_result is None

import pytest
from calculator import Calculator

# Technique: ECP. Each test also checks that the call was recorded in history.
pytestmark = [pytest.mark.unit, pytest.mark.method, pytest.mark.ahmed, pytest.mark.order(600)]

@pytest.fixture
def calc():
    return Calculator()

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 5),
        (-2, -3, -5),
        (-2, 3, 1),
        (2.5, 1.5, 4.0),
        (0, 7, 7),
    ],
)
def test_calculator_add(calc, a, b, expected):
    assert calc.add(a, b) == expected
    assert calc.history[-1][0] == "add"

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (8, 3, 5),
        (3, 8, -5),
        (-5, -2, -3),
        (2.5, 1.0, 1.5),
        (0, 4, -4),
    ],
)
def test_calculator_subtract(calc, a, b, expected):
    assert calc.subtract(a, b) == expected
    assert calc.history[-1][0] == "subtract"

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 6),
        (-2, 3, -6),
        (-2, -3, 6),
        (2.5, 4, 10.0),
        (0, 5, 0),
    ],
)
def test_calculator_multiply(calc, a, b, expected):
    assert calc.multiply(a, b) == expected
    assert calc.history[-1][0] == "multiply"

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (6, 3, 2),
        (5, 2, 2.5),
        (-6, 3, -2),
        (-6, -3, 2),
        (0, 5, 0),
    ],
)
def test_calculator_divide(calc, a, b, expected):
    assert calc.divide(a, b) == expected
    assert calc.history[-1][0] == "divide"

def test_calculator_divide_by_zero_raises(calc):
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)

@pytest.mark.parametrize(
    "operations",
    [
        [("add", 2, 3)],
        [("subtract", 8, 3)],
        [("multiply", 2, 3)],
        [("divide", 6, 3)],
        [("add", 1, 1), ("subtract", 5, 2), ("multiply", 2, 3), ("divide", 9, 3)],
    ],
)
def test_calculator_clear_history(calc, operations):
    for name, a, b in operations:
        getattr(calc, name)(a, b)
    calc.clear_history()
    assert calc.history == []
    assert calc.last_result is None

def test_calculator_works_after_clear_history(calc):
    calc.add(2, 3)
    calc.clear_history()
    assert calc.multiply(4, 5) == 20
    assert calc.history == [("multiply", 4, 5, 20)]

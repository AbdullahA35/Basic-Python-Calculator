import pytest
from calculator.addition import add
from calculator.subtraction import subtract
from calculator.multiplication import multiply
from calculator.division import divide

# Group order 900: data-driven tests run last.
pytestmark = [pytest.mark.unit, pytest.mark.csvdata, pytest.mark.order(900)]

OPERATIONS = {
    "addition": add,
    "subtraction": subtract,
    "multiplication": multiply,
    "division": divide,
}


def test_csv_file_has_enough_rows(calculator_csv_rows):
    assert len(calculator_csv_rows) >= 4


def test_external_csv_case(csv_case):
    """One test per row of tests/data/calculator_cases.csv (see conftest.py)."""
    a = float(csv_case["a"])
    b = float(csv_case["b"])
    expected = float(csv_case["expected"])
    actual = OPERATIONS[csv_case["operation"]](a, b)
    assert actual == pytest.approx(expected)


@pytest.mark.parametrize(
    "operation,a,b,expected",
    [
        ("addition", 2, 3, 5),
        ("subtraction", 7, 2, 5),
        ("multiplication", 3, 4, 12),
        ("division", 8, 2, 4),
    ],
)
def test_parameterized_operation_examples(operation, a, b, expected):
    assert OPERATIONS[operation](a, b) == expected

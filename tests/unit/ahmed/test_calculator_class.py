import pytest
import calculator
from calculator import Calculator

# Class-level tests (state and history), technique: ECP on object state.
pytestmark = [pytest.mark.unit, pytest.mark.class_level, pytest.mark.ahmed, pytest.mark.order(700)]


def test_new_calculator_starts_empty():
    calc = Calculator()
    assert calc.history == []
    assert calc.last_result is None

def test_operation_is_recorded_as_tuple():
    calc = Calculator()
    calc.add(2, 3)
    assert calc.history == [("add", 2, 3, 5)]

def test_last_result_follows_latest_operation():
    calc = Calculator()
    calc.add(2, 3)
    calc.multiply(4, 5)
    assert calc.last_result == 20

def test_history_keeps_call_order():
    calc = Calculator()
    calc.add(1, 1)
    calc.subtract(5, 2)
    calc.divide(9, 3)
    assert [entry[0] for entry in calc.history] == ["add", "subtract", "divide"]

def test_two_calculators_do_not_share_history():
    first, second = Calculator(), Calculator()
    first.add(1, 2)
    assert second.history == []

def test_calculator_is_exported_by_package():
    assert "Calculator" in calculator.__all__
    assert calculator.Calculator is Calculator

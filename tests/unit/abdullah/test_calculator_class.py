import pytest
from calculator import Calculator, add, subtract, multiply, divide

# Class-level tests, technique: BVA on history (empty, one entry, many) and invalid input.
pytestmark = [pytest.mark.unit, pytest.mark.class_level, pytest.mark.abdullah, pytest.mark.order(700)]


def test_clear_history_resets_state():
    calc = Calculator()
    calc.add(1, 2)
    calc.clear_history()
    assert calc.history == []
    assert calc.last_result is None

def test_clear_history_on_empty_calculator_is_safe():
    calc = Calculator()
    calc.clear_history()
    assert calc.history == []

def test_failed_divide_does_not_change_existing_history():
    calc = Calculator()
    calc.add(1, 2)
    with pytest.raises(ZeroDivisionError):
        calc.divide(1, 0)
    assert calc.history == [("add", 1, 2, 3)]
    assert calc.last_result == 3

def test_last_result_can_feed_next_operation():
    calc = Calculator()
    calc.add(2, 3)
    assert calc.multiply(calc.last_result, 4) == 20

def test_history_grows_by_one_per_call():
    calc = Calculator()
    for i in range(10):
        calc.add(i, i)
    assert len(calc.history) == 10

@pytest.mark.parametrize(
    "method,function,a,b",
    [
        ("add", add, 7, 5),
        ("subtract", subtract, 7, 5),
        ("multiply", multiply, 7, 5),
        ("divide", divide, 7, 5),
    ],
)
def test_methods_match_module_functions(method, function, a, b):
    assert getattr(Calculator(), method)(a, b) == function(a, b)

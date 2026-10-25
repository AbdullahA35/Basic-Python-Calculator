"""Ordered, stateful session: one Calculator is shared and each step builds on the last.

The steps use explicit pytest-order indexes (801 to 806). They only make sense
in this order, so the order is set explicitly instead of relying on file layout.
"""
import pytest
from calculator import Calculator

pytestmark = [pytest.mark.unit, pytest.mark.workflow]


@pytest.fixture(scope="module")
def session():
    return Calculator()


@pytest.mark.order(801)
def test_step1_session_starts_empty(session):
    assert session.history == []

@pytest.mark.order(802)
def test_step2_add(session):
    assert session.add(10, 5) == 15

@pytest.mark.order(803)
def test_step3_subtract_from_last_result(session):
    assert session.subtract(session.last_result, 3) == 12

@pytest.mark.order(804)
def test_step4_multiply_last_result(session):
    assert session.multiply(session.last_result, 2) == 24

@pytest.mark.order(805)
def test_step5_divide_last_result_and_check_history(session):
    assert session.divide(session.last_result, 4) == 6
    assert [entry[0] for entry in session.history] == ["add", "subtract", "multiply", "divide"]

@pytest.mark.order(806)
def test_step6_clear_history(session):
    session.clear_history()
    assert session.history == []

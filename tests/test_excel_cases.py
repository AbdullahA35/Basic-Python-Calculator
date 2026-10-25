"""Run the test cases written in test_cases.xlsx (Task 3).

The workbook is the test-case document; this file reads its Input A, Input B
and Expected Result columns and executes every row against the calculator.
"""
import builtins
import importlib
from pathlib import Path

import openpyxl
import pytest

WORKBOOK = Path(__file__).parent.parent / "test_cases.xlsx"

# Group order 900: data-driven tests run last.
pytestmark = [pytest.mark.unit, pytest.mark.excel, pytest.mark.order(900)]


def load_excel_cases():
    sheet = openpyxl.load_workbook(WORKBOOK, read_only=True)["Test Cases"]
    rows = list(sheet.iter_rows(values_only=True))
    header = [str(h) for h in rows[0]]
    return [dict(zip(header, row)) for row in rows[1:] if row[0]]


def resolve(function_path):
    module_name, function_name = function_path.split(".")
    return getattr(importlib.import_module(f"calculator.{module_name}"), function_name)


CASES = [
    pytest.param(case, id=case["Test Case ID"], marks=getattr(pytest.mark, case["Author"].lower()))
    for case in load_excel_cases()
]


def test_workbook_has_enough_cases():
    assert len(CASES) >= 4


@pytest.mark.parametrize("case", CASES)
def test_excel_case(case):
    function = resolve(case["Module / Function"])
    a, b = case["Input A"], case["Input B"]
    expected = str(case["Expected Result"])
    if expected.endswith("Error"):
        with pytest.raises(getattr(builtins, expected)):  # e.g. ZeroDivisionError
            function(a, b)
    else:
        assert function(a, b) == pytest.approx(float(expected))

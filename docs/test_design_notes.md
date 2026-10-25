# Test design notes: ECP and BVA

Ahmed's tests concentrate on **Equivalence Class Partitioning (ECP)**; Abdullah's concentrate on
**Boundary Value Analysis (BVA)** and invalid input. Both apply to every module.

## Equivalence classes (all four operations)

| Class | Example inputs | Expected |
|---|---|---|
| Positive operands | add(2,3); subtract(8,3); multiply(2,3); divide(6,3) | 5; 5; 6; 2 |
| Negative operands | add(-2,-3); subtract(-5,-2); multiply(-2,-3); divide(-6,-3) | -5; -3; 6; 2 |
| Mixed signs | add(-2,3); multiply(-2,3); divide(-6,3) | 1; -6; -2 |
| Result below zero | subtract(3,8) | -5 |
| Zero operand | add(0,0); multiply(0,5); divide(0,5) | 0; 0; 0 |
| Decimal operands | add(2.5,1.5); multiply(2.5,4); divide(5,2) | 4.0; 10.0; 2.5 |
| Invalid divisor | divide(10,0) | `ZeroDivisionError` |

## Boundary values

| Boundary | Values | Expected |
|---|---|---|
| Zero (identity for + and -) | add(7,0); subtract(9,0) | 7; 9 |
| Zero (absorbing for *) | multiply(999,0) | 0 |
| 1 and -1 (identity / sign flip) | multiply(42,1); multiply(42,-1); divide(17,1) | 42; -42; 17 |
| Equal operands | subtract(123,123); divide(12,12) | 0; 1 |
| Sign change of result | subtract(3,8); subtract(8,3) | -5; 5 |
| Divisor boundary | divide(10,0); divide(17,1) | error; 17 |
| Large magnitude | add(10^12,10^12); multiply(10^6,10^6) | exact integers |
| Floating point | add(0.1,0.2); divide(0.3,0.1) | approx 0.3; approx 3.0 |
| Non-numeric input | add("a","b") | "ab" (no validation, documented behaviour) |

## `Calculator` class

| Technique | Cases |
|---|---|
| ECP on state | new object (empty history, `last_result` None); one entry; several entries in call order; two independent instances |
| BVA on history size | empty after `clear_history`; `clear_history` on an empty object; exactly 10 entries |
| ECP on `clear_history()` | history holding one entry of each operation type (add, subtract, multiply, divide); history holding several mixed entries; reuse of the object after clearing |
| Invalid input | failed `divide` leaves history and `last_result` unchanged |
| Consistency | every method returns the same value as the matching module function |

## Where each design is automated

| Level | Location |
|---|---|
| Function (module functions) | `tests/unit/<person>/test_<operation>.py` |
| Function of a class (methods) | `tests/unit/<person>/test_calculator_methods.py` |
| Class | `tests/unit/<person>/test_calculator_class.py`, `tests/workflow/` |
| External data | `tests/data/calculator_cases.csv`, `test_cases.xlsx` |

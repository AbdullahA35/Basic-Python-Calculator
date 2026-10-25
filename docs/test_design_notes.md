# Test design notes: ECP

Ahmed's tests focus on Equivalence Class Partitioning (ECP).

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

## `Calculator` class (ECP)

- New object: empty history and `last_result` is `None`.
- One recorded operation, several operations in call order, and two independent instances.
- `clear_history()` after one entry of each operation, after several mixed entries, and reuse after clearing.
- A failed division leaves history and `last_result` unchanged.
- Each class method returns the same value as its matching module function.

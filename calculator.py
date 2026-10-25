"""Calculator class that wraps the four operations and keeps a history."""
from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide


class Calculator:
    """Run arithmetic operations and remember what was calculated.

    ``history`` holds one ``(operation, a, b, result)`` tuple per successful
    operation. A call that raises (for example divide by zero) is not recorded.
    """

    def __init__(self):
        self.history = []
        self.last_result = None

    def _record(self, operation, a, b, result):
        self.history.append((operation, a, b, result))
        self.last_result = result
        return result

    def add(self, a, b):
        """Return a + b and record it."""
        return self._record("add", a, b, add(a, b))

    def subtract(self, a, b):
        """Return a - b and record it."""
        return self._record("subtract", a, b, subtract(a, b))

    def multiply(self, a, b):
        """Return a * b and record it."""
        return self._record("multiply", a, b, multiply(a, b))

    def divide(self, a, b):
        """Return a / b and record it; raise ZeroDivisionError when b is zero."""
        return self._record("divide", a, b, divide(a, b))

    def clear_history(self):
        """Forget all recorded operations and the last result."""
        self.history.clear()
        self.last_result = None

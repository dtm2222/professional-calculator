"""Calculation classes and factory for the calculator."""

from app.operation import add, subtract, multiply, divide


class Calculation:
    """Represents a single calculator calculation."""

    def __init__(self, a: float, b: float, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def perform(self) -> float:
        """Perform and return the calculation."""
        return self.operation(self.a, self.b)


class CalculationFactory:
    """Creates Calculation objects based on an operation name."""

    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    @classmethod
    def create(cls, operation_name: str, a: float, b: float) -> Calculation:
        """Create and return the requested calculation."""
        if operation_name not in cls.operations:
            raise ValueError(f"Unknown operation: {operation_name}")

        operation = cls.operations[operation_name]
        return Calculation(a, b, operation)
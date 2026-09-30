"""Command-line calculator application."""

from app.calculation import CalculationFactory


class Calculator:
    """Manages calculator operations, history, and user interaction."""

    def __init__(self):
        self.history = []

    def calculate(self, operation: str, a: float, b: float) -> float:
        """Perform a calculation and store it in history."""
        calculation = CalculationFactory.create(operation, a, b)
        result = calculation.perform()

        self.history.append((operation, a, b, result))

        return result

    def show_history(self):
        """Return the calculation history."""
        return self.history

    def clear_history(self):
        """Clear all calculations from history."""
        self.history.clear()


def run():
    """Run the calculator REPL."""
    calculator = Calculator()

    print("Professional Calculator")
    print("Type 'help' for commands.")

    while True:
        command = input("\nEnter operation: ").strip().lower()

        # LBYL: check the command before trying to use it
        if command == "exit":
            print("Goodbye!")
            break

        if command == "help":
            print("Commands: add, subtract, multiply, divide, history, exit")
            continue

        if command == "history":
            history = calculator.show_history()

            if not history:
                print("No calculations in history.")
            else:
                for operation, a, b, result in history:
                    print(f"{operation}: {a}, {b} = {result}")
            continue

        if command not in ["add", "subtract", "multiply", "divide"]:
            print("Invalid operation. Type 'help' for available commands.")
            continue

        # EAFP: try the operation and handle errors if they occur
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            result = calculator.calculate(command, a, b)
            print(f"Result: {result}")

        except ValueError as error:
            print(f"Error: {error}")


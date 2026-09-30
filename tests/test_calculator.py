import pytest

from app.calculator import Calculator, run

def test_calculator_add():
    calculator = Calculator()
    result = calculator.calculate("add", 10, 5)

    assert result == 15


def test_calculator_history():
    calculator = Calculator()

    calculator.calculate("add", 10, 5)
    calculator.calculate("multiply", 4, 3)

    assert calculator.show_history() == [
        ("add", 10, 5, 15),
        ("multiply", 4, 3, 12),
    ]


def test_clear_history():
    calculator = Calculator()

    calculator.calculate("add", 10, 5)
    calculator.clear_history()

    assert calculator.show_history() == []


def test_calculator_invalid_operation():
    calculator = Calculator()

    with pytest.raises(ValueError, match="Unknown operation"):
        calculator.calculate("power", 2, 3)


def test_calculator_divide_by_zero():
    calculator = Calculator()

    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.calculate("divide", 10, 0)






def test_repl_add_and_exit(monkeypatch, capsys):
     inputs = iter(["add", "10", "5", "exit"])
     monkeypatch.setattr("builtins.input", lambda _: next(inputs))

     run()

     output = capsys.readouterr().out

     assert "Professional Calculator" in output
     assert "Result: 15.0" in output
     assert "Goodbye!" in output


def test_repl_help(monkeypatch, capsys):
    inputs = iter(["help", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run()

    output = capsys.readouterr().out

    assert "Commands: add, subtract, multiply, divide, history, exit" in output


def test_repl_empty_history(monkeypatch, capsys):
    inputs = iter(["history", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run()

    output = capsys.readouterr().out

    assert "No calculations in history." in output


def test_repl_history_with_calculation(monkeypatch, capsys):
    inputs = iter(["add", "4", "3", "history", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run()

    output = capsys.readouterr().out

    assert "add: 4.0, 3.0 = 7.0" in output


def test_repl_invalid_operation(monkeypatch, capsys):
    inputs = iter(["power", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run()

    output = capsys.readouterr().out

    assert "Invalid operation" in output


def test_repl_invalid_number(monkeypatch, capsys):
    inputs = iter(["add", "hello", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run()

    output = capsys.readouterr().out

    assert "Error:" in output


def test_repl_divide_by_zero(monkeypatch, capsys):
    inputs = iter(["divide", "10", "0", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run()

    output = capsys.readouterr().out

    assert "Cannot divide by zero" in output


def test_main_module(monkeypatch):
    monkeypatch.setattr("app.calculator.run", lambda: None)

    import runpy
    runpy.run_module("app.calculator", run_name="__main__")
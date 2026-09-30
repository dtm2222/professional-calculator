import pytest

from app.calculation import Calculation, CalculationFactory
from app.operation import add


def test_calculation_perform():
    calculation = Calculation(5, 3, add)
    assert calculation.perform() == 8


@pytest.mark.parametrize(
    "operation_name, a, b, expected",
    [
        ("add", 5, 3, 8),
        ("subtract", 5, 3, 2),
        ("multiply", 5, 3, 15),
        ("divide", 6, 3, 2),
    ],
)
def test_calculation_factory(operation_name, a, b, expected):
    calculation = CalculationFactory.create(operation_name, a, b)
    assert calculation.perform() == expected


def test_calculation_factory_invalid_operation():
    with pytest.raises(ValueError, match="Unknown operation"):
        CalculationFactory.create("power", 5, 3)
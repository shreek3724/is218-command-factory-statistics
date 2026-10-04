"""A calculation stores inputs and a callable, without executing it yet."""
from math import isfinite
from calculator.operations import Operations
from calculator.validation import numeric_values


class Calculation:
    def __init__(self, values, operation, **options):
        self.values = numeric_values(values)
        self.operation = operation
        self.options = dict(options)

    def get_result(self) -> float:
        
        result = float(self.operation(*self.values, **self.options))
        
        if not isfinite(result):
            raise ValueError("Result is outside the supported range.")
        return result

    """added to finish completion problem in part 1"""
    def test_stored_subtract_operation():
        calculation = Calculation([10,4], Operations.subtract)
        assert calculation.get_result() == 6

    """added to finish independent problem in part 1"""
    def test_stored_abs_diff_operation():
        calculation = Calculation([3,9], Operations.abs_diff)
        assert calculation.get_result() == 6
"""A calculation stores inputs and a callable, without executing it yet."""
from math import isfinite
from calculator.operations import Operations
from calculator.validation import numeric_values


class Calculation:
    def __init__(self, values, operation, **options):
        """new init class that can normalize inputs to a tuple sequence of finite floats"""
        """done as work for compeltion/independent task in Part 3"""
        self.values = tuple(numeric_values(values))
        self.operation = operation
        # below stores the configuration dictionary:
        self.options = dict(options)

        """
        self.values = numeric_values(values)
        self.operation = operation
        self.options = dict(options)
        """

    def get_result(self) -> float:
        """as part of Part 3 competion/indepdendent task"""
        """unpacks stored potional tuple and options dict into the callable"""
        result = float(self.operation(*self.values, **self.options))
        if not isfinite(result):
            raise ValueError("Result is outside the supported range.")
        return result

        """
        result = float(self.operation(*self.values, **self.options))
        
        if not isfinite(result):
            raise ValueError("Result is outside the supported range.")
        return result
        """

    """added to finish completion problem in part 1"""
    def test_stored_subtract_operation():
        calculation = Calculation([10,4], Operations.subtract)
        assert calculation.get_result() == 6

    """added to finish independent problem in part 1"""
    def test_stored_abs_diff_operation():
        calculation = Calculation([3,9], Operations.abs_diff)
        assert calculation.get_result() == 6
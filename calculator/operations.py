"""Stateless mathematical operations: no prompts, files, or history."""
from math import pow, sqrt
from calculator.statistics import mean, standard_deviation


class Operations:
    @staticmethod
    def add(a, b) -> float:
        return a + b

    @staticmethod
    def subtract(a, b) -> float:
        return a - b

    @staticmethod
    def multiply(a, b) -> float:
        return a * b

    @staticmethod
    def divide(a, b) -> float:
        # EAFP: the arithmetic operation already detects a zero divisor.
        return a / b

    @staticmethod
    def square(value) -> float:
        return value * value

    @staticmethod
    def sqrt(value) -> float:
        return sqrt(value)

    @staticmethod
    def power(value, *, exponent=2) -> float:
        return pow(value, exponent)

    @staticmethod
    def sum(*values) -> float:
        if not values:
            raise ValueError("Enter at least one value.")
        return sum(values)

    @staticmethod
    def mean(*values) -> float:
        return mean(values)

    @staticmethod
    def stddev(*values, ddof=1) -> float:
        return standard_deviation(values, ddof=ddof)

    """added as part of independent part of assignment part 1 or 2"""
    @staticmethod
    def abs_diff(a, b) -> float:
        """Calculates the absolute difference between two numbers."""
        return abs(a - b)

    """added as indepdendent problem part of part 3"""
    @staticmethod
    def divide_by_factor(value: float, *, factor: float = 1.0) -> float:
        """unary operation dividing a single value by a keyword factor"""
        if factor == 0:
            raise ZeroDivisionError("Factor cannot be zero.")
        return value / factor

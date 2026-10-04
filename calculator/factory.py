"""Select a static operation and construct an unexecuted Calculation."""
from calculator.calculation import Calculation
from calculator.operations import Operations
from calculator.validation import numeric_values

"""during part 3, added divide_by_factor in operations, operand counts, and allowed options"""

class CalculationFactory:
    operations = {
        "add": Operations.add,
        "subtract": Operations.subtract,
        "multiply": Operations.multiply,
        "divide": Operations.divide,
        "square": Operations.square,
        "sqrt": Operations.sqrt,
        "power": Operations.power,
        "sum": Operations.sum,
        "mean": Operations.mean,
        "stddev": Operations.stddev,
        "abs_diff": Operations.abs_diff, 
        #added abs_diff to complete the independent problem in part 2
        "divide_by_factor": Operations.divide_by_factor
        #added divide_by_factor to complete the independent problem in part 3
    }
    operand_counts = {
        "add": 2, "subtract": 2, "multiply": 2, "divide": 2,
        "square": 1, "sqrt": 1, "power": 1,
        "abs_diff": 2, #added to complete the independent problem in part 2
        "divide_by_factor": 1, #added to complete the independent problem in part 3
    }
    allowed_options = {"power": {"exponent"}, "stddev": {"ddof"}, "divide_by_factor": {"factor"}}  #added divide_by_factor to complete the independent problem in part 3, by enabling factor option

    @staticmethod
    def create(name: str, *values, **options) -> Calculation:
        name = name.strip().lower()
        try:
            operation = CalculationFactory.operations[name]
        except KeyError:
            raise ValueError(f"Unknown operation: {name}") from None

        allowed = CalculationFactory.allowed_options.get(name, set())
        converted_options = {}
        for key, value in options.items():
            if key not in allowed:
                raise ValueError(f"Unsupported option for {name}: {key}")
            converted_options[key] = numeric_values([value])[0]

        count = CalculationFactory.operand_counts.get(name)
        if count is not None and len(values) != count:
            raise ValueError(f"{name} requires exactly {count} value(s).")
        return Calculation(values, operation, **converted_options)

import pytest
from calculator.calculation import Calculation
from calculator.factory import CalculationFactory


@pytest.mark.parametrize('name,values,expected', [(' ADD ', ['2', '3'], 5), ('subtract', [2, 3], -1), ('multiply', [2, 3], 6), ('divide', [7, 2], 3.5), ('mean', [2, 4, 6], 4), ('stddev', [2, 4, 6], 2)])

def test_factory_configures_calculation(name, values, expected):
    calculation = CalculationFactory.create(name, *values)
    assert isinstance(calculation, Calculation)
    assert calculation.get_result() == pytest.approx(expected)


@pytest.mark.parametrize('name,values', [('unknown', [1, 2]), ('add', [1]), ('add', [1, 2, 3]), ('add', ['x', '2']), ('add', [1, float('inf')])])

def test_factory_rejects_invalid_request(name, values):
    with pytest.raises(ValueError):
        CalculationFactory.create(name, *values)


def test_factory_does_not_execute():
    calculation = CalculationFactory.create('divide', *[1, 0])
    with pytest.raises(ZeroDivisionError):
        calculation.get_result()


@pytest.mark.parametrize("name,values,options,expected", [
    ("square", [3], {}, 9), ("sqrt", [9], {}, 3),
    ("power", [3], {"exponent": "4"}, 81),
    ("stddev", [2, 4, 6], {"ddof": 0}, (8 / 3) ** .5),
])

def test_argument_counts_and_named_options(name, values, options, expected):
    assert CalculationFactory.create(name, *values, **options).get_result() == pytest.approx(expected)



@pytest.mark.parametrize("name,values,options", [
    ("square", [1, 2], {}), ("sqrt", [], {}),
    ("add", [1, 2], {"exponent": 2}), ("power", [2], {"exponent": "x"}),
])

def test_reject_invalid_argument_contract(name, values, options):
    with pytest.raises(ValueError):
        CalculationFactory.create(name, *values, **options)

"""added 3 below tests to complete independent problem as part of part 2"""
def test_factory_abs_diff_operaton():
    """verifies abs_diff constructs through factory and calculates absolute difference."""
    calc = CalculationFactory.create('abs_diff', 3, 9)
    assert calc.get_result() == 6

def test_factory_abs_diff_normalization():
    """verifies that name normalization works for abs_diff with mix casing and padding"""
    calc = CalculationFactory.create(' AbS_dIfF ', 3, 9)
    assert calc.get_result() == 6

def test_factory_abs_diff_invalid_operand_count():
    """verifies that abs_diff fails if not provided exactly 2 operands"""
    with pytest.raises(ValueError, match=r"abs_diff requires exactly 2 value\(s\)\."):
        CalculationFactory.create('abs_diff', 3)

"""part 3 independent tests for divide_by_factor"""
def test_divde_by_factor_success():
    """verifies unary operation works with both custom and defult factor"""
    calc_custom = CalculationFactory.create('divide_by_factor', 10, factor=2)
    assert calc_custom.get_result() == 5
    calc_default = CalculationFactory.create('divide_by_factor', 10)
    assert calc_default.get_result() == 10

def test_divide_by_factor_option_faliure():
    """verfies that unsupported options raise ValueError during factory creation"""
    with pytest.raises(ValueError, match=r"Unsupported option for divide_by_factor:"):
        CalculationFactory.create('divide_by_factor', 10, invalid_option=5)

def test_divide_by_factor_domain_failure():
    """verifies that factor=0 passes creation but deffers a ZeroDivisionError to get_result()."""
    calc = CalculationFactory.create('divide_by_factor', 10, factor=0)
    with pytest.raises(ZeroDivisionError, match="Factor cannot be zero"):
        calc.get_result()
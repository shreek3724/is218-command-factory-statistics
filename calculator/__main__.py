from calculator.cli import run
from calculator.factory import CalculationFactory

'''
if __name__ == "__main__":
    run()
'''

print(CalculationFactory.create("add", 2, 3).get_result())
print(CalculationFactory.create("power", 3, exponent=4).get_result())
import sys
from pkg.calculator import Calculator

calculator = Calculator()
result = calculator.evaluate("10 // 2")
print(f"Result: {result}")
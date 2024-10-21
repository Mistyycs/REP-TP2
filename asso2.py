import random
import numpy as np
from decimal import Decimal, getcontext
# Set the decimal precision (DPS) to 50
getcontext().prec = 50

def associativity() -> bool:
    x = random.random()
    y = random.random()
    z = random.random()
    return Decimal(x) + Decimal(Decimal(y) + Decimal(z)) == Decimal(Decimal(x) + Decimal(y)) + Decimal(z)

def test_associativity(number_iterations: int) -> None:
    number_not_ok = 0
    for i in range(number_iterations):
        if not associativity():
            number_not_ok += 1
    print(f"Number of associative operations: {number_iterations-number_not_ok} out of {number_iterations}")
    print(f"Percentage of associative operations: {(1-number_not_ok/number_iterations)*100}%")


def main():
    test_associativity(10000)

if __name__ == "__main__":
    main()
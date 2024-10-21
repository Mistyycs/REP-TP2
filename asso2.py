import random
from decimal import Decimal, getcontext
# Set the decimal precision (DPS) to 60
# More accurate than default precision of float python -> give 100% of associativity
getcontext().prec = 60

def associativity() -> bool:
    x = random.random()
    y = random.random()
    z = random.random()
    return Decimal(x) + (Decimal(y) + Decimal(z)) == (Decimal(x) + Decimal(y)) + Decimal(z)

def test_associativity(number_iterations: int) -> None:
    number_not_ok = 0
    for i in range(number_iterations):
        if not associativity():
            number_not_ok += 1
    resultat = round(((1-number_not_ok/number_iterations)*100),2)
    print(resultat)


def main():
    test_associativity(10000)

if __name__ == "__main__":
    main()
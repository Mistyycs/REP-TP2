
import numpy as np

def associativity() -> bool:
    x = np.random.rand()
    y = np.random.rand()
    z = np.random.rand()
    return (x + y) + z == x + (y + z)

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
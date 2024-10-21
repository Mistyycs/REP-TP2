import random
import numpy

def check_property(repetitions) -> bool:
    correct_count = 0
    for _ in range(repetitions):
        x = random.random()
        y = random.random()
        z = random.random()

        # Check if the associative property holds
        result1 = x + y
        result2 = y + x
        if result1 == result2:
            correct_count += 1
        
    print(f"Percentage of trials where associativity works : {round(correct_count/repetitions*100,2)}, number of repetitions : {repetitions}.")

# Define the number of repetitions
repetitions = 10000

#Call the function
check_property(repetitions)
import random

N = 1000

def main() : 
    i = 0
    good_answers = 0
    while(i<N) :
        x = random.random()
        y = random.random()
        z = random.random()
        if((x+y)+z == x+(y+z)) : 
            good_answers += 1
        i+=1
    print(f"Fraction de bonnes réponses : {good_answers} sur {N}\n")


main()
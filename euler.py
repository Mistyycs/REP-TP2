from mpmath import mp
import matplotlib.pyplot as plt
def main():
    # Stocker les valeurs d'e pour chaque niveau de précision
    # Fonctionne à partir d'une précision de mp.dps = 63
    results = {}
    for i in range(30, 100):
        mp.dps = i
        e = mp.mpf('2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274')
        for j in range(1, 50):
            e = mp.mpf(e - 1) * j
        results[i] = e
    
    for i, e in results.items():
        print(f"i : {i}, e : {float(e)}")
    return e

if __name__ == "__main__":
    main()


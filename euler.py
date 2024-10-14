from decimal import *
from mpmath import mp
def main():
    mp.dps = 100
    e = mp.mpf('2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274')
    for i in range(1,50) : 
        e = mp.mpf(e-1)*i
        print(f"i : {i} , e :{e}")
    return e

if __name__ == "__main__":
    main()


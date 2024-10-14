#include <iostream>
#include <random>

class Associativity{
    private :
      double x,y,z;

    public :
        Associativity(){    
            x = 0.1;
            y = 0.2;
            z = 0.3;   
        }

    int main(int argc, int** argv){
        Associativity a;
        int res = (x+y)+z == x+(y+z);
        std::cout << res;
        return 0;
    }
};
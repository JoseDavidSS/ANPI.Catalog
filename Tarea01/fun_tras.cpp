#include "fun_tras.h"

using namespace std;

int main(){
    for (double i = -1; i <=1; i+=0.1)
    {
        cout << "sin(" << i << ") = " << sin_t(i) << endl;
    }
}
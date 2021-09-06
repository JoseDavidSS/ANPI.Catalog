#include "fun_tras.h"

using namespace std;

int main(){
    exp_t(-9);
    for (int i = -5; i < 6; i++)
    {
        cout << "arcsin(" << i << ") = " << asin_t(i) << endl;
    }
}
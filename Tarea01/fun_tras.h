#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;
const double EPS = 2.220446049250313e-16;
const int ITER_MAX = 5000;
const double TOL = 1e-8;

long double factorial(int x)
{
    long double factorial = 1.0;
    for (int i = 1; i <= x; ++i)
    {
        factorial *= i;
    }
    return factorial;
}

const long double fact_100 = factorial(100);
const long double fact_80 = factorial(80);
const long double fact_60 = factorial(60);
const long double fact_40 = factorial(40);
const long double fact_20 = factorial(20);
const long double fact_0 = factorial(0);

double divt(int a)
{
    double x_0 = EPS;
    if (a <= fact_100 && a >= fact_80)
    {
        x_0 = pow(EPS, 15.0);
    }
    if (a <= fact_80 && a >= fact_60)
    {
        x_0 = pow(EPS, 11.0);
    }
    if (a <= fact_60 && a >= fact_40)
    {
        x_0 = pow(EPS, 8);
    }
    if (a <= fact_40 && a >= fact_20)
    {
        x_0 = pow(EPS, 4);
    }
    if (a <= fact_20 && a >= fact_0)
    {
        x_0 = pow(EPS, 2);
    }
    int cont = 0;
    double error = 0;
    double x_ksiguiente;
    while (cont < ITER_MAX || error > TOL)
    {
        x_ksiguiente = x_0 * (2 - a * x_0);
        error = abs((x_ksiguiente - x_0) / x_ksiguiente);
        x_0 = x_ksiguiente;
        cont++;
    }
    cout << "x_k1 " << x_ksiguiente << " "
         << " iters: " << cont << endl;
    return x_ksiguiente;
}
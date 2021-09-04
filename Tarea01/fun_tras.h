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
    while (cont < ITER_MAX and error > TOL)
    {
        x_ksiguiente = x_0 * (2 - a * x_0);
        error = abs((x_ksiguiente - x_0) / x_ksiguiente);
        x_0 = x_ksiguiente;
        cont++;
    }
    cout << "x_k1 " << x_ksiguiente << " "
         << " iters: " << x_0 << endl;
    return x_ksiguiente;
}



/**
 * @brief Funcion f(a), donde f(a) = sen(a)
 *
 * @param a valor de a
 * @return double resultado de evaluar f(a)
 */
double sen_t(int a)
{
    if(a < 0){
        cout << "Debe ingresar un número mayor a 0";
        return 0;
    }
    double x_knext;
    double n = 0;
    double x_k = 0;
    double fact;
    double stopCriteria = 1;
    while ((stopCriteria > TOL) && (n < ITER_MAX))
    {
        fact = factorial(2 * n + 1);
        x_knext = x_k + (pow(-1, n) * (pow(a, 2 * n + 1) * (1/fact)));
        stopCriteria = abs(x_knext - x_k);
        n++;
        x_k = x_knext;
    }
    cout << "x_k1 " << x_k << " "
         << " iters: " << n << endl;
    return x_k;
}


/**
 * @brief Funcion f(a), donde f(a) = e ^ a
 *
 * @param a valor de a
 * @return double resultado de evaluar f(a)
 */
double exp_t(int a)
{
    if(a < 0){
        cout << "Debe ingresar un número mayor a 0";
        return 0;
    }
    double n = 0;
    double x_k = 0;
    double x_knext;
    double fact;
    double stopCriteria = 1;
    while ((stopCriteria > TOL) && (n < ITER_MAX))
    {
        fact = factorial(n);
        x_knext = x_k + pow(a, n) * (1/fact);
        stopCriteria = abs(x_knext - x_k);
        n++;
        x_k = x_knext;
    }
    cout << "x_k1 " << x_k << " "
         << " iters: " << n << endl;
    return x_k;
}


/**
 * @brief Funcion f(a), donde f(a) = cos(a)
 *
 * @param a valor de a
 * @return double resultado de evaluar f(a)
 */
double cos_t(int a)
{
    if(a < 0){
        cout << "Debe ingresar un número mayor a 0";
        return 0;
    }
    double x_knext;
    double n = 0;
    double x_k = 0;
    double fact;
    double stopCriteria = 1;
    while ((stopCriteria > TOL) && (n < ITER_MAX))
    {
        fact = factorial(2 * n);
        x_knext = x_k + (pow(-1, n) * (pow(a, 2 * n) * (1/fact)));
        stopCriteria = abs(x_knext - x_k);
        n++;
        x_k = x_knext;
    }
    cout << "x_k1 " << x_k << " "
         << " iters: " << n << endl;
    return x_k;
}


/**
 * @brief Funcion f(a), donde f(a) = ln(a)
 *
 * @param a valor de a
 * @return double resultado de evaluar f(a)
 */
double ln_t(double a)
{
    if(a < 0){
        cout << "Debe ingresar un número mayor a 0";
        return 0;
    }
    double x_knext;
    double n = 0;
    double x_k = 0;
    double formula;
    double stopCriteria = 1;
    formula = (a - 1) / (a + 1);
    while ((stopCriteria > TOL) && (n < ITER_MAX))
    {
        x_knext = (x_k + (1 / (2 * n + 1)) * pow(formula, 2 * n));
        stopCriteria = abs(x_knext - x_k);
        n++;
        x_k = x_knext;
    }
    x_k = x_k * 2 * formula;
    cout << "x_k1 " << x_k<< " "
         << " iters: " << n << endl;
    return x_k;
}

/**
 * @brief Se obtiene la constante pi al aproximar utilizando
 * la suma parcial de la serie de Leibniz
 *
 * @return pi
 */
double pi() {
    int i = 0;
    double pi = 0;
    double pi_next;
    double stopCriteria = 1;
    while ((stopCriteria > TOL) && (i < ITER_MAX)) {
        pi_next = pi + pow(-1, i) * (4.0 / (2.0 * i + 1));
        stopCriteria = abs(pi_next - pi);
        i++;
        pi = pi_next;
    }
    cout << "x_k1 " << pi << " "
         << " iters: " << i << endl;
    return pi;
}

#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;
//double base = ( sin_t(3 * divt(7)) + ln_t(2));
//(divt(cos_t(2)) * (root_t(base, 3))) + log(pi(), exp_t(-1));
/**
 * @brief Constantante epsilon 
 * 
 */
const double EPS = 2.220446049250313e-16;
/**
 * @brief Constante para las maximas iteraciones posibles
 * 
 */
const int ITER_MAX = 5000;
/**
 * @brief Constante para la constante de tolerancia de error
 * 
 */
const double TOL = 1e-8;

/**
 * @brief Checks if a number is even or odd
 *
 * @param x
 * @return double
 */
bool isEven(int n)
{
    bool result;
    if (n % 2 == 0)
    {
        result = true;
    }
    else
    {
        result = false;
    }
    return result;
}

/**
 * @brief Implementation for f(x) = x!
 * 
 * @param x 
 * @return double 
 */
double factorial(double x)
{
    long double factorial = 1.0;
    for (int i = 1; i <= x; ++i)
    {
        factorial *= i;
    }
    return factorial;
}

const double fact_100 = factorial(100);
const double fact_80 = factorial(80);
const double fact_60 = factorial(60);
const double fact_40 = factorial(40);
const double fact_20 = factorial(20);
const double fact_0 = factorial(0);

/**
 * @brief Implementation for f(number) = 1/number
 * 
 * @param number 
 * @return double 
 */
double divt(double number)
{
    double a = abs(number);
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
    double error = 1;
    double x_ksiguiente;
    while (cont < ITER_MAX && error > TOL)
    {
        x_ksiguiente = x_0 * (2 - a * x_0);
        error = abs((x_ksiguiente - x_0) / x_ksiguiente);
        x_0 = x_ksiguiente;
        cont++;
    }
    return (number > 0) ? x_ksiguiente : x_ksiguiente * (-1);
}

/**
 * @brief Funcion f(a), donde f(a) = e ^ a
 *
 * @param a valor de a
 * @return double resultado de evaluar f(a)
 */
double exp_t(double a)
{

    double n = 0;
    double x_k = 0;
    double x_knext;
    double fact;
    double stopCriteria = 1;
    while ((stopCriteria > TOL) && (n < ITER_MAX))
    {
        fact = factorial(n);
        x_knext = x_k + pow(a, n) * (divt(fact));
        stopCriteria = abs(x_knext - x_k);
        n++;
        x_k = x_knext;
    }

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
    if (a < 0)
    {
        cout << "Debe ingresar un numero mayor a 0" << endl;
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
        x_knext = (x_k + (divt(2 * n + 1)) * pow(formula, 2 * n));
        stopCriteria = abs(x_knext - x_k);
        n++;
        x_k = x_knext;
    }
    x_k = x_k * 2 * formula;
    return x_k;
}

/**
 * @brief Implementation for f(base) = base^exponent
 *
 * @param base
 * @param exponent
 * @return double
 */
double power_t(double base, double exponent)
{
    return (base >= 0) ? exp_t(ln_t(base) * exponent) : NULL;
}

/**
 * @brief Funcion f(a), donde f(a) = sen(a)
 *
 * @param a valor de a
 * @return double resultado de evaluar f(a)
 */
double sin_t(double a)
{
    double x_knext;
    double n = 0;
    double x_k = 0;
    double fact;
    double stopCriteria = 1;
    while ((stopCriteria > TOL) && (n < ITER_MAX))
    {
        fact = factorial(2 * n + 1);
        if (isEven(n))
        {
            x_knext = x_k + 1 * (pow(a, 2 * n + 1) * divt(fact));
        }
        else
        {
            x_knext = x_k + -1 * (pow(a, 2 * n + 1) * divt(fact));
        }
        stopCriteria = abs(x_knext - x_k);
        n++;
        x_k = x_knext;
    }

    return x_k;
}

/**
 * @brief Funcion f(a), donde f(a) = cos(a)
 *
 * @param a valor de a
 * @return double resultado de evaluar f(a)
 */
double cos_t(double a)
{
    if (a < 0)
    {
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
        if (isEven(n))
        {
            x_knext = x_k + 1 * (pow(a, 2 * n) * divt(fact));
        }
        else
        {
            x_knext = x_k + -1 * (pow(a, 2 * n) * divt(fact));
        }
        stopCriteria = abs(x_knext - x_k);
        n++;
        x_k = x_knext;
    }

    return x_k;
}

/**
 * @brief Implementation for f(a)=tan(a)
 * 
 * @param a 
 * @return double 
 */
double tan_t(double a)
{
    return (sin_t(a) * divt(cos_t(a)));
}

/**
 * @brief Se obtiene la constante pi al aproximar utilizando
 * la suma parcial de la serie de Leibniz
 *
 * @return pi
 */
double pi()
{
    int i = 0;
    double pi = 0;
    double pi_next;
    double stopCriteria = 1;
    while ((stopCriteria > TOL) && (i < ITER_MAX))
    {
        if (isEven(i))
        {
            pi_next = pi + 1 * (4.0 / (2.0 * i + 1));
        }
        else
        {
            pi_next = pi + -1 * (4.0 / (2.0 * i + 1));
        }
        stopCriteria = abs(pi_next - pi);
        i++;
        pi = pi_next;
    }

    return pi;
}

/**
 * @brief Implementation for F(base) = base^(1/exponent)
 * 
 * @param base 
 * @param exponent 
 * @return double result
 */
double root_t(double base, double exponent)
{
    if (base <= 0)
    {
        cout << "Debe ingresar un numero mayor a 0" << endl;
        return 0;
    }
    double x_knext;
    double n = 0;
    double x_k = base * divt(2);
    double stopCriteria = 1;
    while ((stopCriteria > TOL) && (n < ITER_MAX))
    {
        x_knext = x_k - (power_t(x_k, exponent) - base) * divt(exponent * power_t(x_k, exponent - 1));
        stopCriteria = abs(x_knext - x_k) / x_knext;
        n++;
        x_k = x_knext;
    }
    return (base == 1) ? 1 : x_knext;
}

/**
 * @brief Implementation for F(base) = base^(1/2)
 * 
 * @param base 
 * @return double 
 */
double sqrt_t(double base)
{
    return root_t(base, 2);
}

/**
 * @brief Implementation of f(argument) = log_base(argument)
 * 
 * @param base 
 * @param argument 
 * @return double 
 */
double log_t(double base, double argument)
{
    return (argument >= 0 && base > 0) ? ln_t(argument) * divt(ln_t(base)) : NULL;
}

/**
 * @brief Implementation for f(a)=arcsin(a)
 * 
 * @param a 
 * @return double 
 */
double asin_t(double a)
{
    if (abs(a) == 1)
    {
        cout << "Debe ingresar un numero entre -1 y 1" << endl;
        return 0;
    }
    double x_knext;
    double n = 0;
    double x_k = abs(a);
    double stopCriteria = 1;
    while ((stopCriteria > TOL) && (n < ITER_MAX))
    {
        x_knext = x_k - (sin_t(x_k) - abs(a)) * divt(cos_t(x_k));
        stopCriteria = abs(x_knext - x_k) / x_knext;
        n++;
        x_k = x_knext;
    }
    return (a < 0) ? -1 * x_knext : x_knext;
}
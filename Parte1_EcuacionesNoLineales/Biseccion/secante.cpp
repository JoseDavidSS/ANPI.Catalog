#include <iostream>
#include <armadillo>
#include "matplotlibcpp.h"
#include <cmath>

using namespace std;
using namespace arma;
namespace plt = matplotlibcpp;

/**
 * @brief En esta funcion se define la f(x) que se desea analizar con el
 * metodo de la secante.
 * 
 * @param x  valor de x
 * @return double resultado de evaluar f(x)
 */
double myFunction(double x)
{
  return pow(exp(1), (-1 * pow(x, 2.0))) - x;
}

/**
 * @brief Funcion para aproximar el valor de f(x) por el metodo de la secante
 * 
 * @param x_k0 extremo menor del intervalo para evaluar
 * @param x_k1 extremos mayor del intervalor para evaluar
 * @param tol numero positivo que representa la tolerancia para |f(x)| < tol
 * @param iterMax numero maximo de iteraciones para cerrar
 * 
 * @return vector con el error y la aproximacion final
 */
std::vector<double>  secante(double x_k0, double x_k1, double tol, int iterMax)
{
  //Definimos las variables para el error y el x_k siguiente.
  double error_k = 1;
  double x_knext = 1;
  //Definimos los vectores para almacenar los datos.
  std::vector<double> results = {};
  std::vector<double> errors = {};
  std::vector<double> iteractions = {};

  int k = 0;
  //Iteramos hasta alcanzar las dos condiciones
  // 1. que el error_k sea menor a la tolerancia
  // 2. cumplir con las iteraciones maximas
  while(k < iterMax || error_k >= tol){

    //Definimos el x_k+1 como se define por el metodo de la secante.
    x_knext = x_k1 - ((x_k1 - x_k0) / (myFunction(x_k1) - myFunction(x_k0))) * myFunction(x_k1);

    //Definimos el error de x_k+1 como error_k a partir de la formula de error relativo.
    error_k = (abs(x_knext - x_k1)) / (abs(x_knext));

    //Insertamos los errores y los resultados en sus respectivos vectores.
    results.insert(results.begin() + k, x_knext);
    errors.insert(errors.begin() + k, error_k);
    iteractions.insert(iteractions.begin() + k, k + 1);

    //Redefinimos las varaibles para la siguiente iteracion
    x_k0 = x_k1;
    x_k1 = x_knext;

    k++;
  }

  //Tras completar el ciclo, contruimos el grafico
  plt::figure();
  plt::plot(iteractions, errors, "b");
  plt::title("Aproximacion por el metodo de la secante");
  plt::xlabel("Numero de iteracion");
  plt::ylabel("Aproximacion");
  plt::show();

  std::vector<double> finalResult = {x_knext, error_k};
  return finalResult;
}

int main()
{
  secante(0, 1, pow(10, -3), 7);
  return 0;
}

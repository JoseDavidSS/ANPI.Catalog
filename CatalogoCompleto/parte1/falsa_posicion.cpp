#include <iostream>
#include "matplotlibcpp.h"
#include <cmath>

using namespace std;
namespace plt = matplotlibcpp;

/**
 * @brief En esta funcion se define la f(x) que se desea analizar con el
 * metodo de la falsa posicion.
 * 
 * @param x  valor de x
 * @return double resultado de evaluar f(x)
 */
double myFunction(double x)
{
  return cos(x) - x;
}

/**
 * @brief Funcion para aproximar el valor de f(x) por el metodo de la falsa posicion
 * 
 * @param x0 extremo menor del intervalo para evaluar
 * @param x1 extremos mayor del intervalor para evaluar
 * @param TOL numero positivo que representa la TOLerancia para |f(x)| < TOL
 * @param MAXITER numero maximo de iteraciones para cerrar
 * 
 * @return vector con el error y la aproximacion final
 */
std::vector<double> falsa_posicion(double x0, double x1, double TOL, int MAXITER)
{
  //Definimos las variables para el error y el x_k siguiente.
  double error = 1;
  double x2 = 1;
  //Definimos los vectores para almacenar los datos.
  std::vector<double> results = {};
  std::vector<double> errors = {};
  std::vector<double> iterations = {};

  int k = 0;
  //Iteramos hasta alcanzar las dos condiciones
  // 1. que el error sea menor a la TOLerancia
  // 2. cumplir con las iteraciones maximas
  while(k < MAXITER || error < TOL){

    //Definimos el x_k+1 como se define por el metodo de la falsa posicion.
    x2 = x1 - ((x1 - x0) / (myFunction(x1) - myFunction(x0))) * myFunction(x1);

    //Definimos el error de x_k+1 como error a partir de la formula de error relativo.
    error = (abs(x2 - x1) / (x2));

    //Insertamos los errores y los resultados en sus respectivos vectores.
    results.insert(results.begin() + k, x2);
    errors.insert(errors.begin() + k, error);
    iterations.insert(iterations.begin() + k, k + 1);

    //Redefinimos las varaibles para la siguiente iteracion

    if(myFunction(x2) * myFunction(x1) < 0){
     x0 = x2;
      }

    if(myFunction(x0) * myFunction(x2) < 0){
      x1 = x2;
    }
    cout << x2 << endl;

    k++;
  }

  //Tras completar el ciclo, contruimos el grafico
  plt::figure();
  plt::plot(iterations, errors, "b");
  plt::title("Aproximacion por el metodo de la secante");
  plt::xlabel("Numero de iteracion");
  plt::ylabel("Aproximacion");
  plt::show();

  std::vector<double> finalResult = {x2, error};
  return finalResult;
}

int main()
{
  falsa_posicion(1/2, M_PI/4, pow(10, -3), 10);
  return 0;
}
#include <iostream>
#include <iomanip>
#include <armadillo>
#include "matplotlibcpp.h"

using namespace std;
using namespace arma;
namespace plt = matplotlibcpp;

/**
 * @brief Metodo de la pseudoinversa
 *
 * @param A: matriz de coeficientes
 * @param B: vector de terminos independientes
 * @param tol: tolerancia
 * @param iterMax: iteraciones maximas
 * @return error: error de la aproximacion
 *         xk: pseudoinversa aproximada
 */

void pseudoinversa(mat A, vec B, double tol, double iterMax){

    // Matrices
    mat x0 = (1 / (pow(norm(A,2),2))) * A.t();
    mat xk, xk1;

    // Matriz identidad
    int m = size(A)[0];
    mat I = eye(m,m);

    //Vector xk y xk1
    vec vecxk, vecxk1;

    //Error
    double error;
    vector <double> errors;

    vector <double>  iterations;

    for(int k = 1; k < iterMax; k++){

        // Pseudoinversa aproximada
        xk = x0 * (2 * I - A * x0);
        vecxk = xk * B;

        xk1 = xk * (2 * I - A * xk);
        vecxk1 = xk1 * B;

        // Formula para calcular el error
        error = (norm(vecxk1 - vecxk,2)) / (norm(vecxk1,2));

        // Condicion de parada
        if(abs(error) < tol){
            break;
        }
        x0 = xk;
        errors.push_back(error);
        iterations.push_back(k);
    }

    cout.precision(10);
    cout.setf(ios::fixed, ios::floatfield);
    cout << setw(15);
    xk.raw_print(cout, "Pseudoinversa aproximada: \n");
    cout << endl;
    vecxk1.raw_print(cout, "Vector aproximado: \n");
    cout << endl;
    cout << "Error: " << scientific << error << endl << endl;
    cout << endl;

    // Grafica de iteraciones vs error
    plt::plot(iteraciones,errores,"r-");
    plt::title("Iteraciones vs Error");
    plt::xlabel("Iteraciones");
    plt::ylabel("Error");
    plt::grid(true);
    plt::show();
}



int main(){
    mat A = {{1,2,-1}, {-3,1,5}};
    vec B = {1,4};

    pseudoinversa(A,B,1e-8,500);

    return 0;
}
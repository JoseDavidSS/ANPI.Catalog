#include <iostream>
#include <armadillo>
#include <vector>

using namespace std;
using namespace arma;

mat potencia_inversa(mat A, mat vector, int maxIter) {
    mat iterations;
    mat errors;
    double tol = 1e-5;
    mat yk1;
    float ck1;
    mat xk1;
    mat xk = vector;
    double error = 1.0 + tol;

    for (int k = 1; k < maxIter; k++){
        yk1 = solve(A, xk);
        ck1 = norm(yk1, "inf");
        xk1 = (1 / ck1) * yk1;
        error = norm(xk1 - xk);
        xk = xk1;

        if (error < tol) {
            cout << "Final error: "<< error << endl;
            cout << "Final k: "<< k << endl;
            cout << "Final ck: "<< ck1 << endl;
            cout << "Final xk: "<< xk << endl;
            break;
        }
        cout << "Error: "<< error << endl;
        cout << "k: "<< k << endl;
        cout << "ck: "<< ck1 << endl;
        cout << "xk: "<< xk << endl;
    }
    return A;
}

int main() {
    mat A = {{5, 4, -2},
           {4, -1, -7},
           {8, 2, 5}};

    mat b = {1, 1, 1};
    b = b.t();
    potencia_inversa(A, b, 15);

    return 0;
}
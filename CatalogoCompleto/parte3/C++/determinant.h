// C++ program to find Determinant of a matrix
#include <iostream>
#include <armadillo>

using namespace std;
using namespace arma;
 
 
/**
 * @brief Obtiene el  cofactor
 * 
 * @param A 
 * @param tmp 
 * @param p 
 * @param q 
 * @param n 
 * @return mat 
 */
mat getCofactor(mat A, mat tmp, int p,
                 int q, int n)
{
    int i = 0, j = 0;
     for (int row = 0; row < n; row++)
    {
        for (int col = 0; col < n; col++)
        {
            // Se copia en la matriz temporal solo aquellos 
            // elementos que no estan en cierta columna fila
            if (row != p && col != q)
            {
                tmp(i,j++) = A(row,col);
                if (j == n - 1)
                {
                    j = 0;
                    i++;
                }
            }
        }
    }
    return tmp;
}
 
/**
 * @brief Funcion general para obtener el determinante
 * de una matriz
 * 
 * @param A 
 * @param n 
 * @return int 
 */
int determinantOfMatrix(mat A, int n)
{
    int D = 0; // Resultado
 
    // Si la matriz solamente contiene un elemento
    if (n == 1)
        return A(0,0);
 
    // Matriz para guardar los cofactores
    mat tmp(A.n_cols, A.n_cols); 
    int sign = 1; 
 
    for (int f = 0; f < n; f++)
    {
        // Obtiene el cofactor de mat[0][f]
        tmp = getCofactor(A, tmp, 0, f, n);
        D += sign * A(0,f) * determinantOfMatrix(tmp, n - 1);
        // Se alterna el signo
        sign = -sign;
    }
 
    return D;
}
 
 

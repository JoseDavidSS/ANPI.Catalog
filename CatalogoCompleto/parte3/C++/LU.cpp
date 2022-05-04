#include "determinant.h"

/**
 * @brief Funcion auxiliar
 * de sustitucion hacia atras
 * 
 * @param A matrix
 * @param b vector
 * @return mat resultante
 */
mat sust_atras(mat A, mat b)
{
  int m = A.n_rows;
  mat x;
  x.zeros(m, 1);
  for (int i = m - 1; i >= 0; i--)
  {
    double aux = 0;
    for (int j = i + 1; j <= m - 1; j++)
    {
      aux += A(i, j) * x(j);
    }
    x(i) = (1 / A(i, i)) * (b(i) - aux);
  }
  return x;
}

/**
 * @brief Funcion auxiliar
 * para que implementa sustitucion hacia adelante
 * 
 * @param A matriz
 * @param b vector
 * @return mat resultante
 */
mat sust_adelante(mat A, mat b)
{
  int m = A.n_rows;
  mat y = zeros<mat>(m, 1);

  for (int i = 0; i < m; i++)
  {
    double val = 0;
    for (int j = 0; j < i; j++)
    {
      val = val + y(j) * A(i, j);
    }
    val = b(i) - val;
    y(i) = val / A(i, i);
  }
  return y;
}

/**
 * @brief Implementacion computacional
 * del metodo Factorizacion LU 
 * 
 * @param A matriz a analizar
 * @param vect vector de resultados
 */
void fact_lu(mat A, mat vect)
{
  // Verificamos que sea invertible
  if ((determinantOfMatrix(A, A.n_cols) != 0) && A.is_square())
  {
    int size = A.n_rows;
    // Creamos y populamos la diagonal con 1`s de la matriz L
    mat L;
    L.eye(A.n_rows, A.n_rows);
    // Creamos la matriz L
    mat U = A;

    // Eliminacion gaussiana
    for (int j = 0; j <= (size - 2); j++)
    {
      for (int i = j + 1; i <= (size - 1); i++)
      {
        // Operaciones entre filas
        L(i, j) = U(i, j) / U(j, j);
        U(i, span(j, size - 1)) -= L(i, j) * U(j, span(j, size - 1));
      }
    }
    mat y = zeros<mat>(size, 1);
    mat x = zeros<mat>(size, 1);
    y = sust_adelante(L, vect);
    x = sust_atras(U, y);
    cout << "L = \n"
         << L << "\nU = \n"
         << U << "\nVector y = \n"
         << y << "\nVector x = \n"
         << x << endl;
  }
  else
  {
    cout << "La matriz no es invertible o no es cuadrada." << endl;
  }
}


int main()
{
  mat A = {{1, 4, 0, 0},
           {3, 4, 1, 0},
           {0, 2, 3, 1},
           {0, 0, 1, 3}};
  mat vect = {1, 1, 1, 1};
  fact_lu(A, vect);
}
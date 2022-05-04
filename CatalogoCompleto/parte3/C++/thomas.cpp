#include <iostream>
#include <armadillo>
using namespace arma;
using namespace std;

/**
 * @brief Retorna el vector de la diagonal adyacente superior
 * 
 * @param A matriz
 * @return mat vector resultante
 */
mat sub_Diagonal(mat A)
{
    int size = A.n_rows;
    mat result;
    result.zeros(1, size - 1); // Define ceros la matriz de resultado
    int cont = 0;
    for (int i = 1; i < size; i++)
    { // Popula la matriz
        result(i - 1) = A(i, cont);
        cont++;
    }
    cout << "La diagonal inferior es: " << result << endl;
    return result;
}

/**
 * @brief Retorna la diagonal de la matriz
 * 
 * @param A matriz por analizar
 * @return mat vector resultante
 */
mat diagonal(mat A)
{
    int size = A.n_rows;
    mat result;
    result.zeros(1, size);
    for (int i = 0; i < size; i++)
    { // popula el vector resultante
        result(i) = A(i, i);
    }
    cout << "La diagonal es: " << result << endl;
    return result;
}

/**
 * @brief Retorna la diagonal superior
 * 
 * @param A matriz por analizar
 * @return mat vector resultante
 */
mat superior_Diagonal(const mat A)
{
    int size = A.n_rows;
    mat result;
    result.zeros(1, size); // Popula con ceros el vector resultantes
    int cont = 1;
    for (int i = 0; i < size - 1; i++)
    { //Popula el vector resultante
        result(i) = A(i, cont);
        cont++;
    }
    cout << "La diagonal superior es: " << result << endl;
    return result;
}

/**
 * @brief Determina si la matriz es tridiagonal
 * 
 * @param matrix matriz por analizar
 * @param vect vector de resultados
 * @return true si la matriz es tridiagonal
 * @return false si la matriz no es tridiagonal
 */
bool isTriDiagonal(mat matrix, mat vect)
{
    if (matrix.is_square()) 
    // Verifica que sea cuadrada
    {
        int size = matrix.n_rows;
        for (int x = 0; x < size; x++)
        {
            for (int y = 0; y < size; y++)
            {
                int cell = matrix(x, y);

                if ((x == y) || (x - 1 == y) || (x + 1 == y)) 
                // Verifica que las posiciones de las diagonales sean diferentes de cero
                {
                    if (cell == 0)
                    {
                        cout << "La matriz no es tridiagonal" << endl;
                        return false;
                    }
                }
                else
                {
                    if (cell != 0) 
                    // Verifica que las posiciones que no pertenecen a las diagonales sean cero
                    {
                        cout << "La matriz no es tridiagonal" << endl;
                        return false;
                    }
                }
            }
        }
        if (matrix.n_cols == vect.size())
        {
            cout << "La matriz es tridiagonal" << endl;
            return true;
        }
    }
}

/**
 * @brief Funcion auxiliar para la sustitucion hacia delante
 * 
 * @param vect 
 * @param A 
 * @param vect_len 
 * @return mat 
 */
mat sustitucion_adelante(mat vect, mat A, int vect_len)
{
    for (int i = 1; i < vect_len; i++)
    {
        vect(i) = vect(i) - A(i - 1) * vect(i - 1);
    }
    return vect;
}

/**
 * @brief Funcion auxiliar para la sustitucion hacia atras
 * 
 * @param vect 
 * @param X 
 * @param C 
 * @param B 
 * @param vect_len 
 * @return mat 
 */
mat sustitucion_atras(mat vect, mat X, mat C, mat B, int vect_len)
{
    X(vect_len - 1) = vect(vect_len - 1) / B(vect_len - 1);
    for (int i = vect_len - 2; i >= 0; --i)
    {
        X(i) = (vect(i) - C(i) * X(i + 1)) / B(i);
    }
    return X;
}

/**
 * @brief Implementacion computacional del metodo de 
 * Thomas para soluciones de sistemas de ecuaciones
 * 
 * @param matrix 
 * @param vect 
 */
void thomas(mat matrix, mat vect)
{
    // determinamos que sea tridiagonal
    isTriDiagonal(matrix, vect); 
    int vect_len = vect.size();

    // Determinamos las tres diagonales de la matriz
    mat A = sub_Diagonal(matrix);
    mat B = diagonal(matrix);
    mat C = superior_Diagonal(matrix);

    mat X; // creamos la matriz resultante
    X.zeros(1, vect_len); 

    // Realizamos la descomposicion de las matrices
    for (int i = 1; i < vect_len; i++)
    {
        A(i - 1) = A(i - 1) / B(i - 1);
        B(i) = B(i) - A(i - 1) * C(i - 1);
    }

    // Por ultimo resolvemos por sustitucion hacia delante y hacia atras
    vect = sustitucion_adelante(vect, A, vect_len);
    X = sustitucion_atras(vect, X, C, B, vect_len);

    cout << "El resultado por el metodo de Thomas es: " << X << endl;
}

int main()
{
  mat A = {{1, 4, 0, 0},
           {3, 4, 1, 0},
           {0, 2, 3, 1},
           {0, 0, 1, 3}};
  mat vect = {1, 1, 1, 1};
  thomas(A, vect);
}

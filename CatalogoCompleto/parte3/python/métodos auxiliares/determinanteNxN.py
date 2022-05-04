from copy import deepcopy
import numpy
    
def determinanteNxN(A):
    
    """
    Esta funcion calcula el determinante de una matriz dada por el usuario
    
    Sintaxis: determinanteNxN(A)
    
    Parametros Iniciales: 
                A = es una matriz de dimension nxn
                
    Parametros de Salida:                 
                determinanteMatriz = determinante de la matriz
    """    

    n = len(A)
    if n == 1:
        return A[0][0]
    
    elif n == 2:
        return (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])
    
    else:
        determinanteMatriz = 0
        
        for i in range(n):
            B = deepcopy(A)
            B = numpy.delete(B, 0, 0)
            B = numpy.delete(B, i, 1)
            
            if (i + 1) % 2 == 1:
                determinanteMatriz += A[0][i] * determinanteNxN(B)
                
            else:
                determinanteMatriz -= A[0][i] * determinanteNxN(B)
                
        #print (determinanteMatriz)
        return determinanteMatriz

help(determinanteNxN)

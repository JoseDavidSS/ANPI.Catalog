import numpy
import math
import matplotlib.pyplot as plt

def gauss_seidel(A, b, x, tol, iterMax):
    
    """
    Esta funcion determina las soluciones de un sistema de ecuaciones representado
    matricialmente por medio del metodo de Gauss-Seidel.
    
    Sintaxis: gauss_seidel(A, b, x, tol, iterMax)
    
    Parametros Iniciales: 
                A = es una matriz de dimension nxn
                b = es un vector con los valores de las igualdades de las ecuaciones.
                x = es un vector con los valores iniciales del sistema de ecuaciones.
                tol = tolerancia para el criterio ||A * x - b||<tol.
                iterMax = cantidad de iteraciones maximas.
                
    Parametros de Salida:                 
                x = es un vector con las soluciones del sistema de ecuaciones
                k = numero de iteraciones realizados
                error = ||A * x - b||
    """ 
    
    i = 0
    j = 0
    n = len(A)
    check = False
  
    while i < n:
        pivote = abs(A[i][i])
        temp_sum = 0
        
        while j < n:
            if i == j:
                j += 1
                
            else:
                temp_sum += abs(A[i][j])
                j += 1
                
        if temp_sum > pivote:
            check = True
            break
        
        i += 1
        j = 0
    
    if check:
        print("La matriz no es diagonalmente dominante.")
    else:
        
        i = 0
        j = 0
        
        k = 0
        error = tol + 1
        e = []
        it = []
        
        while error > tol and k < iterMax:
            
            while i < n:
                temp_sum = 0
                
                while j < n:
                    if i == j:
                        j += 1
                        
                    else:
                        temp_sum += A[i][j] * x[j]
                        j += 1
                        
                x[i] = (1 / A[i][i]) * (b[i] - temp_sum)
                i += 1
                j = 0
                
            errMat = numpy.dot(A, x) - b;
            errAdd = 0
            
            for i in errMat:
                errAdd += math.pow(i, 2)
        
            error = math.sqrt(errAdd)
            e.append(error)
            k = k + 1
            it.append(k)
            i = 0
            j = 0
        
        plt.plot(it, e)
        print ([x, k, error])
        plt.show()
        return [x, k, error] 
    
help(gauss_seidel)

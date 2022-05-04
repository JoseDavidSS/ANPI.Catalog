import matplotlib.pyplot as plt
import numpy
import math

def jacobi(A, b, xk, tol, iterMax):
    
    """
    Esta funcion determina las soluciones de un sistema de ecuaciones representado
    matricialmente por medio del metodo de Jacobi.
    
    Sintaxis: jacobi(A, b, xk, tol, iterMax)
    
    Parametros Iniciales: 
                A = es una matriz de dimension nxn.
                b = es un vector con los valores de las igualdades de las ecuaciones.
                xk = es un vector con los valores iniciales del sistema de ecuaciones.
                tol = tolerancia  para el  criterio  ||A * x - b||<tol.
                iterMax = cantidad de iteraciones maximas.
                
    Parametros de Salida:                 
                xk = es un vector con las soluciones del sistema de ecuaciones.
                k = numero de iteraciones realizados.
                error = ||A * xk - b||.
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
        xk1 = []
        
        for i in xk:
            xk1.append(0)
        
        while error > tol and k < iterMax:
            
            while i < n:
                temp_sum = 0
                
                while j < n:
                    if i == j:
                        j += 1
                        
                    else:
                        temp_sum += A[i][j] * xk[j]
                        j += 1
                        
                xk1[i] = (1 / A[i][i]) * (b[i] - temp_sum)
                i += 1
                j = 0
            
            for i in range(len(xk1)):
                xk[i] = xk1[i]
                
            errMat = numpy.dot(A, xk) - b;
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
        print ([xk, k, error])
        plt.show()
        return [xk, k, error] 

help(jacobi)

from sust_atras import *
from sympy import Symbol
from sympy.solvers import solve

def gaussiana(A, b):
    
    """
    Esta funcion determina las soluciones de un sistema de ecuaciones representado
    matricialmente por medio de eliminacion gaussiana.
    
    Sintaxis: gaussiana(A, b)
    
    Parametros Iniciales: 
                A = es una matriz de dimension nxn.
                b = es un vector con los valores de las igualdades de las ecuaciones.
                
    Parametros de Salida:                 
                x = es un vector con las soluciones del sistema de ecuaciones.
    """ 
    
    X = Symbol('X')
    
    l = len(b)
    i = 0
    j = 0
    n = 0
    
    while i < l:
        
        if i == 0:
            div = A[0][0]
            
            while j < l:
                A[i][j] = A[i][j] / div
                j += 1
                
            b[i] = b[i] / div
            i += 1
            j = 0
            
        else:
            
            if j == i:
                div = A[i][j]
                
                while j < l:
                    A[i][j] = A[i][j] / div
                    j += 1
                    
                b[i] = b[i] / div
                i += 1
                j = 0
                
            elif A[i][j] != 0:
                factor = solve(A[i][j] + A[j][j] * X, X)
                factor = factor[0]
                n = j
                
                while n < l:
                    A[i][n] = A[i][n] + A[j][n] * factor
                    n += 1
                    
                b[i] = b[i] + b[j] * factor
                j += 1
                
            else:
                j += 1
                
    print (sust_atras(A, b))
    return sust_atras(A, b)

help(gaussiana)

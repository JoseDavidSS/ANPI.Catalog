from sympy import Symbol
from sympy import expand
from sympy.plotting import plot

def lagrange(xk, yk):
    
    """
    Esta función encuentra el polinomio de interpolación de Lagrange
    
    Sintaxis: lagrange(xk, yk)
    
    Parámetros Iniciales: 
                xk = es una lista con pares x de las coordenadas
                yk = es una lista con pares y de las coordenadas
                
    Parámetros de Salida:                 
                px = polinomio de interpolación
    """
    
    X = Symbol('X')
    
    n = len(xk)
    L = []
    Ltemp = 1
  
    j = 0
    k = 0
  
    while k < n:
        while j < n:
            if j == k:
                j += 1
            else:
                Ltemp *= (X - xk[j]) / (xk[k] - xk[j])
                j += 1
        
        L.append(expand(Ltemp))
        Ltemp = 1
        k += 1
        j = 0
        
    px = 0
    
    for i in range(n):
        px += yk[i] * L[i]
    
    plot(px)

    print (px)
    return px

help(lagrange)

xk = [-2, 0, 1]
yk = [0, 1, -1]
lagrange(xk, yk)

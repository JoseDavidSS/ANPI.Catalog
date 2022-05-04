from sust_adelante import *
from sust_atras import *
from determinanteNxN import *

from copy import deepcopy
import numpy
import math

def fact_cholesky(A, b):
    
    """
    Esta funcion determina las soluciones de un sistema de ecuaciones representado
    matricialmente por medio de factorizacion de Cholesky.
    
    Sintaxis: fact_cholesky(A, b)
    
    Parametros Iniciales: 
                A = es una matriz de dimension nxn.
                b = es un vector con los valores de las igualdades de las ecuaciones.
                
    Parametros de Salida:                 
                x = es un vector con las soluciones del sistema de ecuaciones.
    """ 
    
    A = numpy.array(A)
    AResp = deepcopy(A)
    AT = numpy.transpose(A)
    check = False
    n = len(A)
    i = 0
    j = 0
    k = 0
    
    while i < n:
        while j < n:
            
            if A[i][j] != AT[i][j]:
                check = True
            else:
                j += 1
        i += 1
        j = 0
        
    i = 0
    j = 0
        
    while i < n - 1:
        while j < n - 1:
            A = numpy.delete(A, i + 1, 0)
            A = numpy.delete(A, i + 1, 1)
            j += 1
            
        mdet = determinanteNxN(A)
        
        if mdet <= 0:
            check = True
            
        else:
            i += 1
            A = deepcopy(AResp)
            k += 1
            j = k
            
    mdet = determinanteNxN(A)
    
    if mdet <= 0:
        check = True
        
    if check:
        print('La Matriz no es simétrica definida positiva')
        
    else:
        i = 0
        j = 0
        k = 0
        l = len(b)
        L = numpy.eye(l, l)
    
        while j < l:
            i = j
            k = j
            tempAdd = A[i][j]
            k -= 1
            
            while k > -1:
                tempAdd -= math.pow(L[i][k], 2)
                k -= 1
                
            L[i][j] = math.sqrt(tempAdd)
            i += 1
            k = j - 1
            
            while i < l:
                tempAdd = A[i][j]
                while k > -1:
                    tempAdd -= (L[i][k] * L[j][k])
                    k -= 1
                    
                L[i][j] = tempAdd / L[j][j]
                i += 1
                k = j - 1
                
            j += 1
    
        y = sust_adelante(L, b)
        print (sust_atras(numpy.transpose(L), y))
        return sust_atras(numpy.transpose(L), y)
    
help(fact_cholesky)

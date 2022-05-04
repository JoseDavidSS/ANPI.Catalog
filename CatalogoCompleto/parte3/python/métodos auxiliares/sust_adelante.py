from copy import deepcopy

def sust_adelante(A, b):
    
    """
    Esta funcion determina las soluciones de un sistema de ecuaciones representado
    matricialmente por medio de susticion hacia adelante.
    
    Sintaxis: sust_adelante(A, b)
    
    Parametros Iniciales: 
                A = es una matriz de dimension nxn triangular superior.
                b = es un vector con los valores de las igualdades de las ecuaciones.
                
    Parametros de Salida:                 
                x = es un vector con las soluciones del sistema de ecuaciones.
    """ 

    n = len(b)
    i = 0
    j = 0
    
    y = deepcopy(b)
    
    y[i] = b[i] / A[i][j]
    
    while i < n:
        tempAdd = 0
        
        while j < i:
            tempAdd += A[i][j] * y[j]
            j += 1
            
        if b[i] - tempAdd > 10**-3 or b[i] - tempAdd < -10**-3:
            y[i] = (b[i] - tempAdd) / A[i][j]
            j = 0
            i += 1
            
        else:
            y[i] = 0
            j = 0
            i += 1

    #print (y)  
    return y

help(sust_adelante)

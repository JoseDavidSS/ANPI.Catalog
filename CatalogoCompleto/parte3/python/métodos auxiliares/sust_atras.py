from copy import deepcopy

def sust_atras(A, b):
    
    """
    Esta funcion determina las soluciones de un sistema de ecuaciones representado
    matricialmente por medio de susticion hacia atras.
    
    Sintaxis: sust_atras(A, b)
    
    Parametros Iniciales: 
                A = es una matriz de dimension nxn triangular inferior.
                b = es un vector con los valores de las igualdades de las ecuaciones.
                
    Parametros de Salida:                 
                x = es un vector con las soluciones del sistema de ecuaciones.
    """ 
    
    n = len(b)
    i = n - 1
    j = n - 1
    
    x = deepcopy(b)
    
    x[i] = b[i] / A[i][j]
    
    while i > -1:
        tempAdd = 0
        
        while j > i:
            tempAdd += A[i][j] * x[j]
            j -= 1
            
        if b[i] - tempAdd > 10**-3 or b[i] - tempAdd < -10**-3:
            x[i] = (b[i] - tempAdd) / A[i][j]
            j = n - 1
            i -= 1
            
        else:
            x[i] = 0
            j = n - 1
            i -= 1
            
    #print (x)
    return x

help(sust_atras)

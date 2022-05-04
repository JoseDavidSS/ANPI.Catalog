import numpy as np
import  sympy as sp

'''
Esta funcion permite estimar el error del trazador cubico.

Sintaxis : cota_traz_cubico(funcion, x_k)

Parametros Iniciales :
    funcion: funcion de la cual se obtienen los trazadores
    x_k: vector de soporte definido en un intervalo [a,b]
Parametros de Salida :
    cota: error estimado
'''
def cota_traz_cubico(funcion, x_k):
    n = len(x_k)
    x = sp.symbols('x')
    fun = sp.simplify(funcion)
    
    #Calculamos la cuarta derivada
    derivada = cuartaDerivada(fun, x)
    
    #Obtenemos las imagenes
    imagenes = vectorImagenes(n, x_k, derivada, x)
    
    #Calculamos el vector h_k
    h_k = vectorH_k(x_k)
    
    #Calculamos el error
    h = max(h_k)
    tmp = max(imagenes)
    cota = tmp*(5*h**4)/384
    return cota

def cuartaDerivada(funcion, x):
    derivada = funcion.diff(x)
    derivada2 = derivada.diff(x)
    derivada3 = derivada2.diff(x)
    derivada4 = derivada3.diff(x)
    return derivada4


def vectorImagenes(n, x_k, derivada, x):
    imagenes = []
    for i in range(n):
        x_i = x_k[i]
        y_i = float(derivada.subs(x,x_i))
        imagenes.append(abs(y_i))
    return imagenes
        
def vectorH_k(x_k):
    h_k = []
    n = len(x_k)
    for i in range(n-1):
        h_i = x_k[i+1] - x_k[i]
        h_k.append(h_i)
    return h_k

x_k = [1, 1.05, 1.07, 1.1]
cota = cota_traz_cubico('3*x*exp(x) - 2*exp(x)', x_k)
print(cota)
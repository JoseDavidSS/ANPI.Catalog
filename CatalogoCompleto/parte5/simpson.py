from sympy import sympify
from sympy import diff

def simpson(f, a, b):
    
    """
    Esta función encuentra una aproximación de la integral de una función
    en un intervalo dado con la regla de simpson.
    
    Sintaxis: simpson(f, a, b)
    
    Parámetros Iniciales: 
                f = función a integrar.
                a = extremo izquierdo del intervalo de integración.
                b = extremo derecho del intervalo de integración.
                
    Parámetros de Salida:                 
                aprox = valor aproximado de la integral en el intervalo específicado.
                error = h^5/90 * |f^4(eps)|.
    """
    func = sympify(f)
    primeraDerivada = diff(func)
    segundaDerivada = diff(primeraDerivada)
    terceraDerivada = diff(segundaDerivada)
    cuartaDerivada = diff(terceraDerivada)
    
    h = (b - a) / 2
    x1 = (a + b) / 2
  
    aprox = ((h / 3) * (func.subs({'x': a}) + 4 * func.subs({'x': x1}) + func.subs({'x': b}))).evalf()

    epsilon = a
  
    for i in range(a, b):
        if abs(cuartaDerivada.subs({'x': i})) > abs(cuartaDerivada.subs({'x': epsilon})):
            epsilon = i
            
    error = (((h**5) / 90) * abs(cuartaDerivada.subs({'x': epsilon}))).evalf()
    print ([aprox, error])
    return [aprox, error]

help(simpson)

simpson('ln(x)', 2, 5)

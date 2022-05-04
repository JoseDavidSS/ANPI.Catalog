from sympy import sympify
from sympy import diff

def simpson_compuesto(f, a, b, m):
    
    """
    Esta función encuentra una aproximación de la integral de una función en un intervalo dado con la regla de simpson compuesto
    
    Sintaxis: simpson_compuesto(f, a, b, m)
    
    Parámetros Iniciales: 
                f = función a integrar
                a = inicio del intervalo de integración
                b = final del intervalo de integración
                m = cantidad de subintervalos a realizar
                
    Parámetros de Salida:                 
                aprox = valor aproximado de la integral en el intervalo específicado
                error = ((b - a) * h^4)/180 * |f^4(eps)|
    """
    
    func = sympify(f)
    primeraDerivada = diff(func)
    segundaDerivada = diff(primeraDerivada)
    terceraDerivada = diff(segundaDerivada)
    cuartaDerivada = diff(terceraDerivada)
    
    h = (b - a) / (m - 1)
    
    i = 1
    x = [];
    x.append(a)
    while i < m:
        x.append(a + (i * h));
        i += 1;
  
    i = 1
    sumaPar = 0
    sumaImpar = 0
    cantVars = len(x) - 1
  
    while i < cantVars:
        if i % 2 == 0:
            sumaPar += (func.subs({'x': x[i]})).evalf()
            i += 1
        else:
            sumaImpar += (func.subs({'x': x[i]})).evalf()
            i += 1
  
    aprox = ((h / 3) * (func.subs({'x': a}) + 2 * sumaPar + 4 * sumaImpar + func.subs({'x': b}))).evalf()
  
    epsilon = a;
  
    for i in range(a, b):
        if abs(cuartaDerivada.subs({'x': i})) > abs(cuartaDerivada.subs({'x': epsilon})):
            epsilon = i
            
    error = ((((b - a) * (h**4)) / 180) * abs(cuartaDerivada.subs({'x': epsilon}))).evalf()
    print ([aprox, error])
    return [aprox, error]

help(simpson_compuesto)

simpson_compuesto('ln(x)', 2, 5, 7)

def biseccion(f, a, b, tol, iterMax):

    """
    Esta función aproxima la solución de la ecuación f(x) = 0, utilizando el método de la bisección
    
    Sintaxis:  biseccion(f, a, b, tol, iterMax)
    
    Parámetros Iniciales: 
                f = es un string que representa a la función f
                a, b = son los extremos del intervalo [a, b]
                tol = un número positivo que representa a la tolerancia para el criterio |f(x)| < tol
                iterMax = cantidad de iteraciones máximas
                
    Parámetros de Salida: 
                [x, k, error], donde                
                x = aproximación del cero de la función f
                k = número de iteraciones realizados
                error = |f(x)|
    """    
    
    from sympy import sympify
    import matplotlib.pyplot as plt

    func = sympify(f)
    fa = func.subs({'x': a})
    fb = func.subs({'x': b})
    
    if fa * fb > 0:
        x = []
        k = []
        error = []
        display('El teorema de Bolzano no se cumple, es decir, f(a) * f(b) > 0')
    else:
        error = tol + 1
        k = 0
        it = []
        er = []
        while error > tol and k < iterMax:
            k = k + 1
            x = (a + b) / 2
            fa = func.subs({'x': a})
            fx = func.subs({'x': x})
            error = abs(fx)
            it.append(k)
            er.append(error)
            if fa * fx < 0:
                b = x                
            else:
                a = x   
    plt.plot(it, er)
    plt.show()
    return [x, k, error]

help(biseccion)

biseccion('exp(x)-x-2', 0, 2, 10**-8, 50)

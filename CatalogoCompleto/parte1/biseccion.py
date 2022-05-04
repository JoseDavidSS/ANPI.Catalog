def biseccion(f, a, b, tol, iterMax):

    """
    Esta funcion aproxima la solucion de la ecuacion f(x)=0,
    utilizando el motodo de la biseccion.
    
    Sintaxis:  biseccion(f, a, b, tol, iterMax)
    
    Parametros Iniciales: 
                f = es una cadena de caracteres (string) que representa a la funcion f
                a, b = son los extremos del intervalo [a, b]
                tol = un numero positivo que representa a la tolerancia para el criterio |f(x)| < tol
                iterMax = cantidad de iteraciones maximas
                
    Parametros de Salida: 
                [x, k, error], donde                
                x = aproximacion del cero de la funcion f
                k = numero de iteraciones realizados
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
            if fa * fx < 0: # Se cumple la condicion en el intervalo 1. 
                b = x               
            else: # Se cumple la condicion en el intervalo 2.
                a = x   
    plt.plot(it, er)
    plt.show()
    return [x, k, error]

help(biseccion)

biseccion('exp(x)-2*x-10', 2, 4, 10**-5, 1000)

def muller(f, xk0, xk1, xk2, tol, iterMax):
    
    """
    Esta funcion aproxima la solucion de la ecuacion f(x) = 0, utilizando el metodo de muller, pero este hace uso de una ecuacion de segundo grado
    
    Sintaxis:  muller(f, xk0, xk1, xk2, tol, iterMax)
    
    Parametros Iniciales: 
                f = es un string que representa a la funcion f
                xk0, xk1, xk2 = son los valores iniciales de la iteracion, estos seran los primeros valores evaluados en la funcion
                tol = un numero positivo que representa a la tolerancia para el criterio |f(x_k)| < tol
                iterMax = cantidad de iteraciones maximas
                
    Parametros de Salida: 
                [x_k, k, error], donde                
                x_k = aproximacion del cero de la funcion f
                k = numero de iteraciones realizados
                error = |f(x)|
    """
    
    from sympy import sympify
    import matplotlib.pyplot as plt
    import numpy
    import math
    
    func = sympify(f)
    
    k = 0
    error = tol + 1
    er = []
    it = []
    while error > tol and k < iterMax:
        k = k + 1
        fxk0 = func.subs({'x': xk0}).evalf()
        fxk1 = func.subs({'x': xk1}).evalf()
        fxk2 = func.subs({'x': xk2}).evalf()
        a=(((xk1-xk2)*(fxk0-fxk2))-((xk0-xk2)*(fxk1-fxk2)))/((xk0-xk1)*(xk0-xk2)*(xk1-xk2))
        b=((((xk0-xk2)**2)*(fxk1-fxk2))-(((xk1-xk2)**2)*(fxk0-fxk2)))/((xk0-xk1)*(xk0-xk2)*(xk1-xk2))
        c = fxk2
        xk = xk2 - ((2 * c) / (b + (numpy.sign(b) * math.sqrt((b ** 2) - (4 * a * c)))));
        fxk = func.subs({'x' : xk}).evalf()
        error = abs(fxk)
        er.append(error)
        it.append(k)
        
        if abs(xk - xk0) < abs(xk - xk1):
            if abs(xk - xk1) < abs(xk - xk2):
                xk2 = xk
            else:
                xk1 = xk2
                xk2 = xk
        else:
            if abs(xk - xk1) < abs(xk - xk2):
                if abs(xk - xk0) < abs(xk - xk2):
                    xk2 = xk
                else:
                    xk0 = xk2
                    xk2 = xk
            else:
                xk0 = xk2
                xk2 = xk
        
    plt.plot(it, er)
    plt.show()
    return [xk, k, error]
    
help(muller)

muller('sin(x) - cos(x)', 1, 2, 3, 10**-8, 50)

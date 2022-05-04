from sympy import *
import  matplotlib.pyplot  as plt



def runge_kutta_4(y0, a, b, n, funcion):
    
    """
    Esta funcion aproxima la solucion de la ecuacion diferencial dx/dy,
    utilizando el metodo de Runge-Kutta de Orden 4.

    Sintaxis:
        runge_kutta_4(y0, a, b, n, funcion)

    Parametros Iniciales:
        y0 = va a ser el valor inicial
        a, b = son los extremos del intervalo [a, b]
        n = va a ser un número que representa la cantidad de puntos
        funcion = es una cadena de caracteres (string) que representa a la ecuacion diferencial

    Parametros  de  Salida:
        [x, y], vectores conteniendo los pares ordenados de la solucion
    """
    
    variableX = Symbol('x')
    variableY = Symbol('y')
    func = sympify(funcion)
    f = lambdify([variableX, variableY], func, "numpy")

    h = (b - a) / (n - 1)

    x = [a]
    y = [y0]
    
    k_4 = []
    k_3 = []
    k_2 = []
    k_1 = []

    i = 0

    while i < n-1:
        
        k_1.append(f(x[i], y[i]))
        k_2.append(f(x[i] + h / 2, y[i] + h * k_1[i] / 2))
        k_3.append(f(x[i] + h / 2, y[i] + h * k_2[i] / 2))
        k_4.append(f(x[i] + h, y[i] + h * k_3[i]))
        
        x.append(x[i] + h)
        y.append(y[i] + h / 6 * (k_1[i] + 2 * k_2[i] + 2 * k_3[i] + k_4[i]))

        i += 1

    plt.plot(x, y)
    plt.show()

    return [x, y]

help (runge_kutta_4)

print(runge_kutta_4(1, 0, 1, 11, '-x*y + 4*x/y'))

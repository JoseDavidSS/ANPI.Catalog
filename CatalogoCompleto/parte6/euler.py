from sympy import sympify
from sympy import Symbol
from sympy import expand
import matplotlib.pyplot as plt

def euler(funcion, intervalo, pasoh, y_0):
    """
    Esta funcion permite resolver el problema de Cauchy
    
    Sintaxis: euler(funcion, intervalo, pasoh, y_0)
    
    Parametros Iniciales: 
                funcion: string de la funcion a evaluar
                intervalo: de la forma [a,b] en la cual se evalua la funcion
                pasoh: numero de puntos dentro del intervalo
                y_0: valor inicial de los pares y_k
                
    Parametros de Salida:  
                Una lista con los siguientes valores               
                x_k: lista de los pares x_k
                y_k: lista de los pares y_k
                px: polinomios de interpolacion
    """
    
    # Se preparan los valores iniciales
    func = sympify(funcion)
    a = intervalo[0]
    b = intervalo[1]
    N = pasoh
    h = (b-a)/(N-1)
    
    #Arrays para almacenar resultados
    valores_xk = []
    valores_yk = []
    
    #Se ejecuta el metodo
    n = 0
    while (n < N):
        x_k = a + n*h      
        valores_xk.append(x_k)
        valores_yk.append(y_0)
        
        f_x_y = func.subs({'x':x_k, 'y':y_0})
        y_n = y_0 + h*f_x_y
        y_0 = y_n
        n+=1
    
    #Se obtiene el polinomio de interpolacion
    pol = lagrange(valores_xk, valores_yk)
    
    #Se construye la grafica
    plt.scatter(valores_xk, valores_yk) 
    plt.plot(valores_xk, valores_yk)

    plt.title("Polinomio de interpolación")
    plt.xlabel("xk")
    plt.ylabel("p(x)")

    plt.show()
    return [valores_xk, valores_yk, pol]


def lagrange(xk, yk):
    #Funcion para obtener polinomio de interpolacion
    k = 0
    polinomio = 0
    while k<len(xk):
        polinomio +=  yk[k]*L_k(k, xk) 
        k+=1
    polinomio = expand(polinomio)

    return polinomio

def L_k(k, xk):
    #Funcion auxiliar para lagrange
    j = 0
    x = Symbol('x')
    Lk = 1
    while j < len(xk):
        if j != k:
            Lk = Lk*(x - xk[j])/(xk[k] - xk[j])
        
        j+=1
    Lk = expand(Lk)
    return Lk

result = euler('1+y-x**2', [0,2],11,0.5)
help(euler)
print("Los parametros de salida son:\n \nValores x_k de los pares ordenados:\n \n", result[0],
      "\n\nValores y_k de los pares ordenados:\n \n", result[1],
      "\n\nPolinomios de interpolacion:\n \n", result[2])


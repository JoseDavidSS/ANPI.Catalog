from sympy import Symbol, expand

def dd_newton(xk, yk):

    """
    Esta función encuentra el px de interpolación de Diferencias Divididas de Newton
    
    Sintaxis: dd_newton(xk, yk)
    
    Parámetros Iniciales: 
                xk = es una lista con pares x de las coordenadas
                yk = es una lista con pares y de las coordenadas
                
    Parámetros de Salida:                 
                px = polinomio de interpolación
    """
    
    par = []
    lista_puntos = []
    largo_lista = len(xk)
    z = 0

    while z < largo_lista:
        par.append(xk[z])
        par.append(yk[z])
        lista_puntos.append(par)
        par = []
        z += 1
    print (lista_puntos)
    
    n = len(lista_puntos)  # Cantidad de puntos
    px = lista_puntos[0][1]  # Polinomio de interpolacion
    resul_previos = []     # Lista para los resultados previos
    x = Symbol('x')        # Variable simbolica
    m = n - 1
    multi = 1  # Variable que almacena la multiplicacion (x-x0) * ... * (x-xn)

    for i in range(0, n): # Se agregan los "y" en la lista de resultados previos
        resul_previos += [lista_puntos[i][1]]

    for i in range(1, n):
        multi *= x - lista_puntos[i - 1][0]  # Se multiplica por (x - xi)
        resul_nuevos = []  # Lista para los resultados nuevos
        
        for j in range(0, m): # Se realiza el calculo de cada elemento del polinomio
            numerador = resul_previos[j] - resul_previos[j + 1]
            denominador = lista_puntos[j][0] - lista_puntos[j + i][0]
            resul_nuevos += [numerador / denominador]
        m -= 1
        
        # Se actualiza el polinomio
        px += resul_nuevos[0] * multi
        
        # Se actualiza la lista de resultados previos
        resul_previos = resul_nuevos.copy()

    return expand(px)

help(dd_newton)

xk = [-2, 0, 1]
yk = [0, 1, -1]
print(dd_newton(xk, yk))


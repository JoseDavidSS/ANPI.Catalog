def coordinado(f, xk, vars, tol, iterMax):

    """
    Esta funcion aproxima la solucion de la funcion f(x), donde
    x = [x1, x2, x3, ..., xn], utilizando el metodo del descenso coordinado.
    
    Sintaxis: coordinado(f, xk, vars, tol, iterMax)
    
    Parametros Iniciales: 
                f = es un string que representa a la funcion f de varias variables.
                xk = es una lista con los valores iniciales de la funcion.
                vars = es una lista con strings de todas las variables que se
                encuentran en la funcion.
                tol = un numero positivo que representa a la tolerancia para el
                criterio ||f(xk)|| < tol.
                iterMax = cantidad de iteraciones maximas.
                
    Parametros de Salida: 
                xk = aproximacion de la convergencia de la funcion f.
                k = numero de iteraciones realizados.
                error = ||f(xk)||
    """    
    
    from sympy import sympify
    from sympy import Symbol
    from sympy import diff
    from sympy import solve
    import math
    import matplotlib.pyplot as plt

    func = sympify(f)    
    symVars = []
    g = []

    for i in vars:
        symVars.append(str(Symbol(i)))
    
    for i in symVars:
        g.append(func.diff(Symbol(i)))
    
    k = 0
    error = tol + 1
    e = []
    it = []
    
    while error > tol and k < iterMax:
        for i in range(len(symVars)):
            tempxk = {}
            for j in range(len(symVars)):
                if j == i:
                    tempxk.update({vars[j]: symVars[j]})
                else:
                    tempxk.update({vars[j]: xk[j]})
            tempFunc = func.subs(tempxk)
            dFunc = diff(tempFunc)
            sol = solve(dFunc, symVars[i])
            if len(sol) > 1:
                mini = 0
                for j in range(len(sol)):
                    currentSol = sol[j].evalf()
                    if currentSol > 0 and mini == 0:
                        mini = currentSol
                    elif currentSol < mini and mini != 0:
                        mini = currentSol
                    else:
                        continue
                xk[i] = mini
            else:
                xk[i] = sol[0].evalf()
    
        evas = {}
        for i in range(len(vars)):
            evas.update({vars[i]: xk[i]})
        
        gk = []
        for i in g:
            gk.append(i.subs(evas))
            
        add = 0
        for i in gk:
            add += math.pow(i, 2)
            
        error = math.sqrt(add)
 
        e.append(error)
        k = k + 1
        it.append(k)
    
    plt.plot(it, e)
    plt.show()
    return [xk, k, error] 

help(coordinado)

coordinado('x**3+y**3+z**3-2*x*y-2*x*z-2*y*z',[1,1,1],['x','y','z'],10**-8,10)

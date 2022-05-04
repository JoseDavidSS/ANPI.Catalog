pkg load symbolic

function [xk, k, error] = newton_raphson(f, xk0, tol, iterMax)

    %Esta funcion aproxima la solucion de la ecuacion f(x) = 0, utilizando el metodo de Newton-Raphson
    %
    %Sintaxis: newton_raphson(f, xk0, tol, iterMax)
    %
    %Parametros Iniciales: 
    %            f = es un string que representa a la funcion f
    %            xk0 = es el valor inicial de la iteracion, este sera el primer valor evaluado en la funcion
    %            tol = un numero positivo que representa a la tolerancia para el criterio |f(x_k)| < tol
    %            iterMax = cantidad de iteraciones maximas
    %   
    %Parametros de Salida:                           
    %            x_k = aproximacion del cero de la funcion f
    %            k = numero de iteraciones realizados
    %            error = |f(x)|
    
    func = matlabFunction(sym(f));
    dfunc = matlabFunction(diff(sym(func)));
    
    k = 0;
    error = tol + 1;
    e = [];
    
    if dfunc(xk0) < tol
        xk = []
        k = []
        error = []
        display('La derivada se indefine.')
    else
        while and(error > tol, k < iterMax)
            k = k + 1;
            if dfunc(xk0) < tol
                break;
            else
                xk = xk0 - (func(xk0) / dfunc(xk0));
                error = abs(func(xk));
                e = [e error];
                xk0 = xk;
            end
        end
        plot(1 : k, e)
    end
end

help newton_raphson
% Comando que corre la funcion Newton Raphson, editar al gusto.
[xk, k, error] = newton_raphson('-cos(x) + x**2', 5, 10**-8, 50)
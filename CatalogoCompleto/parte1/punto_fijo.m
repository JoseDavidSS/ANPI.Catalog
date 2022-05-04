pkg load symbolic

function [xk, k, error] = punto_fijo(phi, xk0, a, b, tol, iterMax)

    %Esta funcion aproxima la solucion de la ecuacion f(x) = 0, utilizando el metodo del punto fijo, pero es necesario indicar el phi(x) de la funcion, f(x) = phi(x) - x
    %
    %Sintaxis: punto_fijo(phi, xk0, a, b, tol, iterMax)
    %
    %Parametros Iniciales: 
    %            f = es un string que representa a la funcion f
    %            xk0 = es el valor inicial de la iteracion, estos seran los primeros valores evaluados en la funcion
    %            tol = un numero positivo que representa a la tolerancia para el criterio |f(x_k) - x_k| < tol
    %            iterMax = cantidad de iteraciones maximas
    %   
    %Parametros de Salida:                           
    %            x_k = aproximacion del cero de la funcion f
    %            k = numero de iteraciones realizados
    %            error = |f(x) - x_k|

    func = matlabFunction(sym(phi));
    dfunc = matlabFunction(diff(sym(func)));
    
    syms x
    sol = solve(dfunc, x);
    pcm = func(sol);
    
    if and(a > func(a), func(a) > b)
        xk = []; 
        k = []; 
        error = [];
        display("El valor a, se sale del intervalo dado")
    elseif and(a > func(b), func(b) > b)
        xk = []; 
        k = []; 
        error = [];
        display("El valor b, se sale del intervalo dado")
    elseif and(-1 >= dfunc(a), dfunc(a) >= 1)
        xk = []; 
        k = []; 
        error = [];
        display("El valor a, se sale del intervalo ]-1, 1[")
    elseif and(-1 >= dfunc(b), dfunc(b) >= 1)
        xk = []; 
        k = []; 
        error = [];
        display("El valor b, se sale del intervalo ]-1, 1[")
    else
        ultpc = pcm(end, end);
        i = 1;
        validar = 1;
        while pcm(i, end) != ultpc
            cpc = pcm(i, end);
            if and(a > cpc, cpc > b)
                display("Hay un punto critico que se sale del intervalo dado")
                validar = 0;
                break;
            else
                i += 1;
            end
        end
        
        if and(a > ultpc, ultpc > b)
            display("Hay un punto critico que se sale del intervalo dado")
            validar = 0;
        else
            if validar == 1
                d2func = matlabFunction(diff(sym(dfunc)));
                sol2 = solve(d2func, x);
                pcm2 = dfunc(sol2);
                
                ultpc2 = pcm2(end, end);
                i = 1;
                validar = 1;
                while pcm2(i, end) != ultpc2
                    cpc2 = pcm2(i, end);
                    if and(-1 >= cpc2, cpc2 >= 1)
                        display("Hay un punto critico que se sale del intervalo ]-1, 1[")
                        validar = 0;
                        break;
                    else
                        i += 1;
                    end
                end
                
                if and(-1 >= ultpc, ultpc >= 1)
                    display("Hay un punto critico que se sale del intervalo ]-1, 1[")
                    validar = 0;
                else
                    if validar == 1
                        k = 0;
                        error = tol + 1;
                        e = [];
                        while and(error > tol, k < iterMax)
                            k = k + 1;
                            xk = func(xk0);
                            error = abs(func(xk) - xk);
                            e = [e error];
                            xk0 = xk;
                        end
                        plot(1 : k, e)
                    else
                        xk = []; 
                        k = []; 
                        error = [];
                    end
                end
            else
                xk = []; 
                k = []; 
                error = [];
            end
        end
    end
end

help punto_fijo

[xk, k, error] = punto_fijo('cos(x) + 10', 1, -1, 1, 10^-8, 50)
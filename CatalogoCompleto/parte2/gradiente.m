pkg load symbolic;
syms x y;

function [xk, k, error] = gradiente(func, x0, y0, tol, iterMax)
  
  %Esta funcion aproxima la solucion de la ecuacion f(x) = 0, utilizando el metodo del gradiente conjugado no lineal.
  %
  %Sintaxis: gradiente(f, x0, y0, tol, iterMax).
  %
  %Parametros iniciales:
  %
  %            f = representa la funcion f.
  %            x0 = valor inicial de x.
  %            y0 = valor inicial de y.
  %            tol = un numero positivo que representa la tolerancia para el criterio (error < tol).
  %            iterMax = cantidad de iteraciones maximas.
  %
  %Parametros de salida:
  %            xk = solucion aporximada de la funcion.
  %            k = numero de iteraciones realizados.
  %            error = |f(x)|
  syms x y;
  
  g = gradient(func);
  xk = [x0; y0];
  gk = double (subs(g,[x y],xk));#gradiente evaluado en valores iniciales
  gk_plus1 = 0;
  dk = -gk;#valor inicial de d
  bk = 0;
  a = 1; #valor inicial de alpha
  sigma = 0.5; #constante para calcular alpha
  listError = [];
  
  for k = 0:iterMax
    for j = 1: iterMax #se calcula alpha
      izq = double(subs(func,[x y],(xk+a*dk)') - subs(func,[x y],xk'));
      der = double (sigma*a*(subs(g,[x y],xk'))'*dk);
      if (izq<der)
        break;
      else
        a = a/5;
      endif
    endfor
    
    gk = double (subs(g,[x y],xk));
    xk = xk + a*dk; #actualiza el xk
    gk_plus1 = double (subs(g,[x y],xk));
    error = norm(gk_plus1);
    listError = [listError;error];
    
    if (error<tol)  
      break;
    else
      bk = (norm(gk_plus1)^2) / (norm(gk)^2);       
      dk = -gk_plus1 + bk*dk;
    endif
  endfor
  plot(1:k+1,listError)

endfunction
help gradiente
[xk, k, error] = gradiente(((x-2)^4+(x-2*y)^2), 2, 4, 10**-5, 10)
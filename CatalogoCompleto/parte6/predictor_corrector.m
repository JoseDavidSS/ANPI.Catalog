pkg load symbolic

function [x, y] = predictor_corrector(f, a, b, y0, n)

  %Esta función encuentra una aproximación a la solución del problema 
  %de Cauchy con el método predictor-corrector.
  %
  %Sintaxis: predictor_corrector(f, a, b, y0, n)
  %
  %Parámetros Iniciales: 
  %            f = función de dos variables x y y
  %            a = inicio del intervalo
  %            b = final del intervalo
  %            y0 = valor inicial de y
  %            n = cantidad de subintervalos a realizar
  %   
  %Parámetros de Salida:                           
  %            x = vector con las soluciones del par ordenado x
  %            y = vector con las soluciones del par ordenado y
  
  func = matlabFunction(sym(f));
  
  h = (b - a) / (n - 1);
  i = 1;
  x(i) = a;
  
  while i < n
    x(i + 1) = a + (i * h);
    i += 1;
  end
  
  y(1) = y0;
  i = 2;
  
  while i < n + 1
    yPrima(i) = y(i - 1) + (h * func(x(i - 1), y(i - 1)));
    temp = (func(x(i - 1), y(i - 1)) + func(x(i), yPrima(i))) / 2;
    y(i) = y(i - 1) + (h * temp);
    i += 1;
  end
  
  stem(x, y)
  
end

help predictor_corrector

[x, y] = predictor_corrector('y - x**2 + 1', 0, 2, 0.5, 11)
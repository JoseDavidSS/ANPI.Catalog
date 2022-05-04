pkg load symbolic;


function result = trapecio_compuesto(funcion, puntos, intervalo)
  %Esta funcion aproxima la integral de una funcion en un intervalo
  % mediante el metodo del trapecio compuesto.
  %
  % Sintaxis: trapecio_compuesto(funcion, puntos, intervalo).
  %
  % Parametros iniciales:
  %  funcion = representa la funcion f.
  %  puntos = numero entero en que se divide el intervalo.
  %  intervalo = vector que contiene los puntos a y b en que se evalua la funcion.
  %
  % Parametros de salida:
  %  sum = aproximacion de la integral.
  %  error = cota de error del metodo.
  
  % Preparamos la funcion y los parametros iniciales
  ff = funcion;
  func = function_handle(sym(ff));
  syms x;
  
  a = intervalo(1);
  b = intervalo(2);
  h = (b-a)/(puntos-1);
  
  % Calculamos el area
  sum = 0;
  for i=0:puntos-2
    x_k = a + i*h;
    x_k1 = a + (i+1)*h;
    sum = sum + (func(x_k)+func(x_k1));
  endfor
  sum = h*sum/2;
  
  % Calculamos el error
  fd=diff(func,x)
  fdd = diff(fd,x);
  fdd_aux = function_handle(-1*abs(fdd));
  max = fminbnd(fdd_aux,a,b);
  error = abs((h**2)*(b-a)*fdd_aux(max)/12);
  
  % Acoplamos el resultado
  result = [sum, error];
endfunction

trapecio_compuesto('ln(x)', 4, [2,5])
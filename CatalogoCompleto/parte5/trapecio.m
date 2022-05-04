pkg load symbolic;


function result = trapecio(funcion, intervalo)
  % Esta funcion aproxima la integral de una funcion en intervalo
  % mediante el metodo del trapecio.
  %
  % Sintaxis: trapecio(funcion, intervalo).
  %
  % Parametros iniciales:
  %  funcion = representa la funcion f.
  %  intervalo = vector que contiene los puntos a y b en que se evalua la funcion.
  %
  % Parametros de salida:
  %  area = aproximacion de la integral.
  %  error = cota de error del metodo.
  
  % Preparamos la funcion y los parametros iniciales
  ff = funcion;
  func = function_handle(sym(ff));
  syms x;
  a = intervalo(1);
  b = intervalo(2);
  
  % Calculamos el area
  h = b-a;
  area = (func(a)+func(b))*(h/2);
  
  % Calculamos el error
  fd=diff(func,x);
  fdd = diff(fd,x);
  fdd_aux = function_handle(-1*abs(fdd));
  max = fminbnd(fdd_aux,a,b);
  error = abs((h**3)*fdd_aux(max)/12);
  
  % Acoplamos el resultado
  result = [area, error];
endfunction

trapecio('ln(x)', [2,5])
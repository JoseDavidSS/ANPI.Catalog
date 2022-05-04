function ejecucion()
     clc

     x_0 = [1; 1; 1];
     A =[-3 1 0;1 -2 1;0 1 -3];
     
     [valor, vector]=potencia(A, x_0);
     
     fprintf('valor propio apropximado: ');
     valor
     fprintf('vector propio correspondiente: ');
     vector
endfunction

function [valor, vector] = potencia(matriz, vector_0)
  %Esta funcion aproxima el calculo de el
  %valor propio de mayor magnitud una matrix de entrada. 
  %
  %Sintaxis: potencia(matriz, vector_0).
  %
  %Parametros iniciales:
  %
  %            matriz = matriz de entrada simetrica definida positiva.
  %            vector_0 = vector de valor inicial.
  %
  %Parametros de salida:
  %            valor = aproximación de valor propio de mayor magnitud de la matriz.
  %            vector = vector propio correspondiente.  
  
  % Definimos valores iniciales
  x_0 = vector_0;
  iterMax = 100;
  tol = 10**-10;
  error = 1;
  error_vect = [];
  
  %Iniciamos iteraciones del metodo
  for (n=1:iterMax)
    %Calculos carecteristicos
    y_k = matriz * x_0;
    c_k = norm(y_k,Inf);
    x_k = (1/c_k)*y_k;
    
    %Calculo del error
    err = norm(x_k-x_0);
    
    %Actualizacion de variables
    x_0 = x_k;
    error_vect = [ error_vect,  err ];
    
    %Condicion de parada
    if (error < tol)
      break
    endif
  
  endfor
  
  %Valores finales
  valor = c_k;
  vector = x_0';

  %Finalmente, graficamos
  plot(0:length(error_vect)-1,error_vect)
  title('Metodo de Potencia')
  xlabel('Iteracion')
  ylabel('Error')

endfunction



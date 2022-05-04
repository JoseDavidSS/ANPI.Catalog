
% Funcion con los pasos para graficar y probar el metodo
function adam_bashford_4 ()
  clc; clear;
  
  f = '1 - (y - x + 2) ^ 2 - x + 4';
  n = 6;
  startValue = [1 1 0.5 2]; 
  interval = [2 4];
  [xv, yv, interPol] = adam_bashford_4_method(f, interval, n, startValue)
  hold on
  
  % Grafica de la solucion con el metodo
  % (rojo)
  xG = interval(1) : 0.0001 : interval(2);
  pol1 = matlabFunction(sym(interPol));
  yP = pol1(xG);
  plot(xG, yP, 'r')
  
  % Grafica analitica
  % (azul)
  yS = @(x) -1 * (x - 1).^(-1) + x
  xG = interval(1):0.0001:interval(2);
  yG = yS(xG);
  plot(xG, yG, 'b')
  title('Grafica de soluciones analitica (azul) y del polinomio de interpolacion (rojo)')
  xlabel('x')
  ylabel('y(x)')
  
endfunction


% Entradas:
%   f: funcion f.
%   interval: intervalo que contiene el valor inicial y final
%   num: corresponde al numero de puntos con el que se
%     realizara el analisis.
%   val_inicial: corresponde al conjunto de valores iniciales
%     que necesita este metodo para ejecutarse

% Salidas:
%   xv, yv: son lo vectores que componen los pares ordenados de los
%     valores aproximados de la solucion del problema.
%   interPol: es el polinomio de interpolacion calculado por medio del 
%     metodo de lagrange para los puntos indicados.
  
  
function [xv, yv, interPol] = adam_bashford_4_method(f, interval, num, startValue)

  pkg load symbolic;
  syms x y;
  f1 = matlabFunction(sym(f));
  
  a = interval(1);
  b = interval(2);
  h = (b - a) / (num - 1);
  
  xv = a : h : b;
  
  y0 = startValue(1);
  y1 = startValue(2);
  y2 = startValue(3);
  y3 = startValue(4);
  
  yv = [y0 y1 y2 y3];

  for n = 4 : num - 1
    
    fk = f1(xv(n), yv(n));
    fk1 = f1(xv(n - 1), yv(n - 1));
    fk2 = f1(xv(n - 2), yv(n - 2));
    fk3 = f1(xv(n - 3), yv(n - 3));
    yv(n + 1)= yv(n)+ (h / 24) * (55 * fk - 59 * fk1 + 37 * fk2 - 9 * fk3);
    
  endfor
  
  
  interPol = metodo_lagrange(xv, yv);
  
endfunction


function Lk = lk(xv, k)
  
  syms x
  n = length(xv) - 1;
  Lk = 1;
  for j = 0 : n
    
    if j ~= k
      Lk = Lk * (x - xv(j + 1)) / (xv(k + 1) - xv(j + 1));
      
    endif  
    
  endfor
  
  Lk = expand(Lk);
  
endfunction


% Metodo de Lagrange

% Parametros de entrada:
%   xv, yv: vetores de los pares ordenador
function p = metodo_lagrange(xv, yv)
  
  syms x
  n = length(xv) - 1;
  p = 0;
  
  for k = 0 : n
    p = p + yv(k + 1) * lk(xv, k);
  endfor
  
  p = expand(p);
  
endfunction


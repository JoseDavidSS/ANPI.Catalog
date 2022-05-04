function test
     pkg load symbolic
     clc;
     
     f = 'cos((x)/2)';
     
     ptos = [-5 0 5];

     valor = 0.4;
     
     cota = cota_poly_inter(f, ptos)
end



% Calcula el error de una aproximacion con un polinomio de interpolacion
% Param f: cadena de caracteres
% Param puntos: vector de los puntos de soporte
% Retorna: Cota del error

function cota = cota_poly_inter(f, puntos)

     n = length(puntos) - 1;
    
     fs = sym(f);
     
     a = puntos(1);
     b = puntos(end);
     
     alpha = alpha(fs, n + 1, a, b);
  
     xMax = polyMax(puntos, a, b);
     
     result = 1;
     for k = puntos
          result *= abs(xMax - k);
     end
     cota = alpha / factorial(n + 1) * result;
     
endfunction


% Calcula el alpha_max
% Retorna: funcion evaluada en punto maximo
function alpha = alpha(fs, m, a, b)

     fn = matlabFunction(fs);
     
     dfm_s = diff(fs, m);
     
     dfm_n = matlabFunction(dfm_s);
  

     fs_aux = -1 * abs(dfm_s);
     
     fn_aux = matlabFunction(fs_aux); 
     
     xMax = fminbnd(fn_aux, a, b);
     
     alpha = abs(dfm_n(xMax));
     
endfunction


% Calcula el puntos maximo
% Retorna: Preimagen del punto maximo
function xMax = polyMax(puntos, a, b)

     syms x;
     f = 1;
     for i = puntos
          f *= (x - i);
     end
     
     f = expand(f);
     
     fs = sym(f);
     
     fn = matlabFunction(fs);
     
     f1 = diff(f, x);
     
     critical_pts = flip(solve(f1)');
     
     X = [fn(a), fn(b), critical_pts];
     
     Y = [];
     
     for k = 1 : length(X)
       
          punto = double(X(k));
          
          if (a < punto) & (punto < b)
            
               Y = [Y, abs(fn(punto))];
               
          else
               X(k) = [];
               
          endif
     end
     
     [yMax index] = max(Y);
     
     xMax = double(X(index));

endfunction



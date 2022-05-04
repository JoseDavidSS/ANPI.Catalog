#{
Params
    f  =  Funcion f en forma de string
    n: numero de orden
    a : limite menor del intervalo
    b : limite mayor del intervalo
        
Parametros de Salida: 
    aprox :  aproximacion
    cota : cota del error de la aproximacion
#}
  

function [I cota]  =  cuad_gaussiana(f,n,a,b)

  pkg load symbolic
  warning('off','all');
  syms x;
  
  cota  =  0;
  I  =  0;
  fs  =  sym(f);
  y  =  ((b - a) * x + (b + a)) / 2;
  gs  =  (b - a) / 2 * subs(fs, x, y);
  gn  =  matlabFunction(gs);
  
  [x, w]  =  ceros_cuad_gaussiana(n);
  
 # Cuadratura gaussiana
  for i  =  1 : n  
    I + =  w(i) * gn(x(i));
  endfor
  
  if n  =  =  2
    # Simbolica
    f2_s  =  abs(diff(gs, 4));
    # Numerica
    f2_n  =  matlabFunction(f2_s);

        
    # Simbolica
    fs_aux  =  (-1) * abs(f2_s);
    # Numerica
    fn_aux  =  matlabFunction(fs_aux);

    # Alpha max
    x_max  =  fminbnd(fn_aux, -1, 1);
    alpha  =  f2_n(x_max);

    #Calculo de la cota.
    cota  =  alpha / 135  # cota.
    
  end
end


function [x, m]  =  ceros_cuad_gaussiana(n)
  if n > 10 | n < 2
    x  =  0;
    m  =  0;
    
  else   
    x  =  []; m  =  [];
    if n  =  =  2
      x(1)  =  -0.5773502692;
      x(2) = -x(1);
      
      m(1)  =  1;
      m(2)  =  1;
      
    elseif n == 3
      x(1) = -0.7745966692;
      x(2) = 0;
      x(3) = -x(1);
      
      m(1) = 0.5555555555;
      m(2) = 0.888888888;
      m(3) = m(1);
      
    elseif n == 4
      x(1) = -0.86113631159405;
      x(2) = -0.339981043584856;      
      x(3) = -x(2);      
      x(4) = -x(1);
      
      m(1) = 0.347854845137454;
      m(2) = 0.652145154862546;
      m(3) = m(2);
      m(4) = m(1);
      
    elseif n == 5
      x(1) = -0.9061798459;
      x(2) = -0.5384693101;
      x(3) = 0;
      x(4) = -x(2);
      x(5) = -x(1);
      
      m(1) = 0.2369268851;
      m(2) = 0.4786286705;
      m(3) = 0.5688888889;
      m(4) = m(2);
      m(5) = m(1);
      
    elseif n == 6
      x(1) = -0.9324695142;
      x(2) = -0.6612093865;
      x(3) = -0.2386191861;
      x(4) = -x(3);
      x(5) = -x(2);
      x(6) = -x(1);
      
      m(1) = 0.1713244924;
      m(2) = 0.3607615730;
      m(3) = 0.4679139346;
      m(4) = m(3);
      m(5) = m(2);
      m(6) = m(1);
      
    elseif n == 7
      x(1) = -0.9491079123;
      x(2) = -0.7415311856;
      x(3) = -0.4058451514;
      x(4) = 0;
      x(5) = -x(3);
      x(6) = -x(2);
      x(7) = -x(1);
      
      m(1) = 0.1294849662;
      m(2) = 0.2797053915;
      m(3) = 0.3818300505;
      m(4) = 0.4179591837;
      m(5) = m(3);
      m(6) = m(2);
      m(7) = m(1);
      
    elseif n == 8
      x(1) = -0.9602898565;
      x(2) = -0.7966664774;
      x(3) = -0.5255324099;
      x(4) = -0.1834346425;
      x(5) = -x(4);
      x(6) = -x(3);
      x(7) = -x(2);
      x(8) = -x(1);
      
      m(1) = 0.1012285363;
      m(2) = 0.2223810345;
      m(3) = 0.3137066459;
      m(4) = 0.3626837834;
      m(5) = m(4);
      m(6) = m(3);
      m(7) = m(2);
      m(8) = m(1);
      
    elseif n == 9
      x(1) = -0.9681602395;
      x(2) = -0.8360311073;
      x(3) = -0.6133714327;
      x(4) = -0.3242534234;
      x(5) = 0;
      x(6) = -x(4);
      x(7) = -x(3);
      x(8) = -x(2);
      x(9) = -x(1);
      
      m(1) = 0.0812743883;
      m(2) = 0.1806481607;
      m(3) = 0.2606106964;
      m(4) = 0.3123470770;
      m(5) = 0.3302393550;
      m(6) = m(4);
      m(7) = m(3);
      m(8) = m(2);
      m(9) = m(1);
      
    elseif n == 10
      x(1) = -0.9739065285;
      x(2) = -0.8650633667;
      x(3) = -0.6794095683;
      x(4) = -0.4333953941;
      x(5) = -0.1488743390;
      x(6) = -x(5);
      x(7) = -x(4);
      x(8) = -x(3);
      x(9) = -x(2);
      x(10) = -x(1);
      
      m(1) = 0.0666713443;
      m(2) = 0.1494513492;
      m(3) = 0.2190863625;
      m(4) = 0.2692667193;
      m(5) = 0.2955242247;
      m(6) = m(5);
      m(7) = m(4);
      m(8) = m(3);
      m(9) = m(2);
      m(10) = m(1);
      
    end
  end
end
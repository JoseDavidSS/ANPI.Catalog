import numpy as np
import  sympy as sp

'''
Esta funcion permite obtener los polinomios de interpolacion grado 3
de una funcion.

Sintaxis : traz_cubico(x_k, y_k)

Parametros Iniciales :
    x_k: corresponde al vector de las preimagenes en un intervalo
    y_k: vector de imagenes de x_k evaluada en una funcion
Parametros de Salida :
    trazadores: vector de polinomios de interpolacion
'''
def traz_cubico(x_k, y_k):
    # Primero se construye el vector de h_k
    h_k = vectorH_k(x_k)
    
    # Segundo se construye el vector de u_k
    u_k = vectorU_k(y_k, h_k)
    
    #Tercero se contruye la tridiagonal
    tridiagonal = construirTridiagonal(h_k)
    
    #Cuarto se calcula la solucion M del sistema A*M=U por metodo de Thomas
    M = thomas(tridiagonal,u_k.transpose())
    
    #Quinto se calculan los coeficientes a,b,c,d y se calculan los trazadores S_i
    trazadores = vectorTrazadores(M, h_k, x_k, y_k)
    
    

def vectorH_k(x_k):
    h_k = []
    for i in range(len(x_k)-1):
        h_k.append(x_k[i+1]-x_k[i])
    return h_k

def vectorU_k(y_k, h_k):
    u_k = np.zeros((1,len(y_k)-2))
    for i in range(len(y_k)-2):
        tmp = (y_k[i+2]-y_k[i+1])/h_k[i+1]
        tmp2 = (y_k[i+1]-y_k[i])/h_k[i]
        u_k[0][i] = (6*(tmp - tmp2))
    return u_k

def construirTridiagonal(h_k):
    m = len(h_k)-1
    tridiagonal = np.zeros((m,m))
    for i in range(m):
        tmp = np.zeros(m)
        if (i==0):
            tmp[i+1] = h_k[i+1]
        elif (i==(m-1)):
            tmp[i-1] = h_k[i]
        else :
            tmp[i-1]=h_k[i]
            tmp[i+1] = h_k[i+1]
        tmp[i] = 2*(h_k[i]+h_k[i+1])
        tridiagonal[i] = tmp
    return tridiagonal


def is_tridiagonal(a):
    dims=a.shape

    for i in range(dims[0]):
        for j in range(dims[1]):
            if(j>i+1 and a[i,j]!=0):
                return False
            elif(j<i-1 and a[i,j]!=0):
                return False
    return True

def thomas(a,b):
    if(is_tridiagonal(a)):
        n=len(b)
        a_s=[]
        b_s=[]
        c_s=[]
        d_s=b.transpose();
        p_s=[]
        q_s=[]
        xk =np.zeros((1,n))
        for i in range(n):
            if(i==0):
                a_s.append(0)
                b_s.append(a[i,i])
                c_s.append(a[i,i+1])
            elif(i==n-1):
                a_s.append(a[i,i-1])
                b_s.append(a[i,i])
                c_s.append(0)
            else:
                a_s.append(a[i, i - 1])
                b_s.append(a[i, i])
                c_s.append(a[i, i + 1])
        n=len(b)
        qi=0
        pi=0
        for i in range(n):
            if(i==0):
                p_s.append(c_s[i]/b_s[i])
                q_s.append(d_s[0,i]/b_s[i])

            else:
                if(i!=n-1):
                    p_s.append(c_s[i]/(b_s[i]-p_s[i-1]*a_s[i]))
                    q_s.append((d_s[0,i]-q_s[i-1]*a_s[i])/(b_s[i]-p_s[i-1]*a_s[i]))
                else:
                    q_s.append((d_s[0, i] - q_s[i - 1] * a_s[i]) / (b_s[i] - p_s[i - 1] * a_s[i]))
        for j in range(n-1,-1,-1):
            if(j==n-1):
                xk[0,j]=q_s[j]
            else:
                xk[0,j]=q_s[j]-p_s[j]*xk[0,j+1]
        
        m_k = []
        m_k.append(0)
        for i in range(n):
            m_k.append(xk[0,i])
        m_k.append(0)
        
        return m_k
    else:
        print("La matriz no es tridiagonal")
        return None

def vectorTrazadores(M_k, h_k, x_k, y_k):
    trazadores = []
    x = sp.symbols('x')

    for i in range(len(h_k)):
        a= (M_k[i+1]-M_k[i])/(6*h_k[i])
        b= M_k[i]/2
        c= ((y_k[i+1]-y_k[i])/h_k[i])-((h_k[i]*(M_k[i+1]+2*M_k[i]))/6)
        d= y_k[i]
        polinomio= a*(x-x_k[i])**3+b*(x-x_k[i])**2+c*(x-x_k[i])+d
        trazadores.append(polinomio)

    return trazadores


# --------------- Ejemplo de la presentacion --------------
x_k = [1,1.05,1.07,1.1]
y_k = [2.718282, 3.286299, 3.527609, 3.905416]
traz_cubico(x_k, y_k)

import numpy as np


def producto_punto(x, y):
    result = 0
    for i in range(len(x)):
        result += x[i] * y[i]
    return result


def factorizacion_QR(A):
    A = np.array(A)
    Q = []
    for i in range(len(A)):
        Ak = A[:, i]
        if i == 0:
            U = Ak
        else:
            sum = 0
            for j in range(i):
                sum += producto_punto(Ak, Q[j]) * np.array(Q[j])
            U = A[:, i] - sum
        P = U / np.linalg.norm(U)
        Q.append(P.tolist())
    R = np.dot(Q, A)
    Q = np.transpose(Q)
    return Q, R


"""
Metodo QR para el calculo de autovalores de una matriz
Entradas: Matriz y tolerancia minima
Salidas: Valores propios de la matriz
"""
def metodo_QR(A, tol):
    error = tol
    while error >= tol:
        QR = factorizacion_QR(A)
        A = np.dot(QR[1], QR[0])
        error = 0
        for i in range(1, len(A)):
            for j in range(i):
                error += abs(A[i][j])
    return np.diagonal(A)


print(metodo_QR([[5, 0, 2], [1, 2, 3], [8, 1, 4]], 0.000005))

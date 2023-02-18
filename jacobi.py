from math import *
from pprint import pprint

def distinf(x, y):
    return max([abs(x[i] - y[i]) for i in range(len(x))])

def jacobi(A, b, x0, tol, max):
    n = len(A)
    x = [0.0 for x in range(n)]
    k = 1
    while k <= max:
        for i in range(n):
            if abs(A[i][i]) <= 1e-15:
                print("Imposible iterar")
                return None
            s = sum([A[i][j] * x0[j] for j in range(n) if j != i])
            x[i] = (b[i] - s) / A[i][i]
        pprint(x)
        if distinf(x, x0) < tol:
            print(r"Solucion encontrada")
            return x
        k += 1
        for i in range(n):
            x0[i] = x[i]
    print("Iteraciones agotadas")
    return None

A = [[2, -1, 1, 1], [2, 2, 2, -4], [-1, -1, 2, 5]]
b = [1, 2, -1]
x0 = [0, 0, 0]

print("Matriz A:")
pprint(A)
print("Vector b:")
pprint(b)
print("Vector x0:")
pprint(x0)
print("Iteracion de Jacobi")
jacobi(A, b, x0, 1e-16, 100)
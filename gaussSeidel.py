from math import *
from pprint import pprint

def distinf(x, y):
    return max([abs(x[i] - y[i]) for i in range(len(x))])

def gaussSeidel(A, b, x0, tol, max):
    n = len(A)
    x = [0.0 for x in range(n)]
    k = 1
    while k <= max:
        for i in range(n):
            if abs(A[i][i]) <= 1e-15:
                print("Imposible iterar")
                return None
            s1 = sum([A[i][j] * x[j] for j in range(i)])
            s2 = sum([A[i][j] * x0[j] for j in range(i + 1, n)])
            x[i] = (b[i] - s1 - s2) / A[i][i]
        pprint(x)
        if distinf(x, x0) < tol:
            print(r"Solucion encontrada")
            return x
        k += 1
        for i in range(n):
            x0[i] = x[i]
    print("Iteraciones agotadas")
    return None

A = [[10, -1, 2, 0], [-1, 11, -1, 3], [2, -1, 10, -1], [0, 3, -1, 8]]
b = [6, 25, -11, 15]
x0 = [0, 0, 0, 0]

print("Matriz A:")
pprint(A)
print("Vector b:")
pprint(b)
print("Vector x0:")
pprint(x0)
print("Iteracion de Gauss-Seidel")
gaussSeidel(A, b, x0, 1e-15, 100)

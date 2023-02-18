# Método de la bisección

from math import *

# Se define la función

def fun(x):
    return x**3 + 4*x**2 - 10

# Función de la bisección

def bi(fun, a, b, tole, n):
    i = 1;
    while i <= n:
        p = a + (b - a) / 2
        print("i = {0:<2}, p = {1:.12f}".format(i, p))
        if abs(f(p)) <= 1e-15 or (b - a)/2 < tol:
            return p
        i += 1
        if f(a)*f(b) > 0:
            a = p
        else:
            b = p
    print("Iteraciones agotadas: Error!")
    return None


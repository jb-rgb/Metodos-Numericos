from math import *
import math
from tkinter import N

def fun1(x):
    return x**3 - x - 1

def fun2(x):
    return 2*math.sin(math.pi*x) + x

def fun3(x):
    return 3*x**2 - math.e**x

def fun4(x):
    return x - math.cos(x)

def puntoFijo(fun, p0, tol, n):
    i = 1
    while i <= n:
        p = fun(p0)
        print("Iterador = {0:<2}, p = {1:.12f}".format(i, p))
        if abs(p - p0) < tol:
            return p
        p0 = p
        i = i + 1
    print("Iteraciones agotadas: Error!")
    return None

# print("Punto fijo de x^3 - x - 1: ")
# puntoFijo(fun1, 1, 1e-8, 100)

# print("Punto fijo de 2*sin(pi*x) + x: ")
# puntoFijo(fun2, 1, 1e-8, 100)

# print("Punto fijo de 3*x^2 - e^x: ")
# puntoFijo(fun3, 0, 1e-8, 100)

print("Punto fijo de x - cos(x): ")
puntoFijo(fun4, 0, 1e-8, 100)
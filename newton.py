from hashlib import new
from math import *

def fun(x):
    return cos(x) - x

def funPrima(x):
    return -sin(x) - 1

def newton(fun, funPrima, p0, tol, n):
    i = 1
    while i <= n:
        p = p0 - fun(p0) / funPrima(p0)
        print("Iteracion = {0:<2}, p = {1:.12f}".format(i, p))
        if abs(p - p0) < tol:
            return p
        p0 = p
        i = i + 1
    print("Iteraciones agotadas: Error!")
    return None

print("Metodo Newton-Rahpson de cos(x) - x: ")
newton(fun, funPrima, pi/4, 1e-8, 100)
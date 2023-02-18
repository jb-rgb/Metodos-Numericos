from math import *
from tkinter.messagebox import NO

def fun(x):
    return cos(x) - x

def secante(fun, p0, p1, tol, n):
    i = 2
    while i <= n:
        p = p1 - (fun(p1) * (p1 - p0) / (fun(p1) - fun(p0)))
        print("Iteracion = {0:<2}, p = {1:.12f}".format(i, p))
        if abs(p - p1) < tol:
            return p
        p0 = p1
        p1 = p
        i = i + 1 
    print("Iteraciones agotadas: Error!")
    return None

print("metodo de la secante de cos(x) - x: ")
secante(fun, 0.5, pi/4, 1e-8, 100)
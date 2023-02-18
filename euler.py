from math import *

def f(t, y):
    return (-5*y) + (5*t**2) + (2*t)

def Euler(a, b, y0, f, N):
    h = (b - a) / N
    t = a
    w = y0
    print("t0 = {0:.2f}, w0 = {1:.12f}".format(t, w))
    for i in range(1, N+1):
        w = w + h*f(t, w)
        t = a + i*h
        print("t{0:<2} = {1:.2f}, w{0:<2} = {2:.12f}".format(i, t, w))
    return w

a = int(input('Introduzca el valor de a: '))
b = int(input('Introduzca el valor de b: '))
y0 = float(input('Introduzca el valor de y0: '))
N = int(input('Introduzca el valor de N: '))

print('\nMetodo de Euler:')
Euler(a, b, y0, f, N)
from math import *
from numpy import *

a = int(input("Ingrese el valor del limite inferior: "))
b = int(input("Ingrese el valor del limite superior: "))
n = int(input("Ingrese el numero de particiones: "))
f = input("Ingrese la funcion: ")
fx = lambda x: eval(f)

def simpson(f, a, b, n):
    h = 0.25
    oddSum = 0
    evenSum = 0
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            evenSum += 2 * f(x)
        else:
            oddSum += 4 * f(x)
    return (h / 3) * (f(a) + oddSum + evenSum + f(b))

print("{0:.12f}".format(simpson(fx, a, b, n)))
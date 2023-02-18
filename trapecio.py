from math import *

# Funcion a integrar
def f(x):
    return (x**2) * (e**(-x**2))

# Integral exacta
# def I(a,b):
#     return (e**b - e**a)

# Trapecio
def trapecio(f, a, b, n):
    h = 0.25 #(b - a) / float(n) 
    acum = 0.0
    for i in range(1, n):
        acum += 2 * f(a + i * h)
        print(acum)
    aprox = (h / 2.0) * (f(a) + acum + f(b))
    return aprox

# print("\nArea bajo la curva de e^x de la integral exacta: \n")
# print("{0:.12f}".format(I(0, 4)))

print("\nArea bajo la curva de la integral aproximada con 2 particiones: \n")
print("{0:.12f}".format(trapecio(f, 0, 2, 10)))

# print("\nArea bajo la curva de e^x de la integral aproximada con 100 particiones: \n")
# print("{0:.12f}".format(trapecio(f, 0, 4, 100)))

# print("\nArea bajo la curva de e^x de la integral aproximada con 1000 particiones: \n")
# print("{0:.12f}".format(trapecio(f, 0, 4, 1000)))

# print("\nArea bajo la curva de e^x de la integral aproximada con 10000 particiones: \n")
# print("{0:.12f}".format(trapecio(f, 0, 4, 10000)))

# print("\nArea bajo la curva de e^x de la integral aproximada con 100000 particiones: \n")
# print("{0:.12f}".format(trapecio(f, 0, 4, 100000)))

# print("\nArea bajo la curva de e^x de la integral aproximada con 1000000 particiones: \n")
# print("{0:.12f}".format(trapecio(f, 0, 4, 1000000)))

# print("\nArea bajo la curva de e^x de la integral aproximada con 10000000 particiones: \n")
# print("{0:.12f}".format(trapecio(f, 0, 4, 10000000)))
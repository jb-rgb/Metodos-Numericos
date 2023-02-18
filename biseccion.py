from math import *
 
# función 1
# def fun(x):
#     return x**3 + 4*x**2 - 10 

# funcion 2
# def fun(x):
#     return x**3 - 10*x**2 + 5

# funcion 3
def fun(x):
    return x - tan(x)

def biseccion(f,a,b,E):
    n = 50 #numero de máximo de iteraciones
    i=1
    while i<=n: 
        p=a+((b-a)/2)
        print("i = {0:<2}, p = {1:.12f}".format(i, p))
        if abs(f(p)) <= 1e-15 or (b - a)/2 < E:
            return p
        i += 1
        if f(a)*f(p) > 0:
            a = p
        else:
            b = p
    print("Iteraciones agotadas: Error!")
    return None


# print("\nBisección función x**3 + 4*x**2 - 10:")
# biseccion(fun, 1, 2, 1e-10)

# print("\nBisección función x**3 - 10*x**2 + 5:")
# biseccion(fun, 0.6, 0.8, 1e-10)

print("\nBisección función x - tan(x):")
biseccion(fun, 0, 20, 1e-10)
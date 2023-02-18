import numpy as np

def f1(x, y):
    return x**2 - 10*x + y**2 + 8

def f2(x, y):
    return x*y**2 + x - 10*y + 8

def df1x(x, y):
    return 2*x - 10

def df2y(x, y):
    return 2*y*x - 10

def newtonModificadoNoLineal(f1, f2, df1x, df2y, x, y, iterMax, tol):
    cumple = False
    k = 0
    while not cumple and k < iterMax:
        x = x - (f1(x, y) / df1x(x, y))
        y = y - (f2(x, y) / df2y(x, y))
        print('Iteracion {}: x = {} y = {}'.format(k, x, y))
        cumple = np.linalg.norm(f1(x, y)) <= tol and np.linalg.norm(f2(x, y)) <= tol
        k += 1
    if k < iterMax:
        return x, y
    else:
        raise ValueError('No converge')

def main():
    x0 = 0
    y0 = 0
    raiz = newtonModificadoNoLineal(f1, f2, df1x, df2y, x0, y0, 100, 1e-10)
    print('f1({}) = {}'.format(raiz, f1(raiz[0], raiz[1])))
    print('f2({}) = {}'.format(raiz, f2(raiz[0], raiz[1])))

main()
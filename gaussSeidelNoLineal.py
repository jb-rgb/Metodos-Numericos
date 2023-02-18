import numpy as np

def f(x):
    xk1 = x.copy()
    xk1[0] = 1/3*np.cos(x[1]*x[2]) + 1/6
    xk1[1] = 1/9*np.sqrt(x[0]**2 + np.sin(x[2]) + 1.06) -0.1
    xk1[2] = -1/20*np.exp(-x[0]*x[1]) - (10*np.pi - 3) / 60
    return xk1

def gaussSeidelNoLineal(f, x, iterMax, tol):
    cumple = False
    k = 0
    while not cumple and k < iterMax:
        x0 = x.copy()
        x = f(x0)
        norma = np.linalg.norm(x - x0)
        print('Iteracion {}: {} norma = {}'.format(k, x, norma))
        cumple = norma < tol
        k += 1
    if k < iterMax:
        return x
    else:
        raise ValueError('No converge')

def main():
    x = np.array([0.1, 0.1, -0.1])
    x = gaussSeidelNoLineal(f, x, 200, 1e-10)
    print('Solucion: ', x)

main()
import numpy as np

def f(x):
    return np.array([3*x[0] - np.cos(x[1]*x[2]) - 1/2, \
                     x[0]**2 - 81*(x[1] + 0.1)**2 + np.sin(x[2]) + 1.06, \
                     np.exp(-x[0]*x[1]) + 20*x[2] + (10*np.pi - 3) / 3])

def j(x):
    return np.array([[3, x[2]*np.sin(x[1]*x[2]), x[1]*np.sin(x[1]*x[2])], \
                     [2*x[0], -162*(x[1] + 0.1), np.cos(x[2])], \
                     [-x[1]*np.exp(-x[0]*x[1]), -x[0]*np.exp(-x[0]*x[1]), 20]])

def newtonNoLineal(f, j, x, iterMax, tol):
    cumple = False
    k = 0
    while not cumple and k < iterMax:
        deltaX = np.linalg.solve(j(x), -f(x))
        x = x + deltaX
        print('Iteracion {}: {}'.format(k, x))
        cumple = np.linalg.norm(f(x)) <= tol
        k += 1
    if k < iterMax:
        return x
    else:
        raise ValueError('No converge')

def main():
    x0 = np.array([0.1, 0.1, -0.1])
    raiz = newtonNoLineal(f, j, x0, 100, 1e-10)
    print('f({}) = {}'.format(raiz, f(raiz)))

main()
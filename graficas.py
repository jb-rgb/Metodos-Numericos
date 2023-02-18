from numpy import *
from matplotlib.pyplot import *

def f(x):
    return 1/x

def P(x):
    return 0.05*x**2 - 0.425*x + 1.15

x = linspace(0.1, 10, 100)
y1 = f(x)
y2 = P(x)
xlabel('x')
ylabel('y')
plot(x, y1, 'r-')
plot(x, y2, 'g-')
aux1 = [2, 2.5, 4]
aux2 = [1/2, 1/2.5, 1/4]
plot(aux1, aux2, "o")
legend(['f(x)', 'P(x)'])
show()
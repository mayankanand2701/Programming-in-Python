import math
def f(x):
    return x**2+math.sin(x)
def df(x):
    return 2*x +math.cos(x)
def gradient_descent(x0,rate, iteration):
    x=x0
    for j in range(iteration):
        x=x-rate*df(x)
    return x

x0=2
rate=0.1
iteration=5000
minima_point=gradient_descent(x0, rate, iteration)

print('Point of Minima : ', minima_point)
print('Minimum value of f(x) : ',f(minima_point))

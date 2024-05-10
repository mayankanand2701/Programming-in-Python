import math
def f(x):
    return math.exp(x**2)+math.sin(x)-math.tan(x)+math.log(x)
def derivative(x,h):
    return (f(x+h)-f(x))/h
h=0.0001
x=1
print('Derivative of f(x) at x=1 is : ', derivative(x,h))

import math
def f(x,y):
    return ((1-x)**2)+((y-(x**2))**2)

def df_dx(x,y):
    return -2*(1-x)-4*x*(y-x**2)

def df_dy(x,y):
    return 2*(y-x**2)

def gradient_descent(x0,yo, rate, iteration):
    x=x0
    y=y0
    for j in range(iteration):
        x=x-rate*df_dx(x,y)
        y=y-rate*df_dx(x,y)
    return [x,y]

x0,y0=0,0
rate=0.001
iteration=1000

xm,ym=gradient_descent(x0, y0, rate, iteration)
print('Point of Minima : ', xm,ym)
print('Minimum value of f(x,y) : ',f(xm,ym))

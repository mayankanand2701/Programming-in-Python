def f(x,y):
    return (1-x)**2 + 100*(y-x**2)**2
def derivative(x, y, h):
    c=(f(x+h,y)-f(x,y))/h
    d=(f(x,y+h)-f(x,y))/h
    return [c,d]
x,y=1,2
h=0.0001
print("Approximate derivatve of f(x) at x=1 : ",derivative(x, y, h))

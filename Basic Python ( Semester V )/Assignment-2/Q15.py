def fun(a=0, b=1):
    return (a**2 + b**2)

#a
#print(fun(2,a=3))
# Output : Error :fun() got multiple values for argument 'a'

#b
#print(fun(b=3,2))
# Output : SyntaxError : positional argument follow keyword argument

#c
#print(fun(3,b=2))
# Output : 13

#d
#print(fun(a=4,5))
# Output : Error : postional argumnet follow keyword argument

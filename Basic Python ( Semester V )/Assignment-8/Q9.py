a=int(input("Enter the base = "))
b=int(input("Enter the exponent = "))
def pow(a,b):
    if b==1:return a
    return a+pow(a,b-1)

print("The resultant number formed is = ",pow(a,b))

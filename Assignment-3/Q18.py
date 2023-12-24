def add(a,b):
    sum=0
    while(b>0):
        sum=sum+a
        b=b-1
    return sum

a=int(input("Enter the first number = "))
b=int(input("Enter the second number = "))
res=add(a,b)
print("The Reult is = ",res)


a=int(input("Enter the first number = "))
b=int(input("Enter the second number = "))
c=int(input("Enter the third number = "))

def max3(a,b,c):
    ans=max2(a,b)
    ans=max2(ans,c)
    return ans

def max2(a,b):
    ans=0
    if a>b:ans=a
    else: ans=b
    return ans

max=max3(a,b,c)
print("Maximum number is = ",max)



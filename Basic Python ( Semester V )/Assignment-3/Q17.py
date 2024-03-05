def gcd(a, b):
    # Euclidean algorithm to find the greatest common divisor (GCD)
    while b:
        a,b =b,a % b
    return a

n1=int(input("Enter the first number = "))
n2=int(input("Enter the second number = "))
res=gcd(n1,n2)
if(res==1):print("Co-Prime")
else: print("Not Co-Prime")

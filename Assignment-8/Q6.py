n=input("Enter the value of n = ")
def calculate(n):
    if n==0:return 0
    elif n==1:return 1
    else: return n+calculate(n-2)

print("The resultant is = ",calculate(6))

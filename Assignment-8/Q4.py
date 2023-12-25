n=int(input("Enter the terms = "))
def hsum(n):
    if n==1:return 1
    return 1/n+hsum(n-1)

print("The resulatant sum of the pattern is = ",hsum(n))

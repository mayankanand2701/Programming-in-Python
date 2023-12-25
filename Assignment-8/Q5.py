n=int(input("Enter the terms = "))
def gsum(n):
    if n==1:return 1
    return (2/2**n)+gsum(n-1)

print("The resulatant sum of the pattern is = ",gsum(n))

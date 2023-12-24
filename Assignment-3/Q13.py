x=int(input("Enter the value of x = "))
n=int(input("Enter the number of terms = "))

import math

def series_a(x, n):
    result = 0
    for i in range(n + 1):
        numerator = (-1) ** i * (x ** (2 * i))
        denominator = math.factorial(2 * i)
        result += numerator / denominator
    return result

res=series_a(x,n)
print(f"The sum of the {n} terms for series a is:",res)

def series_b(x, n):
    result = 0
    for i in range(n + 1):
        numerator = x ** i
        denominator = math.factorial(i)
        result += numerator / denominator
    return result

res=series_b(x,n)
print(f"The sum of the {n} terms for series b is :",res)


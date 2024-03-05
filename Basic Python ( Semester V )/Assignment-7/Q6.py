n=int(input("Enter the n value = "))
def generate(n):
    result = []
    for i in range(1, n+1):
        mult= [j * i for j in range(1, 6)]
        result.append(mult) 
    return result

ml= generate(n)
print(ml)

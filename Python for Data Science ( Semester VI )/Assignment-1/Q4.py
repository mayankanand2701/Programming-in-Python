import random

length=int(input("Enter the length of password : "))
nop=int(input("Enter the number of password you want to generate : "))

uc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lc="abcdefghijklmnopqrstuvwxyz"
dig="0123456789"

string=uc+dig+lc

print("Random Password's generated are : ")
for i in range(0,nop):
    res = ''.join(random.choices(string, k=length))
    print(str(res))
       
    




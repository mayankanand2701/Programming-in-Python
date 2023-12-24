row=int(input("Enter the  number of terms = "))
for i in range(1,row+1):
    print()
    for s in range(1,row-i+1):print("  ",end="")
    for j in range(i,0,-1): print(j,end=" ")
    for k in range(2,i+1): print(k,end=" ")

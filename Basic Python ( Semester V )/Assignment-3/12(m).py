row=int(input("Enter the  number of terms = "))
for i in range(1,row+1):
    print()
    for l in range(1,i):print("  ",end="")
    for j in range(i,row+1):
        print("$",end=" ")
        

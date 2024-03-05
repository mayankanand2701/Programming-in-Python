row=int(input("Enter the  number of terms = "))
for i in range(1,row+1):
    print()
    for j in range(1,row+1):
        if(i==1 or j==1 or i==row or j==row):print("* ",end=" ")
        else: print("  ",end=" ")

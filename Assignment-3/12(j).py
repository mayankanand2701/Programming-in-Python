n=int(input("Enter the number of terms ="))
for i in range(1,n+1):
    for k in range(1,i):
        print("  ",end="")
    for k in range(1,n-i+2):
        print("* ",end="")
    for k in range(i,n):
        print("* ",end="")
    print()
        

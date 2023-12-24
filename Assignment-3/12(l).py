n=int(input("Enter the number of terms ="))
for i in range(1,n+1):
    for k in range(1,n-i+1):
        print("  ",end="")
    for k in range(1,i+1):
        print("* ",end="")
    for k in range(1,i):
        print("* ",end="")
    print()
for i in range(1,n):
    for k in range(1,i+1):
        print("  ",end="")
    for k in range(1,n-i+1):
        print("* ",end="")
    for k in range(i,n-1):
        print("* ",end="")
    print()

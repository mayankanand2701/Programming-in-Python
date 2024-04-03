row=int(input("Enter the value of row : "))
column=int(input("Enter the value of column : "))

matrix=[]

for m in range(row):
    res=[]
    for n in range(column): res.append(m+n)
    matrix.append(res)

# For printing the matrix
print("The resultant matrix obtained is :")
for r in range(row):
    for c in range(column):
        print(matrix[r][c], end=" ")
    print()

        


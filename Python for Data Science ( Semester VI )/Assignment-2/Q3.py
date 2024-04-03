row=int(input("Enter the value of row : "))
column=int(input("Enter the value of column : "))

matrix=[]

for m in range(row):
    res=[]
    for n in range(column): 
            print("Enter the value for row number ",m,"& column number ",n)
            res.append(int(input()))
    matrix.append(res)

def extractRows():
        print("All the rows of the Matrices are : ")
        for i in matrix: print(i)
        
def extractColumns():
    print("All the columns of the Matrices are : ")
    # calculating the transponse of a matrix 
    transposedMatrix = []
    for i in range(column):
        res = []
        for j in range(row):
            res.append(matrix[j][i])
        transposedMatrix.append(res)
        
    for i in transposedMatrix:print(i)

extractRows()
extractColumns()
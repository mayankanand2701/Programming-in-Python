vector=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

vl=len(vector[0])
assert all(len(x)==vl for x in vector),"All vectors must be of the same length"

meanVector=[0,0,0]
for x in vector:
    for i,y in enumerate(x):
        meanVector[i]=meanVector[i]+y

# to calculate the mean
for i in range(0,vl):
    meanVector[i]=meanVector[i]/vl
        
print("The Component Wise Mean of the Vector is ",meanVector)
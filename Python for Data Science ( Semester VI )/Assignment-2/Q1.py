import math

# just writing this code for annotations
from typing import List
vector=List[float]

v1:vector=[1,2,-4,6]
v2:vector=[2,3,-1,0]

def addition(x:vector,y:vector)->vector:
    #checking that both vector should be of equal length
    assert len(x)==len(y)
    return [x+y for x,y in zip(x,y)]


def subtraction(x:vector,y:vector)->vector:
    #checking that both vector should be of equal length
    assert len(x)==len(y)
    return [x-y for x,y in zip(x,y)]

def scalarMultiplication(v:vector,c:float)->vector:
    # to check there exist at least one element in the vector
    assert v
    return [x*c for x in v]

def dotProduct(x:vector,y:vector)->float:
    # to check both the vecor should be of equal length
    assert len(x)==len(y)
    res=0.0
    for a,b in zip(x,y):res=res+(a*b)
    return res

def lengthOfVecotr(x:vector,y:vector)->float:
    res=0.0
    for a,b in zip(x,y):
        res=res+((b-a)**2)
    res=math.sqrt(res)
    return res
    
def main():
    while(True):
        print()
        print("--- Menu Options ---")
        print("1 for Vector Addition")
        print("2 for Vector Subtraction")
        print("3 for Scalar Multiplication")
        print("4 for Dot Product")
        print("5 for Length of Vecotor")
        print("6 to Exit")
        opt = int(input("Enter your Option : "))
        if(opt==1):
            print("Addition of Two Vector is ",addition(v1,v2))
        elif(opt==2):
            print("Subtraction of Two Vector is ",subtraction(v1,v2))
        elif(opt==3):
            print("The resultant vector after performing scalar multiplication is ",scalarMultiplication(v1,3))
        elif(opt==4):
            print("The result of Dot Product is = ",dotProduct(v1,v2))
        elif(opt==5):
            print("The length of the Vector is =",lengthOfVecotr(v1,v2))
        elif(opt==6):break
        
main()

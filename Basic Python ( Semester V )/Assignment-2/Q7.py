import math
def areaTraingle():
    side1=int(input("Enter the first side = "))
    side2=int(input("Enter the second side = "))
    side3=int(input("Enter the third side = "))
    assert((side1+side2>side3) and (side2+side3>side1) and (side3+side2>side1))
    s=(side1+side2+side3)/2
    area=float(math.sqrt((s*(s-side1)*(s-side2)*(s-side3))))
    return area

def main():
    res=areaTraingle()
    print("The area of traingle is = ",res)
main()

# Input :

# Enter the first side = 5
# Enter the second side = 12
# Enter the third side = 13

# Output :
# The area of traingle is =  30.0

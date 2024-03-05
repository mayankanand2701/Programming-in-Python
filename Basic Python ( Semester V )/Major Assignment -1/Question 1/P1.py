# Program to Convert a Binary Base Number to its Decimal Equivalent

def main():
    bnum=input("Enter the Binary Number = ")
    p=0 
    dnum=0
    for ch in bnum[::-1]:
        dnum=dnum+((2**p)*(int(ch)))
        p=p+1
    print("The Decmial Equivalent of Binary Number",bnum,"is = ",dnum)
    
main()

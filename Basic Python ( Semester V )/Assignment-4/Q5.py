import pdb
pdb.set_trace()

def findHCF(num1,num2):
    if num1<num2:
        minNum=num1
    else:
        minNum=num2
    for i in range(minNum,1,-1):
        if num1%i==0 and num2%i==0:
            HCG=i
    return HCF

def main():
    num1=int(input("Enter the first number : "))
    num2=int(input("Enter the second number : "))
    print(findHCF(num1,num2))

if __name__=="__main__":
    main()

# The issue in the given code is due to the incorrect variable name used for the "Highest Common Factor" (HCF).
# The variable HCG is used instead of HCF, causing the function to return an undefined variable.
# The code will be coreect if you follow the below three steps :
#   - Renamed HCG to HCF inside the findHCF() function.
#   - Added a break statement inside the loop to exit once the HCF is found.
#   - Added an else block to set HCF to 1 if no common factor other than 1 is found.
# n is uded for next line in pdb
# s is used to inside any function in pdb

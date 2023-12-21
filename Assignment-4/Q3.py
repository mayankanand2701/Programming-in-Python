import pdb
pdb.set_trace()

def main():
    totalMarks=0
    i=0
    while True:
        marks=input("Enter marks for subject "+str(i+1)+":")
        if marks=="": break
        marks=int(marks)
        if marks<0 or marks >100:
            print("Invalid marks")
            continue
        i+=1
        totalMarks+= marks
    percentage=totalMarks//i
    print("Total marks",int(totalMarks))
    print("Percentage ",round(percentage,2))
if __name__=="__main__":
    main()

# there is no syntax error in the above code
# but there exist the logical error
# in order to print the accurate %age value we need to use / operator instead or //
# / operator gives the result in float or decimal points
# // opeator gives the result in integer
# Thus we need to make change in only line 13
# percentage=totalMarks/i
# n is used to change the next line in pdb
# s is used to enter inside any function

        

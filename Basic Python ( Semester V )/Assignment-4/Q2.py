import pdb
pdb.set_trace()

def invertedRightTriangle(nRows):
    for i in range(nRows,0):
        print("*"*i)
def main():
    nRows=int(input("Enter the number of rows = "))
    invertedRightTriangle(nRows)
if __name__=="__main__":
    main()

# there is no syntax error in the above code
# logical error exit
# the prototype of function range is range(start, stop, step)
# in order to print the inverted right traingle we nee decrease the value of step by 1 each time
# but in the above code there is no step provided so we are not getting the correct ouput
# replacing range(nRows,0,-1) gives the correct output
# n for next line
# s to go inside the function



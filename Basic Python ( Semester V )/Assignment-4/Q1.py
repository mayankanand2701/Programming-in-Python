import pdb
pdb.set_trace()

def summation(n):
    total=0
    for count in range(1,n):
        total+=count
        print(total)
    return total
def main():
    n=int(input("Enter the number of terms: "))
    total=summation(n)
    print(total)
    print("Sum of first ",n,"positive integers : ",total)
if __name__=="__main__":
    main()

# In the above code there is no syntax error
# But the logical error exist in line 5 the range should be (1,n+1)
# n for next line
# s to go inside the function

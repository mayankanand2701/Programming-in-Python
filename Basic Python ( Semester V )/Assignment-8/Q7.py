def printSubSet(list):
    if len(list)==1: print(list[0])
    else : return printSubSet(len(list)-1)
           
list=eval(input("Enter the list = "))
print(list)
printSubSet(list)    

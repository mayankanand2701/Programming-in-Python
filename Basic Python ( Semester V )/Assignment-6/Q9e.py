str=input("Enter the String = ")
idx=int(input("Enter the index = "))
res=""
if(idx>len(str)): print("Invalid Index !")
else :
    for x in range(0,len(str)):
        if(x!=idx):res=res+str[x]

print("The Resultant String is : ",res)
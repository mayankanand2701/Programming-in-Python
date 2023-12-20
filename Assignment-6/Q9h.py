str=input("Enter the String = ")
acount=0
dcount=0
for ch in str:
    if(ch.isdigit()):dcount=dcount+1
    elif(ch.isalpha()):acount=acount+1
if (dcount>=1 and acount>=1): print("The String consist of at least one digit and one alphbet ")
else: print("The String do not consist of at least one digit and one alphabet")
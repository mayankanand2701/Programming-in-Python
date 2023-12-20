str=input("Enter the String = ")
ch=input("Enter the Character whose frequncy you want to count = ")
count=0
for c in str:
    if(c==ch):count=count+1

print("The Frequency of the Character is  : ",count)
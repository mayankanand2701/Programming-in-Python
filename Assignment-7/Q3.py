string=input("Enter the string = ")
dict={}
for ch in string:
    count=0
    for c in string:
        if(ch==c):count=count+1
    if ch.isalpha()==True: dict[ch]=count
print("The Frequency dictionary so formed is  = ")
print(dict)
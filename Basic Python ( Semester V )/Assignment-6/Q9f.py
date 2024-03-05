str=input("Enter the String = ")
str=str.lower()
vcount=0
ccount=0
list=['a','e','i','o','u']
for i in range(0,len(str)):
    if(str[i] in list):vcount=vcount+1
    else : ccount=ccount+1

print("The number of vowels in the string is = ",vcount)
print("The number of consonants in the string is = ",ccount)
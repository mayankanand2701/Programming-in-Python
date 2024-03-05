# Program to count the number of Lowecase,Uppercase,Digit and Special Symbol form the input string

str=input("Enter the string = ")
import re

x=re.findall("[a-z]",str)
print("The number of Lowercase Letters in string : ",len(x))

x=re.findall("[A-Z]",str)
print("The number of Uppercase Letters in string : ",len(x))

x=re.findall("[0-9]",str)
print("The number of Digits in string : ",len(x))

#special="~`!@#$%^&*()_-+=[]{}\|:;'?/., "
#x=re.findall(special,str)
#print("The number of Special Case Letters are : ",len(x))


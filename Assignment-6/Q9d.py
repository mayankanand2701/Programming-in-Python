str=input("Enter the String = ")
ans=""
for ch in str[::-1]:ans=ans+ch
if(str==ans):print("Palindrome String")
else :print("Not a Palidrome String")

str=input("Enter the String = ")
list=str.split(" ")
ans=""
for ch in list[::-1]:ans=ans+ch+" "
print("The Reversed String without reversing words  is : ",ans.strip())
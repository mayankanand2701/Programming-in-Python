num1=int(input("Enter the first number = "))
num2=int(input("Enter the second number = "))
num3=int(input("Enter the third number = "))

maximum=max(num1,num2,num3)
minimum=min(num1,num2,num3)
mid=((num1+num2+num3)-(maximum+minimum))
print("The number in sorted form is : ",minimum," ",mid," ",maximum)

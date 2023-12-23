num=int(input("Enter the four digit number = "))
dig1=num//1000
dig2=num//100%10
dig3=num//10%10
dig4=num%10

sum=dig1+dig2+dig3+dig4
print(dig1," + ",dig2," + ",dig3," + ",dig4," = ",sum)

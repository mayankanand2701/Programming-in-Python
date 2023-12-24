def sum(a):
    sum=0
    while(a>0):
        dig=a%10
        sum=sum+dig
        a=a//10
    return sum

a=int(input("Enter the number = "))
s=sum(a)
print("The sum of digits of the number is = ",s)
sum=0
count=0
num=int(input("Enter the number = "))
if(num==0):print("Invalid Input! The first number cannot be 0.")
else:
    sum=sum+num
    count=1
    while(True):
        n=int(input("Enter the new number = "))
        if(n==0):break
        sum=sum+n
        count=count+1
    print("The average of all the number taken as input is : ",(sum//count))


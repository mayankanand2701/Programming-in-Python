def sumOfEvenDigits(num):
    sum=0
    dig1=num//1000
    dig2=num//100%10
    dig3=num//10%10
    dig4=num%10
    if dig1%2==0: sum=sum+dig1
    if dig2%2==0: sum=sum+dig2
    if dig3%2==0: sum=sum+dig3
    if dig4%2==0: sum=sum+dig4
    return sum
def main():
    num=int(input("Enter the number = "))
    res=sumOfEvenDigits(num)
    print("The sum of even digits is = ",res)
main()


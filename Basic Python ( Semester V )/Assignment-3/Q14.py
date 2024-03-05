def rev(a):
    nnum=0
    num=a
    while(num>0):
        dig=num%10
        nnum=nnum*10+dig
        num=num//10
    if(nnum==a):return True
    else: return False

a=int(input("Enter the  number = "))
res=rev(a)
if(res):print("Palindrome Number ")
else :print("Not a Palindrome Number")
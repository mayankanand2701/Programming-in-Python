def armstrong(n):
    nn=n
    sum=0
    while(n>0):
        dig=n%10
        sum=sum+(dig**3)
        n=n//10
    if(sum==nn):return True
    else: return False

def main():
    for i in range(1,1001,1):
        res=armstrong(i)
        if(res): print(i)

print("All the armstrong number in the range of 1 to 1000 is : ")
main()
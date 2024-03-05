str=input("Enter the String = ")
n=len(str)
mid=0
if n%2==0: mid=n//2
else: mid=mid//2+1

start=0
end=mid
flag=0
while(start<mid and end<mid):
     if(str[start]==str[end]):
            start= start+1
            end= end+1
     else:
            flag=1
            break
        
if flag==0:print("Symmetric")
else:print("Asymmetric")


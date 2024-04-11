def median(list):
    list=sorted(list)
    n=len(list)
    res=0
    if(n%2==1):res=list[n//2]
    else:
        mid1=n//2
        mid2=mid1-1
        res=(list[mid1]+list[mid2])/2
    return res

list=[1,2,3,4,5,6]
print("The Median is : ",median(list))
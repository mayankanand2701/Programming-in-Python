from collections import defaultdict
d=defaultdict(dict)
n=int(input("Enter the number of entry you want = "))
for i in range(0,n,1):
    name=input("Enter the name : ")
    sec=input("Enter the section : ")
    secn=int(input("Enter the section number : "))
    d.update({name:{sec:secn}})
print(d)
print(d['Aman'])

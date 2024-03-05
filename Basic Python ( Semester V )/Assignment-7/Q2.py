l=list(eval(input("Enter the original list = ")))
nl=[]
for i in range (len(l)):
    sum=0
    for j in range(0,i+1):sum=sum+l[j]
    nl.append(sum)
print("The Resultant list is  : ")
print(nl)

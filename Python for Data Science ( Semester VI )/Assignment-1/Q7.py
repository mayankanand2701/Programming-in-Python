import matplotlib.pyplot as plt
string=input("Enter the string : ")
string=string.lower()
key=[]
value=[]
for c in string:
    count=0
    for v in string:
        if(c==v):
            count=count+1
    if(key.count(c)>=1 or c==' '):continue
    key.append(c)
    value.append(count)
plt.bar(key,value)
plt.xlabel(" Character  ")
plt.ylabel(" Frequency ")
plt.show()

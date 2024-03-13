salaries_and_tenures=[
    (83000,8.7),(88000,8.1),(48000,0.7),(76000,6),(69000,6.5),(76000,7.5),(60000,2.5),(83000,10),(48000,1.9),(63000,4.2)
]
from collections import defaultdict
d1=defaultdict(list)
for x,y in salaries_and_tenures:
    if (y<2):d1["less then 2"].append(x)
    elif (y>=2 and y<=5):d1["between 2 and 5"].append(x)
    elif(y>5):d1["more than 5"].append(x)
        
d2=defaultdict(list)
for  x in d1:
    sum=0
    for y in d1[x]:sum=sum+y
    d2[x]=sum/(len(d1[x]))
    
condition=""
if(d2["less then 2"]>d2["between 2 and 5"] and d2["between 2 and 5"]<d2["more than 5"]):
    condition = "Users with very few and very many years of experience tend to pay."
else:
    condition = "Users with average amounts of experience don’t."

# Print the condition
print("Condition :")
print(condition)
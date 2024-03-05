#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 14:13:40 2024

@author: student
"""

users=[
       {"id":0,"name":"Ashok"},
       {"id":1,"name":"Rahul"},
       {"id":2,"name":"Sarita"},
       {"id":3,"name":"Rohan"},
       {"id":4,"name":"Akhaya"},
       {"id":5,"name":"Prakash"},
       {"id":6,"name":"Madhabi"},
       {"id":7,"name":"Spandan"}
]

interests=[(0,'python'),(0,'java'),(1,'java'),(2,'python'),(2,'java'),(3,'python'),(4,'c'),(5,'c'),(6,'python'),(7,'java')]

# Question 1
from collections import defaultdict
d=defaultdict(list)
for i,j in interests:
    d[j].append(i)
    
#print("The list of user id by interest is : ",d)
print("The list of user id by interest is : ")
for i in d:print(i," :",d[i])

print()

# Question 2
from collections import defaultdict
d1=defaultdict(list)
for i,j in interests:
    d1[i].append(j)
#print("The list of interest by user id : ",d1)
print("The list of interest by user id : ")
for i in d1:print(i," :",d1[i])

# Question 3
list=[]
index=int(input("Enter the id = "))
for s in d1[index]:
    print(s)
    for j in d[s]:
        print(j)
        if j==index:continue
        else:list.append(j)
        
from collections import Counter
print(Counter(list))

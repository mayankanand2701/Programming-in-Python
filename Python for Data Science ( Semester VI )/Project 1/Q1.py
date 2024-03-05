#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 15:24:25 2024

@author: student
"""
users=[
       {"id":0,"name":"Hero"},
       {"id":1,"name":"Dunn"},
       {"id":2,"name":"Sue"},
       {"id":3,"name":"Chi"},
       {"id":4,"name":"Thor"},
       {"id":5,"name":"Clive"},
       {"id":6,"name":"Hicks"},
       {"id":7,"name":"Devin"},
       {"id":8,"name":"Kate"},
       {"id":9,"name":"Klein"}
]
friendship_pairs=[(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),(4,5),(5,6),(5,7),(6,8),(7,8),(8,9)]

# Question 2

from collections import defaultdict
d=defaultdict(list)
for i,j in friendship_pairs: 
    d[i].append(j)
    d[j].append(i)
print(d)

count=0
nonode=len(d)
#print(nonode)

for i in d:
    count=count+len(d[i])

#print(count)
#print("The total number of connections = ",nonode)
#print("The total average connections = ",(count/nonode))

# Question 3
d2=dict(sorted(d.items(),key=lambda x:x[1]))
for i in d2:
    print(i," :",d2[i])
    
# Question 4
index=int(input("Enter the index for which you want to calculate the friendship : "))
rlist=[]
for i in d[index]:
   for j in d[i]:
       rlist.append(j)
#print("Friends of Friends : ",set(rlist))



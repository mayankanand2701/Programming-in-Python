#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 15:35:02 2024

@author: student
"""
salaries_and_tenures=[
    (83000,8),(88000,8),(48000,1),(76000,6),(69000,6),(76000,7),(60000,2),(83000,10),
    (48000,2),(63000,4),(52000,1),(85000,8),(71000,5),(80000,7)
    ]

# Question 1

from collections import defaultdict
d=defaultdict(list)
avg=defaultdict(list)
for x,y in salaries_and_tenures:
    d[y].append(x)
for x in d:
    sum=0
    for i in d[x]:sum=sum+i
    avg[x]=sum/len(d[x])
#for x in avg:print(x," : ",avg[x])

# Question 2

d1=defaultdict(list)
for x,y in salaries_and_tenures:
    if (y<2):d1["less then 2"].append(x)
    elif (y>=2 and y<=5):d1["between 2 and 5"].append(x)
    elif(y>5):d1["more than 5"].append(x)
#for x in d1:print(x," : ",d1[x])

# Question 3
d2=defaultdict(list)
for  x in d1:
    sum=0
    for y in d1[x]:sum=sum+y
    d2[x]=sum/(len(d1[x]))
for x in d2:print(x,": the averages salary is : ",d2[x])
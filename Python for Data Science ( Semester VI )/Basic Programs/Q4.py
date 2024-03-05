#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 14:45:00 2024

@author: student
"""
from collections import Counter
s='BACDA'
c=Counter(s)
print(c)

# it gives output in decreasing order 
# Output : Counter({'A': 2, 'B': 1, 'C': 1, 'D': 1})

list=[]
for x,y in c.most_common(3):
    list.append((x,y))
    # print(x,y)
print(list)
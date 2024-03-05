#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 15:01:41 2024

@author: student
"""

x=[1,2,1,3,2,4]

# sorted(x) return after sorting it does not make changes in original 
y=sorted(x)
print(y)
print(x)

# x.sort() it makes the changes inside x
x.sort()
print(x)

a=[-1,-3,2,4]
b=sorted(a,key=abs,reverse=True)
print(b)
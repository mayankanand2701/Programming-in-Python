#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 15:15:10 2024

@author: student
"""

# to sort the array according to its values
d={'A':1,'B':0,'C':4,'D':5}

d1=d.items()
print(d1)
# Output : dict_items([('A', 1), ('B', 0), ('C', 4), ('D', 5)])

# will sort the dictionay according to values
d2=sorted(d1,key=lambda x:x[1])
print(d2)   
#  Output : [('B', 0), ('A', 1), ('C', 4), ('D', 5)]

# to convert it into dictionary foramt
print(dict(d2))
# Output : {'B': 0, 'A': 1, 'C': 4, 'D': 5}
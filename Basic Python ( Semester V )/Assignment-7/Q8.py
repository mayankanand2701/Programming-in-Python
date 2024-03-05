address='B-6, Lodhi road, Delhi'
list1=[1,2,3]
list2=['a',1,'z',26,'d',4]
tuple1=('a','e','i','o','u')
tuple2=([2,4,6,8],[3,6,9],[4,8],5)
dict1 = {'apple': 'red','mango':'yellow','orange':'orange'}
dict2 = {'X':['eng','hindi','maths','science'],'XII':['english','physics','chemistry','maths']}

# 1
list1[3] = 4
# Output : Error: list assignment index out of range

# 2
#print(list1*2)
# Output : [1, 2, 3, 1, 2, 3]

# 3
#print(min(list2))
# Output : Error: '<' not supported between instances of 'int' and 'str'

# 4
#print(max(list1))
# Output : 3

# 5
#print(list(address))
# Output : ['B', '-', '6', ',', ' ', 'L', 'o', 'd', 'h', 'i', ' ', 'r', 'o', 'a', 'd', ',', ' ', 'D', 'e', 'l', 'h', 'i']

# 6
#list2.extend(['e', 5])
#print(list2)
# Output : ['a', 1, 'z', 26, 'd', 4, 'e', 5]

# 7
#list2.append(['e', 5])
#print(list2)
# Output : ['a', 1, 'z', 26, 'd', 4, ['e', 5]]

#8
#names = ['rohan','mohan','gita']
#names.sort(key= len)
#print(names)
# Output : ['gita', 'rohan', 'mohan']

#9
#list3 = [(x * 2) for x in range(1, 11)]
#print(list3)
# Output : [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#10
#del list3[1:]
#print(list3)
# Output : [2]

#11
#list4 = [ x+y for x in range(1,5) for y in range(1,5)]
#print(list4)
# Output : [2, 3, 4, 5, 3, 4, 5, 6, 4, 5, 6, 7, 5, 6, 7, 8]

# 12
#tuple2[3] = 6
# Output : Error:'tuple' object does not support item assignment

# 13
#tuple2.append(5)
# Output : : 'tuple' object has no attribute 'append'

# 14
#t1 = tuple2 +(5)
# Output : Error: can only concatenate tuple (not "int") to tuple

# 15
#print(','.join(tuple1))
# Output : a,e,i,o,u

# 16
#print(list(zip(['apple','orange'],('red','orange'))))
# Output : [('apple', 'red'), ('orange', 'orange')]

# 17
#print(dict2['XII'])
# Output : ['english', 'physics', 'chemistry', 'maths']

# 18
#print(dict2['XII'].append('computer science'),dict2)
# Output : None {'X': ['eng', 'hindi', 'maths', 'science'], 'XII': ['english', 'physics', 'chemistry', 'maths', 'computer science']}

# 19
#print('red' in dict1)
# Output : False

# 20
#print(list(dict1.items()))
# Output : [('apple', 'red'), ('mango', 'yellow'), ('orange', 'orange')]

# 21
#print(list(dict2.keys()))
# Output : ['X', 'XII']

#22
#print(dict2.get('XI','None'))
# Output : None

#23
#dict1.update({'kiwi':'green'})
#print(dict1)
# Output :  {'apple': 'red', 'mango': 'yellow', 'orange': 'orange', 'kiwi': 'green'}


from collections import defaultdict
d=defaultdict(list)
# for int the default value is 0
# for float by default value is 0.0
# for list by default value is []
# same goes for tuple,dict
s="ABCDA"
for i in s:
    # d[i]+=1
    d[i].append(1)
print(d)
# print(dict(d))
# print(d['E'])

# Output for int : defaultdict(<class 'int'>, {'A': 2, 'B': 1, 'C': 1, 'D': 1})
# Output for list : defaultdict(<class 'list'>, {'A': [1, 1], 'B': [1], 'C': [1], 'D': [1]})

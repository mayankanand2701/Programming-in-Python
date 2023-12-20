import re
string3="cdccdcddd343344aabb"

match1=re.search('(c|d)*\d*(a|b)*',string3)
print(match1.group())

match2=re.search('(cd)*d',string3)
print(match2.group())

match3=re.search("(cc|cd)*(3|4)*(aa|bb)",string3)
print(match3.group())

match4=re.search("(cc|cd|dd)*(3|4)*(aa|bb)",string3)
print(match4.group())

match5=re.search('(cc|cdc|dd)*(3|4)*(aa|bb)*',string3)
print(match5.group())

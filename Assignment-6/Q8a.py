import re
string1="Python Programming Language"

match1=re.search('......m?',string1)
print(match1.group())

match2=re.search('......m{1,2}',string1)
print(match2.group())

match3=re.search(".*Language$",string1)
print(match3.group())

match4=re.search("\w*\s\w*",string1)
print(match4.group())

match5=re.search('.*',string1)
print(match5.group())

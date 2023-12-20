import re
string2="Car Number DL5645"

match1=re.search('\w\w?\d{1,4}',string2)
print(match1.group())

match2=re.search('.*5',string2)
print(match2.group())

match3=re.search(".*5?",string2)
print(match3.group())

match4=re.search("\d{3}",string2)
print(match4.group())

match5=re.search('^C.*5$',string2)
print(match5.group())

l=list(input("Enter the original list = "))
nl=[]
for i in l:
    if nl.__contains__(i):continue
    elif i.isalnum(): nl.append(i)
print("The Resultant list after removing duplicate is = ")
print(nl)

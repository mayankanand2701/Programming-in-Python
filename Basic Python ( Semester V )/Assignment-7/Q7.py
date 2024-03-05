dict={1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",0:"Zero"}
num=input("Enter the number = ")
res=""
for i in num:
    dig=int(i)
    res=res+dict[dig]+" "
print("The resultant string formed is : "+res.strip())
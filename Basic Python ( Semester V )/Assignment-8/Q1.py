str=input("Enter the String = ")
res=0
def convert(str,res):
    if str=="": return res
    else :
        res=res*10+int(str[0])
        return convert(str[1:],res)
print("The input string in integer format is = ",convert(str,res))

        

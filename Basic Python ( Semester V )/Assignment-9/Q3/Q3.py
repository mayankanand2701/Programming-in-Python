def convertToCapital():
    file=open("file.txt","w")
    print("Enter nothing to stop inputing the sentence : ")
    str=""
    while(True):
        str=input("Enter the sentence : ")
        if str=='':break
        str=str+"\n"
        str=str.upper()
        file.write(str)
    file.close()
convertToCapital()
    

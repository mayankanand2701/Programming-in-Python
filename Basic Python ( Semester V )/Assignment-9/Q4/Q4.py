def copyAlternateLines():
    # to input the lines for the text file
    file=open("file.txt","w")
    print("Enter nothing to stop inputing the sentence : ")
    str=""
    while(True):
        str=input("Enter the sentence : ")
        if str=='':break
        str=str+"\n"
        file.write(str)
    file.close()

    try:
        file1=open("file.txt","r")
        file2=open("file1.txt","w")
        flag=0
        for line in file1:
            if(flag==0):
                file2.write(line)
                flag=1
            else:flag=0
        file1.close()
        file2.close()
    except FileNotFoundError: print("Error: File not found.")
    except IOError: print("Error: Input Error")
    except Exception:print("Error : Unexpected Error Occured")
    
copyAlternateLines()      
        
    
    

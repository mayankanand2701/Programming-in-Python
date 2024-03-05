def copy():
    # Code to input the content of first File
    file1=open("file1.txt","w")
    print("Enter Q to stop inputing the sentence : ")
    str=""
    while(True):
        str=input("Enter the sentence : ")
        if str=='':break
        str=str+"\n"
        file1.write(str)
    file1.close()
    file1=open("file1.txt","r")
    print(file1.read())
    
    # Code to read the content of this fiel1 to new file2
    file1=open("file1.txt","r")
    file2=open("file2.txt","w")
    for line in file1:
        file2.write(line)
    file2.close()
    file1.close()

    # Code to print the content of file2 after copying from file 1
    print("The content after copying are's : ")
    file2=open("file2.txt","r")
    #for line in file2.readline():print(line)
    print(file2.read())
    file2.close()
    
copy()


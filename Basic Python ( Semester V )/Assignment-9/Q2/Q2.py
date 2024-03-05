def count():
    # Code to input the content of first File
    file=open("file.txt","w")
    print("Enter nothing to stop inputing the sentence : ")
    str=""
    while(True):
        str=input("Enter the sentence : ")
        if str=='':break
        str=str+"\n"
        file.write(str)
    file.close()

    # to count the number of words and number of vowels
    wcount=0
    vcount=0
    file=open("file.txt","r")
    for line in file:
        line=line+" "
        for c in line:
            if c=='a'or c=='e' or c=='i'or c=='o' or c=='u' or c=='A' or c=='E' or c=='I'or c=='O' or c=='U':vcount=vcount+1
            elif c==' ':wcount=wcount+1

    file.close()
    print("The number of words in  the file is = ",wcount)
    print("The number of vowels in the file is = ",vcount)
    
count()

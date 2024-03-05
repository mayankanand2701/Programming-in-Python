def read():
    file=open("Poem.txt","r")
    abtcount=0
    bscount=0
    lcase=0
    ucase=0
    wswvcount=0
    ocount=0
    for line in file:
        for c in line:
            if c.isalpha():
                abtcount=abtcount+1
                if c.islower():lcase=lcase+1
                elif c.isupper():ucase=ucase+1
            elif c==' ':bscount=bscount+1
        ocount=ocount+line.count('beautiful')
        line=line.strip()
        list=line.split(" ")
        if list==['']:
            pass
        else:
            for word in list:
                if word[0]=='a' or word[0]=='e' or word[0]=='i' or word[0]=='o' or word[0]=='u' or word[0]=='A' or word[0]=='E' or word[0]=='I' or word[0]=='O' or word[0]=='U':wswvcount=wswvcount+1    
        
    print("Number of Alpbabet in File : ",abtcount)
    print("Number of Lowercasse in File : ",lcase)
    print("Number of Uppercase in File: ",ucase)
    print("Number of Blankspace in File: ",bscount)
    print("Number of times the word beautiful ocuured in file is : ",ocount)
    print("Number of words staring with Vowel in File is : ",wswvcount)

read()   

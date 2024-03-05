def calculatePricePerUnitWeight():
    # to input the respecitve weights and price of the items
    file1=open("file.txt","w")
    file2=open("file1.txt","w")
    print("Enter the Weights of the  respectives items = ")
    while(True):
        w=input("Enter the weight's : ")
        if (w==''):break
        file1.write(w+"\n")
    file1.close()

    print("Enter the Price of the respective items = ")
    while(True):
        p=input("Enter the Prices's : ")
        if (p==''):break
        file2.write(p+"\n")
    file2.close()

    # to create a resultant file that will hold price per unit weight for each item
    file1=open("file.txt","r")
    file2=open("file1.txt","r")
    file3=open("file2.txt","w")
    for a, b in zip(file1, file2):
        try:
            weight = float(a.strip())
            price = float(b.strip())
            if weight != 0:  # Avoid division by zero
                res = price / weight
                file3.write(str(res) + "\n")
            else: file3.write("Invalid\n")
        except ValueError: file3.write("Invalid\n")
        # more error can be handled here
    file3.close()
    file2.close()
    file1.close()
        
calculatePricePerUnitWeight()

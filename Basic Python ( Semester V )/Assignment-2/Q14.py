def uppercase(c):
    assert 'a' <= c <= 'z', "Invalid input! Please enter a lowercase alphabet."
    l=ord(c)-32
    print("The equivalent uppercase for character is :",chr(l))
    
c=input("Enter the charcter = ")
uppercase(c)

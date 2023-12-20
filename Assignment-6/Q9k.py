str=input("Enter the string = ")
freq={}
for char in str:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
char = max(freq, key=freq.get)

print ("The maximum occuring characters is : "+char)

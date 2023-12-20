globalVar=10
def test():
    localVar=20
    print("Inside function test : globalVar = ",globalVar)
    print("Inside function test : localVar = ",localVar)
test()
print("Outside function test : globalVar = ",globalVar)
print("Outside function test : localVar = ",localVar)
globalVar=10
def test():
    localVar=20
    globalVar=30
    print("Inside function test : globalVar = ",globalVar)
    print("Inside function test : localVar = ",localVar)
test()
print("Outside function test : globalVar = ",globalVar)
# Program  to perform any Base Conversion

def convertToAnyBase(num,ibase,obase):
    if not (2<=ibase<=16 and 2<=obase<=16):
        print("Invalid Base Input : The Base should be between 2 and 16 ")
        #return "Base must be between 2 and 16 "
        exit()
    dec = int(num, ibase)
    dig = "0123456789ABCDEF"
    if dec == 0:
        return "0"
    output = ""
    while dec > 0:
        digit = dec % obase
        output = dig[digit] + output
        dec //= obase
    return output

def main():
    number = input("Enter a number: ")
    ibase = int(input("Enter the Base of the Input number = "))
    obase = int(input("Enter the Base in which you want the Output = "))
    result = convertToAnyBase(number,ibase,obase)
    print("The Input Number ",number," is in base ",ibase," and is Equivalent Conversion in Base",obase," is " ,result)

main()

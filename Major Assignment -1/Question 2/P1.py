def int2hex(num):
    table={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    if num not in table:
        print("Invalid Input : Input number should be between 0 to 15")
        exit()
    return table[num]

def hex2int(chr):
    table={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    chr=chr.upper()
    if chr not in table:
        print("Invalid Input : Invalid Hexadecimal Digit.")
        exit()
    return table[chr]

def main():
    hval=input("Enter the Hexadecimal Digit = ")
    dval=hex2int(hval)
    print("The Decimal Equivalent of ",hval,"is : ",dval)

    dval=int(input("Enter the Decimal Digit = "))
    hval=int2hex(dval)
    print("The Hexadecimal Equivalent of ",dval," is : ",hval)

main()

    

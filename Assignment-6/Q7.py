def main():
    greeting="Good Morning.Have a Good Day!!"
    print("1 : ",greeting.count('Good'))
    print("2 : ",greeting.find('a'))
    print("3 : ",greeting.rfind('a'))
    print("4 : ",greeting.capitalize())
    print("5 : ",greeting.lower())
    print("6 : ",greeting.upper())
    print("7 : ",greeting.swapcase())
    print("8 : ",greeting.istitle())
    print("9 : ",greeting.replace('Good','Sweet'))
    print("10 : ",greeting.strip())
    print("11 : ",greeting.split())
    print("12 : ",greeting.partition('.'))
    print("13 : ",greeting.startswith('good'))
    print("14 : ",greeting.endswith("!!"))

main()
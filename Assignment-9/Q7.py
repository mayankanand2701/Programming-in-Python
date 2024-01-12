def inverse1():
    try:
        num = input("Enter the number: ")
        num = float(num)
        inverse = 1.0 / num
    except ValueError: print("ValueError")
    except TypeError: print("TypeError")
    except ZeroDivisionError: print("ZeroDivisionError")
    except: print("Any other Error")
    else: print(inverse)
    finally: print("Function inverse completed")
inverse1()

# a
# Input : 5
# Output : 0.2
#          Function inverse completed
    
# b
# Input : 0
# Output : ZeroDivisionError
#          Function inverse completed

# c
# Input : 2.0
# Output : ZeroDivisionError
#          Function inverse completed

# d
# Input : x
# Output : ValueError
#          Function inverse completed

# e
# Input : None
# Output : ValueError
#          Function inverse completed

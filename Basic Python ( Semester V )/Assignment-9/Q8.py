def percentage(marks, total):
    try:
        percent = (marks / total) * 100
    except ValueError: print("ValueError")
    except TypeError: print("TypeError")
    except ZeroDivisionError: print("ZeroDivisionError")
    except: print("Any other Error")
    else:print(percent)
    finally:print("Function percentage completed")

# a
# percentage(150.0,200.0)
# Output : 75.0
#          Function percentage completed

# b
# percentage(150.0, 0.0)
# Output : ZeroDivisionError
#          Function percentage completed

# c
# percentage('150.0', '200.0')
# Output : TypeError
#          Function percentage completed

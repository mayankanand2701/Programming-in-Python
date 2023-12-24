mname=input("Enter the Month name = ")
mname=mname.lower
if mname=="january" or mname=="march" or mname=="may" or mname=="july" or mname=="august" or mname=="october" or mname=="december":print("31 Days")
elif mname=="april" or mname=="june" or mname=="september" or mname=="november":print("30 days")
else: print("28 or 29 days")
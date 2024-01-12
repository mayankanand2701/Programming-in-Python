# a

try:
    f = open("file1.txt","r")
except IOError: print("Problem with Input Output...\n")
else: print("No Problem with Input Output...")

# Output : Problem with Input Output...

# b
# try:
#     f = open("file1.txt","w")
# except IOError: print("Problem with Input Output...\n")
# else: print("No Problem with Input Output...\n")

# Output : No Problem with Input Output...

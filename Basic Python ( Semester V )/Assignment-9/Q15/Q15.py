f = open("PYTHON", "w")
description =["we either choose the pain of discipline \n", "or\n" "the pain of regret\n"]
f.writelines(description)
f.close()
f = open("PYTHON","r")
print(f.read())
f.close()

# Output :
# we either choose the pain of discipline 
# or
# the pain of regret

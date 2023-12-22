# a
def say (message, times=2):
    print(message*times)
say ('Hello')
say('World',5)

# Output : HelloHello
#          WorldWorldWorldWorldWorld


# b
def fun(a=2,b=3,c=7):
    d= a+b+c
    print(d)
print(fun (2))
# output : 12
#          None

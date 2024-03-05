# Program to generate Random Password between length of 7 to 10
import random

def generateRandomPassword():
    plen=random.randint(7,10)
    password=''.join(chr(random.randint(33,126)) for _ in range(plen))
    return password

def main():
    rpwd=generateRandomPassword()
    print("The Randomly Generated Password is = ",rpwd)

main()

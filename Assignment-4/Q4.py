import pdb
pdb.set_trace()

def isLeapYear(year):
    return year%400==0 or year%100==0 and year%4==0


# This logic isn't considering the correct conditions for a leap year. According to the leap year rule:
# Years divisible by 4 are leap years.
# However, if a year is divisible by 100, it is not a leap year, unless it is also divisible by 400.
# replacing the return statement with return (year%400==0) or (year%100!=0 and year%4==0) 
# solve all the problem
# n is used for next line in pdb
# s is uded to go inside any function in pdb

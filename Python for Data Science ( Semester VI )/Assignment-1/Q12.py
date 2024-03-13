def isPerfectSquare(num):
    sqrtNum = int(num ** 0.5)
    return sqrtNum * sqrtNum == num

def sumOfDigits(num):
    return sum(int(digit) for digit in str(num))

def findNumbersInRange(start, end):
    result = []
    for num in range(start, end + 1):
        if isPerfectSquare(num) and sumOfDigits(num) < 10:
            result.append(num)
    return result

start = int(input("Enter the start of the range : "))
end = int(input("Enter the end of the range : "))

numbers = findNumbersInRange(start, end)
if numbers:
    print("Numbers in the range with sum of digits less than 10 and are perfect squares : ")
    print(numbers)
else:
    print("No numbers found in the range with sum of digits less than 10 and are perfect squares.")

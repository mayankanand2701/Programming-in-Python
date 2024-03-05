def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_factors(n):
    factors = []
    divisor = 2

    while n >= 2:
        if n % divisor == 0 and is_prime(divisor):
            factors.append(divisor)
            n /= divisor
        else:
            divisor += 1

    return factors

def main():
    num = int(input("Enter an integer (2 or greater): "))

    if num < 2:
        print("Please enter an integer greater than or equal to 2.")
    else:
        print(f"The prime factors of {num} are:")
        factors = prime_factors(num)
        for factor in factors:
            print(factor)

if __name__ == "__main__":
    main()

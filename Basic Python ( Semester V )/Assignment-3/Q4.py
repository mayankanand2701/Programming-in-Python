import random

red_numbers =[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
black_numbers =[num for num in range(1, 37) if num not in red_numbers]
special_numbers =[0,00]

# Simulate a spin of the roulette wheel
spin_result= random.choice(red_numbers+black_numbers+special_numbers)

# Display the selected number
print("The spin resulted in ",spin_result,"...")

if spin_result in special_numbers:
    print(f"Pay {spin_result}")
else:
    if spin_result in red_numbers:
        print("Pay Red")
    else:
        print("Pay Black")

    if spin_result % 2 == 0 and spin_result not in special_numbers:
        print("Pay Even")
    else:
        print("Pay Odd")

    if spin_result >= 1 and spin_result <= 18:
        print("Pay 1 to 18")
    else:
        print("Pay 19 to 36")

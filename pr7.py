#Write a Python program to check if the number provided by the user is an Armstrong number or not.

def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    total = 0
    for digit in num_str:
        total += int(digit) ** num_digits
    return total == number

number = int(input("Enter a number: "))

if is_armstrong_number(number):
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")

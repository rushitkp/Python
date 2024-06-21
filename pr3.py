#Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal

def convert_to_base(number, base):
    if number == 0:
        return '0'
    digits = '0123456789ABCDEF'
    result = ''
    while number > 0:
        remainder = number % base
        result = digits[remainder] + result
        number = number // base
    return result

decimal = int(input("Enter a decimal number: "))

binary = convert_to_base(decimal, 2)
octal = convert_to_base(decimal, 8)
hexadecimal = convert_to_base(decimal, 16)

print(f"Binary: {binary}")
print(f"Octal: {octal}")
print(f"Hexadecimal: {hexadecimal}")

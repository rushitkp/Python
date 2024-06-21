#Write a program in python to find out maximum and minimum number out of three user entered number.

def find_max_min(a, b, c):
    max_num = max(a, b, c)
    min_num = min(a, b, c)
    return max_num, min_num

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

max_num, min_num = find_max_min(num1, num2, num3)

print(f"Maximum number: {max_num}")
print(f"Minimum number: {min_num}")

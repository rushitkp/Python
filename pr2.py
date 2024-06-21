#Write a program in python to swap two variables without using temporary variable.

def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

x = 5
y = 10

print(f"Before swapping: x = {x}, y = {y}")
x, y = swap(x, y)
print(f"After swapping: x = {x}, y = {y}")

#Write a program in python to implement Factorial series up to user entered number. (Use recursiveFunction)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

number = int(input("Enter a number: "))

print("Factorial series up to", number, "is:")
for i in range(number + 1):
    print(factorial(i), end=" ")

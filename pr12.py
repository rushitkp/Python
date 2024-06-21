#Write a program in python to implement Fibonacci series up to user entered number. (Use recursiveFunction)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

number = int(input("Enter a number: "))

print("Fibonacci series up to", number, "is:")
for i in range(number):
    print(fibonacci(i), end=" ")

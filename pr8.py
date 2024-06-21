# Write a Python program to display all the prime numbers in user entered range.

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

print(f"Prime numbers between {start} and {end} are:")
for num in range(start, end + 1):
    if is_prime(num):
        print(num, end=" ")

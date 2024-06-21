# n = int(input("Enter the value of 'n': "))
# a = 0
# b = 1
# sum = 0
# count = 1
# print("Fibonacci Series: ", end = " ")
# while(count <= n):
#     print(sum, end = " ")
#     count += 1
#     a = b
#     b = sum
#     sum = a + b

def factorial(n):

  if n < 0:
    raise ValueError("Factorial is not defined for negative numbers.")
  elif n == 0:
    return 1
  else:
    return n * factorial(n - 1)

# Example usage
try:
  number = int(input("Enter a non-negative integer: "))
  result = factorial(number)
  print(f"The factorial of {number} is {result}.")
except ValueError as e:
  print(e)

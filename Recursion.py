# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#             return n*factorial(n-1)

# print(factorial(10))
# print(factorial(2*2+1-1))
# print(factorial(20))

# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(6))    
# 5*factorial(4)


# number=int(input("Enter Number:"))
# print(factorial(number))
# # def fact(n)
# fact=1
# for i in range(number):
#     fact=fact*(i+1)

def fact(n):
    if(n==0 or n==1):
        return 1  
    else:
        return n*fact(n-1)
print(fact(5))
      
        
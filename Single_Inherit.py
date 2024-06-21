# class A:
#     def showA(self):
#         print("ShowA")
# class B(A):
#     def showB(self):
#         print("ShowB")

# obj=B()
# obj.showA()        
# obj.showB()       

def fibonacci_recursive(n):
  if n <= 1:
    return n
  else:
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# def func1():
#     try:
#         l=[1,2,3,4,5]
#         i=int(input("Enter The Index:"))
#         print(l[i])
#         return 1
#     except:
#         print("Some Error Occured")
#         return 0
#     finally:
#         print("I Am Always Executed")
#     x=func1()
#     print(x)

def func1():
    try:
        l = [1, 4, 5, 67, 8, 9]
        i = int((input("Enter The Number:")))
        print(l(i))
    except:
        print("Some Error Occurred")
        return 0
    # print("I AM Also Executed")
x = func1()
print(x)

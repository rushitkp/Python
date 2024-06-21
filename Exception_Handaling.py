# a=input("Enter The Number:")
# print("Multipication Table of {a} is:")

# try:
#     for i in range(1,10):
#         print(f"{a}X{i}={int(a)*i}")
# except Exception as e:
#     print("Invalid Input")

# try:
#     num=int(input("Enter An Integer"))
#     a=[2,6]
#     print(a[num])s
# except ValueError:
#     print("Value Error")
# except IndexError:
#     print("Index Error")

# a = input("Enter The NUmber:")
# print(f"Multification table of {a} is:")
# try:
# for i in range(1, 11):
# print(int(a),"X",i,"=",int(a*i))
# print(f"{int(a)} X {i} = {int(a)*i}")
# except Exception as e:
#     print(e)

# try:
# a =(int(input("Enter Number:")))
#     for i in range(1, 11):
#         print(a,"X", i, "=", a*i)
# except Exception as e:
#     print("Error:",e)

# try:
#     num=int(input("Enter Number:"))
#     a=[6,3]
#     print(a[num])
# except ValueError:
#     print("Number Entered is Not An Interger")
# except IndexError:
#     print("Index Error")

try:
    a = (int(input("Enter First Number:")))
    b = (int(input("Enter Second Number:")))

    c = a/b
    print(c)
except Exception as e:
    print("Error:", e)
else:
    print("Done");
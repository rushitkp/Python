# marks=[1,12,10,4,23,45]
# index=0
# for mark in marks:
#     print(mark)
#     if(index==2):
#         print("Python")
#     index +=1
# for index,mark in enumerate(marks,start=4):
#     print(mark)
#     if(index == 3):
#         print("Py")

marks = [67, 55, 34, 78, 87, 56, 54, 76]
for index,marks in enumerate(marks,start=1):
    print(marks)
    if(index==3):
        print("R")
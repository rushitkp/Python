# tup=(1,2,3,4,
# 5,"Str","%#*%*%&$")
# # tup[1]=12
# print(type(tup),tup)
# print(tup[0])
# print(tup[-6])
# print(tup[2])
# print(tup[6])

# if 2 in tup:
#     print("Yes",tup[1],"is present")
# tup2=tup[1:4]
# print(tup2)    

tup=(1,34.54,343.23,232,True,"R",False)
# print(tup)
print(type(tup),tup)
print(tup[0])
print(tup[1])
print(tup[3])
print(tup[-2])
print(len(tup))

if 343.23 in tup:
    print("Yes")

tup2=tup[1:4]
print(tup2)


# a=34,54,66,788,2334,65  #tuples
a=(36,54,66,788,54,2334,65)
b=1,2,3,4,5,6
print(sum(a))
print(max(a))
print(min(a))
print(len(a))
print(any(a))
print(all(a))
print(sorted(a))


z=[2,5,6,5,7]
x=tuple(z)
print(type(x))

print(a.index(54))
print(a.index(65))
print(3 in a)
print(3 not in a)
print(a+b)
print(a==b)
print(a>b)

for x in a:
    print(x)
    
for x in range(5):
    print(a[x])


x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
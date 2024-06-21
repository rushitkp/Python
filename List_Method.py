# l=[20,22,23,23,23,33,41,44]
# print(l)
# l.append(65)
# print(l)
# l.sort()
# l.sort(reverse=True)
# l.reverse()
# print(l)

# # print(l.index(1))
# # print(l)
# print(l.count(3))
# l.insert(3,3333)
# print(l)
# m=[1,2,3,4,5]
# l.extend(m)
# k=l+m
# print(k)

l=[1,2,3,4,5]
print(l)
l.append(7)
print(l)
l.sort(reverse=True)
print(l)
print(l.index(2))
print(l.count(2))
m=l
m=l.copy()
m[0]=0
print(l)
l.insert(1,2222)
m=[900,1000,2000]
k=l+m
print(k)
l.extend(m)
print(l)

a=[23,56,10,56,80,88,35,90]
print(max(a))
print(min(a))
print(sum(a))
print(list("Rushit"))

r=[45,67,89,21,57]
r.append(100)
print(r)

r.insert(21,1)
print(r)

r.remove(21)
print(r)

r.pop(1)
print(r)

b=[2,4,6,8]
r.extend(a+b)
print(r)

r.clear()
print(r)

print(r.count(2))



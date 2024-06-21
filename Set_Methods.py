# s1={2,4,6,8,10}
# s2={5,9,1,3,23,3.3}
# print(s1.union(s2))
# print(s1,s2)
# s1.update(s2)

# city={"visnagar","Gandhinagar","Ahmadavad","Surat"}
# city2={"satlasana","Kheralu","Mahesana","visnagar"}
# city3=city.union(city2)
# print(city3)
# city3=city.intersection(city2)
# print(city3)
# city3=city.intersection_update(city2)
# print(city3)
# city3=city.symmetric_difference(city2)
# print(city3)
# city3=city.difference(city2)
# print(city3)
# print(city3.issuperset(city3))
# print(city3.issuperset(city3))
# city.discard("Surat")
# print(city)


s1={2,4,6,8}
s2={1,2,3,4,5,6,7,8,10}
print(s1.union(s1))

s1.update(s2)
print(s1,s2)
print(s1.intersection(s1,s2))

r1={"A","B","C","D"}
r2={"B","R","C","J"}
r3={"A","S","B","C","D","J",True,0,-10}
print(r1.issuperset(r1))
print(r1.issubset(r3))
r1.update(r2)
print(r1)
r3.remove("A")
print(r3)
r3.add("RR")
print(r3)

RR=r3.pop()
print(r3)
print(RR)

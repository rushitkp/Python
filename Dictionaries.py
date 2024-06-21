# dic={
#     "Rk":"Rushit Prajapati",
#     65:"rk",
#     62:"AK"
# }
# print(dic["Rk"])
# print(dic[65])
# print(dic[62])

# info={'name':'R','age':'20','eligible':True}
# print(info)
# print(info.keys())
# for key in info.keys():
#     print(info[key])
#     print("The Value {key} is {info[key]}")

#     print(info.items())

dic={
    "dict":"Dictionary",
    "mean":"meaning,means",
    63:"Rk",
    60:"ak",
    62:"Db"
}
# print(dic[63])
# print(dic[60])
# print(dic[60])

info={'name':'Rk','age':20,'eligible':True}
print(info)
print(info["name"])
print(info["eligible"])
print(info.get("age"))
print(info.keys())
print(info.values())

for key in info.keys():
    print("The Value is",info[key])

print(info.items())
for key,value in info.items():
    print({key},{value})
    
    
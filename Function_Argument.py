# def average(a=20,b=10):
#     print("The Average is",(a+b)/2)
# # average(12,13)
# average(12)
# average(b=43)
# average(a=34,b=45)

# def name(fname,mname="Rushit",lname="Prajapati"):
#     print("Hello,",fname,mname,lname)
# name("How Are You","Rk","RRR")


# def average(*numbers):
#     sum=0
#     for i in numbers:
#         sum=sum+i
#     print("Average is:",sum/len(numbers))    
# # average(23,32,33,23.43,23,3434)
#     return 2
# def name(**name):
#     print("Hello,",name["fname"],name["mname"],name["lname"])
# name(mname="RR",lname="RK",fname="Km")    

def average(a,b):
    print("The Average is",(a+b)/2)
average(12,34)    

def average(x=2,y=4):
    print("The Average is",(x+y)/2)
average(12)    
average(3445,3422)
average(2)

def name(fname,mname="K",lname="Prajapati"):
    print("Hello",fname,mname,lname)
name("Rushit")    

def r(*numbers):
    sum=0
    print(type(r),type(numbers))
    for i in numbers:
        sum=sum+i
    print("Average is:",sum/len(numbers))
r(4,6,34,5,5,6,5,)     

def name(**name):
    print(name['fname'],name['mname'],name['lname'])
name(mname="Rushit",lname="K",fname="Prajapati")   

 


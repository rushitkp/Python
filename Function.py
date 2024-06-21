def function(a,b):
    mean=(a*b)/(a+b)
    print(mean)
    
def isGreter(a,b):  
    if(a>b):
         print("First Number is Greter")
    else:
        print("Second Number is Greter Or Equal") 
a=30
b=20
isGreter(a,b)
function(a,b)
   
# gmean1=(a*b)/(a+b)
# print(gmean1)

c=34
d=44
# gmean2=(c*d)/(c+d)
# print(gmean2)
isGreter(c,d)
function(c,d)

def fn():
    print("Function")
fn()   

def my_fun(fname):
    print(fname+"R")
my_fun("Hello ")  

def my_function(fname,lname):
  print(fname,lname)
my_function("Emil", "Id")

def fun(*kid):
    print("Last Name is "+kid[1])
fun("Rushit","Prajapat")
 
def fr(food):
    for x in food:
        print(x)
fruits=["Apple","Mango","Banana","Orange"]
fr(fruits)         

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

def recursion(k):
  if(k > 0):
    result = k + recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\nRecursion Example Results")
recursion(5)
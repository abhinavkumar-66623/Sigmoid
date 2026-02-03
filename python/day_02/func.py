 
def f1():
    print("Python as a functional programming language")
    print("Python as a functional programming language")
    print("Python as a functional programming language")
    print("Python as a functional programming language")
    print("Python as a functional programming language")

# f1()
     

def greet():
    print("Hello!")

# greet()

def mul(num1,num2):
    return num1*num2
# print(mul(1,9))


def sqr(n1):
    return n1*n1

# print(sqr(4))

def calc(num1,num2):
    add=num1+num2
    sub=num1-num2
    mul=num1*num2
    div=num1/num2

    return add,sub,mul,div


a,b,c,d=calc(15,2)
print(a)
print(b)
print(c)
print(d)
print(type(calc(15,2)))


def fac(num1):
    mul=1
    for i in range(1,num1+1):
        mul*=i

    return mul

def fac1(num1):
    if(num1==1):
        return 1
    
    return num1*fac1(num1-1)


# print(fac(5))
# print(fac1(5))

def greet(name,msg):
    print("hello",name,msg)

greet('ravi','good morning')
greet(name='ravi',msg='good moring')
greet('ravi',msg='good morning')
greet(msg='good morning',name='avi')
# greet('good moring',name='ravi')


def greet(name='ravi'):
    print("hello", name)

# greet('avi')
# greet(name='a')


def sum(*n):
    total=0
    for e in n:
        total+=e

    return total

# print(sum(10,102,14))

a=10

def fun():
    print(a)


fun()
print(a)

def fun1():
    global aa 
    aa=10
    print(aa)

fun1()

def fun2():
    print(aa)

fun2()
print('aa:',aa)


def fact(num):
    res=1
    while num>=1:
        res=res*num
        num-=1

    return res

print(fact(4))


sqr1= lambda n:n*n
print(sqr1(40))
# print(type(sqr1))
add=lambda a,b:a+b
print(add(1,2))



def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False

l1 = [1, 2, 4, 5, 6, 21, 24, 25]
l2 = list(filter(isEven, l1))
print(l2)

l3 = [11, 21, 42, 52, 61, 21, 24, 257]
l4 = list(filter(lambda x: x % 2 == 0, l3))
l5=[x%2==0 for x in l3]
print(l4,l5)

l6=list(filter(lambda x:x%3==1,l3))
print(l6)


l7=list(filter(lambda x:x%2==0,map(lambda x:x*x,l1)))
print(l7)

from functools import reduce

l7=reduce(lambda x,z:x-z,l1)
print(l7)

def div():
    print(3/2)

l7=div
l7()

print(l7 is div)

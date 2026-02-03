import sys
# print(sys.version)

# def func1():
#     print('python is a functional language')

# func1()


# class Class1:
#     def f2(self):
#         print('pytion is object oriented language')


# obj1=Class1()
# obj1.f2()

# cannot contain an special character
# ca$h=500
# print(ca$h)

# import keyword
# print(keyword.kwlist)

# a=10
# print(a)
# print(type(a))
# print(id(a))

# a=0O1001 #octal
# print(a)
# print(type(a))


# a=0X1111 #hexa
# print(a)
# print(type(a))

# a=0B0111 #binary
# print(a)
# print(type(a))


# print(oct(15))


# print(bin(15))
# print(bin(0X1456))
# print(bin(0O1456))

# print(oct(15))
# print(oct(0X1456))
# print(oct(0b111))

# print(hex(15))
# print(hex(0X1456))
# print(hex(0b111))
# print(hex(200))
     

# f = 1.234
# print(f)
# print(type(f))

# f = 1.2e3
# print(f)
# print(type(f))

# f = 1.2E3
# print(f)
# print(type(f))


# print(bin(0x234))


# a=True
# print(a)
# print(type(a))


# b=False
# print(b)
# print(type(b))


# print(True+True)
# print(True+False)

# b=[1,2,5,10]
# print(type(b))
# b1=bytes(b)

# for i in range(0,len(b)):
#     print(b1[i])
# print(b1)
# print(type(b1))
# b1=bytearray(b)
# b1[0]=10
# print(b1[0])


# s1='hello'
# print(s1)
# print(type(s1))
# print(id(s1))


# s2="Hello"
# print(s2)
# print(type(s2))
# print(id(s2))


# s3="""Hello"""
# print(s3)
# print(type(s3))
# print(id(s3))


# s1="""
# My name is "abhinav"
# """

# print(s1)
# print(type(s1))
# print(id(s1))

# s2='''
# the day is hectic '102323'
# '''

# print(s2)
# print(type(s2))
# s="hello"

# for i in range(0,len(s)):
#     print(i,s[i],end=" ")



# s="ABCDEFGHIJ"
# print(s*2)
# print(len(s))
# print(s[::-2])



# s9 = "toDay is a wonDERfuL dAY"
# print("Length of String:", len(s9))
# print("Upper case:", s9.upper())
# print("Lower case:", s9.lower())
# print("Swap case:", s9.swapcase())
# print("Title Case:", s9.title())
# print("Capitalize:", s9.capitalize())


# s="Tody is mondDay"
# print(s.upper())
# print(s.lower())
# print(s.swapcase())
# print(s.capitalize())
# print(s.title())


# print("Today"+" "+"is good")
# print(50*"h")
# print("h"*50)
# s="learn is fun and gun"
# print(s.split())
# print(type(s.split()))
# print(s.split("\t"))

# print(float())

# print(bool(0))
# print(bool(1))
# print(bool(10+3j))

# print(str(10))
# print(type(str(10.3)))

# var1="HEllo"
# var2="HEllo"
# print(var1 is var2)

# r1=range(10,20,4)
# for n in r1:
#     print(n)

# print(type(r1))
# print(r1[0])


# r2=list(r1)
# r2[0]=20
# print(r2)


# l1=[1,"abhi",4,10.4,1]
# l2=l1.copy()
# l2[0]=0
# print(l2,l1)
# print(l1)
# l1[0]="l2"
# print(type(l1[0]))
# l2=l1
# print(l2 is l1)
# print(id(l2))
# print(id(l1))
# print(l1+l2)


# l2=[1,2,3]
# print(l2)
# l2.append(10)
# print(l2)

# l1=(1,32,3342)
# l1.append(2)


# l1={'r':"Red",'b':"Blue"}
# l1['r']="Royal"
# print(l1['r'])

# s1={0,0}
# print(s1)
# s1.add(1)
# print(s1)
# s2=frozenset(s1)
# print(s2)

# x=None
# print(type(x))
# print(x)


# def greet():
#     print("Hello!")

# result = greet()
# print(result)
# print(type(result))


# a=9
# b=2
# print(a+b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(a**b)

# import math as m
# print(m.sqrt(16))
# print(m.pi)


# a=int(input("Enter num:"))
# b=int(input("Enter num1:"))
# c=int(input("Enter num2:"))

# min_val= a if a<b and a < c else b if b<c else c

# print(min_val)


# user=input("Enter mess:")

# if user=='root':
#     print("task₹")
#     print("task2")
# print("thank")


# print(range(10))
# for i in range(10):
#     print(i)


# ls=[2,3,4,324231,12]

# for i in range(len(ls)):
#     print(ls[i])

# str1="python"

# for x in str1:
#     print(x)

# for x in range(21):
#     if x%2==0:
#         print(x)

# for i in range(5):
#     for j in range(5):
#         print('i:', i," j=", j)

# cnt=0
# while (cnt<5):
#     print(cnt)
#     cnt+=1

# user =input("Enter name")
# while user!='root':
#     user=input("Enter name:")


# for i in range(5):
#     for j in range(i+1):
#         print('*',end=" ")
#     print()


# for i in range(6):
#     print("* "*(i+1))

# n=int(input("Enter number of rows:"))

# for i in range(1,n+1):
#     print("* "*i)
amount=10000
mx=0
for i in range(15):
    amount+=amount*5/100
    

print(amount)


amount=20000

for i in range(15):
    amount+=amount*8/100

print(amount)

sum_val=10000
initial_amount=10000
for i in range(14):
    initial_amount+=(initial_amount*5)/100
    sum_val+=initial_amount
    print(i,sum_val)
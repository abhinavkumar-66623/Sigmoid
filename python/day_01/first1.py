# for i in range(6):
#     print(i)
#     if i==4:
#         print("breaking the loop")
#         break


# for i in range(5):
#     if i==2:
#         continue
#     print(i)
# else:
#     print("all done")

   

# def fun1():
#     pass

# x=fun1()
# print(x)


# x=10
# print(x)
# del x
# # print(x)

# ls=[1,2,3]
# print(ls[0])
# print(type(ls[0]))
# print(id(ls[0]))
# ls[0]=2
# print(ls[0])
# print(type(ls[0]))
# print(id(ls[0]))

# x=1
# print(x)
# print(type(x))
# print(id(x))




amount =20000
year=15
rate=8

l=[]
for i in range(year):
    l.append(amount)
    amount=amount+amount*rate/100

print(amount)
print(l)
print(sum(l))
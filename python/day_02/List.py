# list1=[]
# print(list1)
# print(type(list1))


# list1=list(range(0,10,2))
# print(list1)


# str='learning is not fun its hectic'
# l=str.split()
# print(l)
# print(type)

# list1.append(1)
# print(list1,len(list1))


# l2=list(range(10,110,10))
# print(l2)
# print(l2[-1::-1])

# print(l2[:100])


# l1=[1,2,3]
# l2=[4,5,6]
# l3=l1+l2
# print(l3)


# l4=[]
# for i in range(1,101):
#     if i%10==0:
#         l4.append(i)

# print(l4)


# l5=[1,2,3]
# l6=l5
# l5.append(100)
# print(l5,l6)


# l7=l5.copy()
# l7.append(100)
# print(l7 is l5)
# print(l7,l5)


# print(l5)
# l5.insert(2,100)
# print(l5)

# l5.extend([91,23,24])
# l5.append("Hii")
# l5.append("bywe")
# sorted_1=sorted(l5,key=str)
# print(sorted_1)
# print(l5)
# l5.remove(23)
# print(l5)
# l5.pop(1)
# print(l5)
# # l5.sort()
# print("sort: " ,sorted_1)
# l5.clear()
# print(l5)


# l6=["abhi","cat","rice","wheat","aaa","bowl"]
# l6.sort()
# print(l6)

# l8=[x*x for x in l5]
# print(l8)


# l1=[1,2,3]
# l2=[1,2,3]

# print(id(l1),id(l2))


# s1=[]
# for x in range(1,11):
#     s1.append(x*x)


# print(s1)

# s2=[x*x for x in range(1,11)]
# print(s2)

# print(s1 is s2)

# s3=[x%10==0 for x in range(1,11)]
# print(s3)



# words=["Identifier","kwyword","abhinav","banger"]

# s1=[w[0] for w in words]
# print(s1)


# str2 = "the quick brown fox jumps over the lazy dog"
# words=str2.split()
# s2=[(w.upper(),len(w)) for w in words]
# print(s2)

# list1=['a','b','c','d','e','f']
# list2=['a','b','c']
# list3=[x for x in list1 if x  in list2]
# print(list3)
# list4=list1*3
# print(list4)

# l1=[1,2,1]

# l1.remove(1)
# print(l1)
# l1.reverse()
# l1.remove(1)
# print(l1)


# l1=[1,2,3]
# l2=l1.copy()

# print('Before')
# print('l1 ',l1)
# print('l2 ',l2)
# l1.append(4)
# print('l1 ',l1)
# print('l2 ',l2)



# l3=[1,2,[3,4]]
# l4=l3.copy()

# print(l3)
# print(l4)

# l3[2].append(99)
# l3.append(100)
# print(l3)
# print(l4)

import copy
l1=[1,2,[3,4],5]
l2=copy.deepcopy(l1)

print (l1)
print(l2)

l1[2].append(99)
print (l1)
print(l2)


l1.append(4)
print (l1)
print(l2)

import module1 as m
print(m.x)
print(m.add(1,2))



from module1 import add
print(add(2,5))
print(dir(m))


import math as m
print(m.sqrt(35))
print(len(dir(m)))

l=[1,23,423]
l1=l.copy()
l2=copy.deepcopy(l)
l2.append(28)
l.append(32)

print(l,l1,l2)


# t3 = (10)
# print(t3)
# print(type(t3))

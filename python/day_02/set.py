se1={}
print(se1)

se2=set()
print(se2)

se3=set(range(1,5))
se3.add(4)
print(se3)
se3.add(0)

l1=['a','b']
l2=['x','y']
se3.update(l1,l2)
print(se3)

se4=se3.copy()
print(se4)


# while(len(se3)!=0):
#     print(se3.pop(),end=" ")
# se3.pop()
# se3.pop()

# print()
# se3.remove('a')
# print(se3)
# se3.clear()
# print(se3)


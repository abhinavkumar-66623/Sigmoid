# ls=1,2,34
# print(type(ls))

# ls1=(1,3424,42,5254,)
# print(type(ls1))

# ls3=1,
# print(type(ls3))

# ls4=list(ls1)
# ls4.append(5)
# print(ls4)
# print(ls[0])
# print(ls[-2])

# ls6=ls+ls1
# print(ls6)
# print(ls6.count(1))
# print(min(ls6),max(ls6))

# print(sorted(ls6))


# a=10;b=20;c=30;d=40
# t8=a,b,c,d
# print(t8)

# a,*b=(1,2,3,4,5)
# print(a,b)
# a,*b=[43,32,21,45,32]
# print(a,b)
# r,f,*g='abhinav'
# print(r ,f ,g )


market={}
print(market)
print(type(market))


market['store1']={'name':'online'}
market['store2']={'name':'offline'}
print(market)


market['store1']['items']=[
    {'name':'laptop','price':'8000'},
    {'name':'mobile','price':'10000'}
]


market['store2']['items']=[
    {'name':'headset','price':'8000'},
    {'name':'earphone','price':'10000'}
]


print(market)

import json
print(json.dumps(market,indent=4))


print(market['store1']['name'])


#print all items in store1 if items is laptop print its price 


print(market['store1']['items'])
items=market['store1']['items']
for i in items:
    if(i['name']=='laptop'):
        print(i['price'])
    
# print(
# market['store1']['r'])

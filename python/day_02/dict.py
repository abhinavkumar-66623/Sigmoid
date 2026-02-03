# d1={}
# print(d1)
# print(type(d1))

# d2=dict()
# print(d1)
# print(d1 is d2)

# d2['st']='start'
# d2['end']='end'

# print(d2.keys())
# print(d2.values())

# print(d2)
# d1=d2.copy()
# print(d1)
# del d1

# for k,v in d2.items():
#     print(k+"_"+v)



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
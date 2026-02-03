
# amount=1000;rate=10
# amount_1_year=amount+amount*rate/100
# amount_2_year=amount_1_year+amount_1_year*rate/100
# amount_3_year=amount_2_year+amount_2_year*rate/100
# amount_4_year=amount_3_year+amount_3_year*rate/100
# amount_5_year=amount_4_year+amount_4_year*rate/100

# print(amount_5_year)


# #using loops
# for _ in range(5):
#     amount=amount+amount*rate/100

# print(amount)



# #using functions

# def get_amount(initial,rate,years):

#     for _ in range(years):
#         initial+=initial*rate/100
    
#     return initial

# print(get_amount(1000,4,20))


#collections for organising data

# years=20
# investments=[('stocks',500),('savings',500)]
# rates={'stocks':8,'savings':4}


# for items in investments:
#     category=items[0]
#     amount=items[1]
#     rate=rates[category]
#     print(category,amount,rate)


import random
# print(random.randint(9,20))


#Introduce randomness
def get_stock_rate():
    return random.randint(-8,20)

def get_savings_rate():
    return random.randint(2,7)

def get_amount(initial,rate_fn,years):
    amount=initial
    for _ in range(years):
        amount+=amount*rate_fn()/100

    return amount

    

def run_simulation():
    years=20
    investments=[('stocks',500),('savings',500)]
    rates={'stocks':get_stock_rate,'savings':get_stock_rate}
    total=0

    for item in investments:
        category=item[0]
        amount=item[1]
        rate_fn=rates[category]
        total+=get_amount(amount,rate_fn,years)
    return total


output=[]

for _ in range(1000):
    output.append(run_simulation())


# print(max(output) ,min(output),sum(output)/len(output))


#write results in file

from datetime import datetime


def get_stock_rate():
    return random.randint(-8,20)

def get_savings_rate():
    return random.randint(2,7)

def get_amount(initial,rate_fn,years):
    amount=initial
    for _ in range(years):
        amount+=amount*rate_fn()/100

    return amount

    

def run_simulation():
    years=20
    investments=[('stocks',500),('savings',500)]
    rates={'stocks':get_stock_rate,'savings':get_stock_rate}
    total=0

    for item in investments:
        category=item[0]
        amount=item[1]
        rate_fn=rates[category]
        total+=get_amount(amount,rate_fn,years)
    return total


output=[]

for _ in range(1000):
    output.append(run_simulation())

with open('simulation_output.txt','a') as f:
    f.write(50 * '-'+ '\n')
    f.write('Exexution Time '+ str(datetime.now())+'\n')
    f.write(str(max(output))+'\n')
    f.write(str(min(output))+'\n')
    f.write(str(sum(output)/len(output))+'\n')
    f.write('Execution Time'+ str(datetime.now())+ '\n')
    f.write(50 * '-'+ '\n')



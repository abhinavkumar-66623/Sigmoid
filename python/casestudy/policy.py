from datetime import datetime
import random
insurance_plans={1:'Standard_Policy',2:'Premium_Policy'}
standard={'initial_premium':10000,'annual_increase':5}
premium={'initial_premium':20000,'annual_increase':8}

customer_count=0
premium_rates_total=[]
while(customer_count<5000):
    customer_count+=1
    print('-'*50)
    print('-'*50)
    print("select one policy : ")
    Enter_num=random.randint(1,2)
    print(f"Policy Selected: {Enter_num}")
    Enter_policy_duration=15
    if Enter_num==1:
        initial_amount=standard['initial_premium']
        initial_rate=standard['annual_increase']
        sum_val=initial_amount
        for i in range(Enter_policy_duration-1):
            initial_amount+=(initial_amount*initial_rate)/100
            sum_val+=initial_amount


        premium_rates_total.append(sum_val)

            
    else:
        initial_amount=premium['initial_premium']
        initial_rate=premium['annual_increase']
        sum_val=initial_amount
        for i in range(Enter_policy_duration-1):
             initial_amount+=(initial_amount*initial_rate)/100
             sum_val+=initial_amount

        premium_rates_total.append(sum_val)

            

with open("insurance_premium_report.txt",'a') as report:

        report.write("-"*100+'\n')
        report.write(f"Date_Time: {str(datetime.now())} \n")
        sum_amount=sum(premium_rates_total)
        max_amount=max(premium_rates_total)
        min_amount=min(premium_rates_total)


        avg_Amount=sum_amount/len(premium_rates_total)
        report.write(f"Total Premium Collection:  {sum_amount}"+'\n')
        report.write(f"Highest Premium Paid:      {max_amount}"+'\n')
        report.write(f"Lowest Premium Paid:       {min_amount}"+'\n')
        report.write(f"Average Premium Paid:      {avg_Amount}"+'\n')
        report.write("-"*100+'\n')

    
            
        

        












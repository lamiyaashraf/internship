l=[1,2,3,4,5]
OUTPUT=dict(map(lambda x:(x,x*2),l))
print(OUTPUT)
l=[1,2,3,4,5]
output={i:i*2 for i in l}
print(output)
##########################################################################################################################################
prices=[15,20,10,30,50]
prices_below_20=[price for price in prices if price<20]
print(prices_below_20)
############################################################################################################################################
customers=['Rahul','Antony','salman','Arun','Kiran']
customer_start_with_a=[customer for customer in customers if customer.startswith('A')]
print(customer_start_with_a)
########################################################################################################################################
employees={'Antony':55000,'Susan':45000,'Kiran':60000}
categorized_employees={name:'high' if salary>50000 else 'low' for name,salary in employees.items()}
print(categorized_employees)
#######################################################################################################################################
words=['apple','banana','apple','orange','banana','apple']
count_word={word:words.count(word) for word in set(words)}
print(count_word)
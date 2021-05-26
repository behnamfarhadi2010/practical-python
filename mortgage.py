# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment = 1000.0
month = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    month = month + 1
    if principal > payment:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
    else:
        payment = principal * (1+rate/12)
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment

    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    print('Month',month, 'Total Paid', round(total_paid,2), 'Debt', round(principal, 2))   
print (f'Total paid  {round(total_paid,2)} in {month} months')








# Exercise 1.7

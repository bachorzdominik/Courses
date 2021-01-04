# https://hyperskill.org/projects/90/stages/501/implement
from math import ceil

loan_principal = int(input('Enter the loan principal: '))
calculate = input('''What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:''')

if calculate == 'm':
    monthly_payment = int(input('Enter the monthly payment: '))
    n_months = ceil(loan_principal / monthly_payment)
    if n_months == 1:
        print(f'It will take {n_months} month to repay the loan')
    else:
        print(f'It will take {n_months} months to repay the loan')
elif calculate == 'p':
    n_months = int(input('Enter the number of months: '))
    payment = ceil(loan_principal / n_months)
    last_payment = loan_principal - (n_months - 1) * payment
    print(f'Your monthly payment = {payment} and the last payment {last_payment}')

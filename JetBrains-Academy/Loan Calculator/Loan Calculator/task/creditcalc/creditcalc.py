# https://hyperskill.org/projects/90/stages/502/implement
import math

calculate = input('''What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
''')

if calculate == 'n':
    loan_principal = int(input('Enter the loan principal: '))
    monthly_payment = int(input('Enter the monthly payment: '))
    loan_interest = float(input('Enter the loan interest: '))

    interest_rate = (loan_interest / 100) / (12 * 1)

    number_of_months = math.log((monthly_payment / (monthly_payment - interest_rate * loan_principal)),
                                (1 + interest_rate))
    number_of_months = math.ceil(number_of_months)

    if number_of_months == 1:
        print(f'It will take {number_of_months} month to repay the loan')
    elif number_of_months <= 12:
        print(f'It will take {number_of_months} months to repay the loan')
    else:
        years = math.floor(number_of_months / 12)
        months = number_of_months - (12 * years)
        print(f'It will take {years} years and {months} months to repay this loan!')

elif calculate == 'a':
    loan_principal = int(input('Enter the loan principal: '))
    number_of_months = int(input('Enter the number of periods: '))
    loan_interest = float(input('Enter the loan interest: '))

    interest_rate = (loan_interest / 100) / (12 * 1)

    monthly_payment = loan_principal * ((interest_rate * pow(1 + interest_rate, number_of_months))
                                        / (pow(1 + interest_rate, number_of_months) - 1))
    print(f'Your monthly payment = {math.ceil(monthly_payment)}!')

elif calculate == 'p':
    annuity_payment = float(input('Enter the annuity payment: '))
    number_of_months = int(input('Enter the number of periods: '))
    loan_interest = float(input('Enter the loan interest: '))

    interest_rate = (loan_interest / 100) / (12 * 1)
    loan_principal = annuity_payment / ((interest_rate * math.pow(1 + interest_rate, number_of_months))
                                        / (math.pow(1 + interest_rate, number_of_months) - 1))

    print(f'Your loan principal = {round(loan_principal)}!')

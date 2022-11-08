## Part A: House Hunting
## Write a program to calculate how many months it will take you to
## save up enough money for a down payment. You will want your main
## variables to be floats so you shoudld cast user inputs as floats.

annual_salary = float(input('Enter annual salary: '))
portion_saved = float(input('Enter the monthly portion (in percentage) to save: '))/100
total_cost = float(input('Enter cost of your dream home: '))
portion_down_payment = 0.25
current_savings = 0
r = 0.04
down_payment = total_cost*portion_down_payment

n=0
while current_savings < down_payment:
    n += 1
    current_savings += current_savings*r/12 + portion_saved*annual_salary/12

    if current_savings == down_payment:
        break

print('Number of months: ', n)


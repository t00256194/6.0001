## Part B: Saving, with a raise
## Write a program to calculate how many months it will take you to
## save up enough money for a down payment. Factor in a raise every
## six months. Assume the same interest rate and down payment. 

annual_salary = float(input('Enter annual salary: '))
portion_saved = float(input('Enter the monthly portion (percentage) to save: '))/100
monthly_savings = annual_salary/12*portion_saved

total_cost = float(input('Enter cost of your dream home: '))
portion_down_payment = 0.25
down_payment = total_cost*portion_down_payment

semi_annual_raise = float(input('Enter semi-annual raise (percentage): '))/100

r = 0.04
current_savings = 0

n=0

while current_savings < down_payment:
    n += 1
    current_savings += monthly_savings + current_savings*r/12 

    if n%6 == 0:
        annual_salary += annual_salary*semi_annual_raise
        monthly_savings = annual_salary/12*portion_saved

print('Number of months: ', n)
  

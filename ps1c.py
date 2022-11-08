## Part C: Finding the right amount to save away
### Suppose you want to be able to afford down payment in three 
### years. Write a program that finds the best monthly salary 
### savings rate.

total_cost = 1e6                                             #total home cost 
portion_down_payment = 0.25                                  #down payment percent
down_payment = total_cost*portion_down_payment               #down payment total
annual_return = 0.04                        
semi_annual_raise = 0.07                                  
                
annual_salary = float(input('Enter annual salary: '))        #annual salary
current_savings = 0                                          #current savings

tol = 100                                                    #tolerance
min = 0                                                      #left boundary of guess
max = 10000                                                  #right boundary of guess

step_count = 0

while abs(down_payment - current_savings) >= tol:

    step_count += 1

    salary = annual_salary
    r = annual_return
    s = semi_annual_raise

    current_savings = 0

    #integer division
    mid = (min + max)//2
    
    #float division
    monthly_savings = ((min + max)/2/10000)*salary/12

    for n in range(36):
        current_savings += monthly_savings + current_savings*r/12

        if n%7 == 0:
            salary += salary*s
            current_savings += monthly_savings + current_savings*r/12

    if abs(down_payment - current_savings) <= tol :
        portion_saved = mid/10000                 
        print('Best savings rate: ', portion_saved)
        print('Steps in bisection search: ', step_count)
        break

    if current_savings < down_payment:
        min = mid   

    else :
        max = mid
                                  
    if step_count > 37:
        print('Not possible to save for down payment in  36 months')
        break

    #check value test
    print(mid/10000, current_savings)


    












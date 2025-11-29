# Code to take the input of montly contribution and goal 
# and annual interest to find total deposit and How long it would take

# Author: Ri

# Import math
import math

# Input of interest rate per year, montly contribution, goal
inp_rate = float(input("Please input the rate of interest you receive in savings account annually(in percentage): "))
inp_contribution = float(input("Please input your monthly contribution to your savings account: "))
inp_goal = float(input("Please input the final goal of monetary value that you want to achieve: "))

# check how long it would take to reach the goal with the interest as well
# best option is to turn the annual rate to montly rate
# then apply it montly to each month
monthly_rate = inp_rate/1200 # in decimals

# Need some values that in a loop would add up for conditionals
time_taken_years = 0
final_amount = 0
penultimate_amount = final_amount

# The loop that does the check and calculates the time period to final answer so that last years problem can be solved
for i in range(12):
    final_amount = inp_contribution * (1 + monthly_rate)
while final_amount <= inp_goal:
    time_taken_years += 1
    penultimate_amount = final_amount
    for i in range(12):
        final_amount = inp_contribution * (1 + monthly_rate)

# Calculations for last year
amount_remaining_for_last_year = inp_goal - penultimate_amount
months_for_last_year = math.ceil(amount_remaining_for_last_year / inp_contribution)


but i also need to check for the last years months since if it doesnt amount to 12 for last 
year then the yearly interest would not be applied to the amount

# print output
print(f'Your montly contribution of {inp_contribution} along a period of {time_taken_years} years and {months_for_last_year} months would allow a saving goal success')
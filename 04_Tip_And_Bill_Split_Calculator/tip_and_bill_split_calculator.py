# this codes does these steps: takes bill value, tip percentage, split direction and then displays total tip and bill split
# Author: Ri

# Ask for input regarding bill
bill_input = float(input("Please input the final bill outcome: "))

# Ask them what their tip percentage is. Set range else it loops
tip_pcent = float(input("Please input the tip percentage above 0.1(decimals): "))
while tip_pcent < 0.1:
    tip_pcent = float(input("Please input the tip percentage above 0.1(decimals): "))

# Calculating the tip based on percentage.
tip_value = tip_pcent * bill_input

# Ask for split direction count
split_direction = int(input("How many directions do you want to split the bill? "))

# Calculate total payment divided by split direction count
total_payment = tip_value + bill_input
unit_payment = total_payment / split_direction

# Print bill amount, tip percentage, tip, split direction, split price
print(f'Bill amount: {bill_input} \nTip Percentage: {tip_pcent * 100} % \nTip: {tip_value}')
print(f'Total split directions: {split_direction} \nPayment per person: ${unit_payment:.2f}')
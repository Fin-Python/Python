# This code takes the principle, rate, time and compound frequency to calculate the compound interest
# It also calculates the amount after that period
# Author: Ri

# Take the input values of principle, rate, time period and compound freqnecy
inp_prin = float(input("Please provide the principle value: "))
inp_rate = float(input("Please provide the rate in percentage: ")) / 100
inp_time = float(input("Please provide the time period: "))
inp_freq = int(input("Please provide the compound frequency per year: "))

# Calculate the Amount
amount = inp_prin * ((1 + (inp_rate / inp_freq)) ** (inp_freq * inp_time))

# Calculate the Interest
interest = amount - inp_prin

# Print the information to console
print(f'Your principle amount is: {amount}\nYour total interest to pay is: {interest}')
# Calculates the profit or loss made from stock trading
# Simple model. only takes buy and sell values to calculate the difference for profit/loss
# Author: Ri

# Take input regarding the buy value, sell value
inp_buy = float(input("Please provide the buy value per share: "))
inp_sell = float(input("Please provide the sell value per share: "))
inp_count = float(input("Please provide the share count bought: "))

# Compute the Profit/Loss
profit_loss = inp_sell - inp_buy
total_p_l = profit_loss * inp_count

# Print output
if profit_loss > 0:
    judgement = 'Profit'
elif profit_loss == 0:
    judgement = 'Nothing'
else:
    judgement = 'Loss'

print(f'You made a {judgement} of {round(abs(profit_loss), 3)} per share with total {judgement} of {round(abs(total_p_l),3)}')
# Loan Payment - EMI
# EMI - Equated Monthly installments
# EMI includes part of the principle and part of interest
# This code would take the loan value and then calculate the monthly EMI and total interest paid
# Author: Ri

# Take inputs of Principle, Rate and Installment counts

# take values
inp1 = int(input("Please provide the principle amount loaned: "))
inp2 = int(input("Please provide the Rate of interest per year in percentage: "))
inp3 = int(input("Please provide the time period in months: "))

# compute the EMI
emi = (inp1 * (inp2/1200) * ((1+(inp2/1200)) ** inp3))/(((1+(inp2/1200)) ** inp3) - 1)

# print EMI
print("Your monthly emi is: " + str(round(emi, 2)))

# compute total interest paid
total_paid = emi * inp3
total_interest = total_paid - inp1

# print interest paid
print("Your total interest paid: " + str(round(total_interest, 2)))
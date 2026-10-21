# Takes the income and calculates the tax required to pay
# Complicating it using tax bracket

# Author: Ri

# Creating class for holding subroutines for checking tax bracket and then for calculating tax
# These are tax brackets of netherlands 2025
class ne_tax:
    def taxes(a):
        # Bracket 1
        if a <= 38882:
            return 0.357 * a
        
        # Bracket 2
        elif a <= 77319:
            b = a - 38882
            c = 0.3756 * b
            return c + ne_tax.taxes(38882)
        
        # Bracket 3
        elif a > 77319:
            b = a - 77319
            c = b * 0.495
            return c + ne_tax.taxes(77319)
        
# asking for income
x = int(input("What is your income? I will calculate your income tax: "))

# calculating tax by calling methods
y = ne_tax.taxes(x)

# printing tax
print(f'Your income tax is {y}')

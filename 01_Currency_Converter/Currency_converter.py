# Program to convert between currency
# For ease of working, considered currency are Euro and Dollar

# Author: Ri

# Create a class for conversion
class EuroDollar:
    FIXED_RATE_EU_DO = 1.12
# Create methods in the class for linear singular conversion to target currency
    @staticmethod
    def toDollar(a):
        b = a * EuroDollar.FIXED_RATE_EU_DO
        return b
    
    @staticmethod
    def toEuro(a):
        b = a / EuroDollar.FIXED_RATE_EU_DO
        return b

# Take input
a = int(input("Please tell me the value to convert:"))
x = int(input("If you want to convert to Euro input 1, else if you wnat to convert to Dollar, input 2"))

# call method from class
while x!=1 and x!=2:
    if x == 1:
        converted = EuroDollar.toEuro(a)
    elif x == 2:
        converted = EuroDollar.toDollar(a)

# Print output
print(f'Your converted value is {converted}')
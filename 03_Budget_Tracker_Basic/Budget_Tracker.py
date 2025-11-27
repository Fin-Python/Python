# Takes all income sources and expense sources, stores them in list and then calculates leftovers
# Author: Ri

# Create basic menu on the CLI
print('Hello, I will act as the budget manager for you to manage your income and outcome')
print("1. Add incoming value")
print("2. Add outgoing value")
print("3. Show summary")
print("4. Exit")

# should have 2 lists for each of incoming and outgoing
# For incoming
a = []
# For outgoing
b = []

c = int(input("Choose the number based on the action to be taken"))

# Should include, add incoming, add outgoing, summary, and exit
while c != 1 and c != 2 and c != 3 and c != 4:

    # Switch to each method for the tasks 
    if c == 1:
        d = int(input("Provide the value: "))
        a.append(d)
    elif c == 2:
        d = int(input("Provide the value: "))
        b.append(d)

    # for summary, print sum and leftover
    elif c == 3:
        print(f'The total incoming monetary value is: {sum(a)}')
        print(f'The total outgoing monetary value is: {sum(b)}')
        print(f'The total remaining value is: {sum(a) - sum(b)}')

    # for exit, exits program
    else:
        exit()

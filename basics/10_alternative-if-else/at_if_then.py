# i want to try the 2 ways that i have found of doing a if then else statements.

print("""
1: Message 1
2: Message 2
3: Message 3
4: Message 4
""")

print("""
1: If-else chain
2: Dictionary lookup
""")
a = int(input("Please input the number for which you wanna see the output"))
b = int(input("please state which type of branch you wanna do?"))

tup = (a,b)

def ifelsechain(tup):
    print("this is ifelse chain")
    if tup[0] == 1:
        print("Message 1")
    elif tup[0] == 2:
        print("Message 2")
    elif tup[0] == 3:
        print("Message 3")
    else:
        print("Message 4")

def dictionarychain(tup):
    print("this is dictionary chain")
    dic = {
        1: "Message 1",
        2: "Message 2",
        3: "Message 3", 
        4: "Message 4"
    }
    print(dic[tup[0]])

if tup[1] == 1:
    ifelsechain(tup)
elif tup[1]== 2:
    dictionarychain(tup)

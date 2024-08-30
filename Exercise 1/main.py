from math import *
"""

money = int(input("How much money do you have?: "))

canAfford = money / 100
neededMoney = float(ceil(canAfford)) - canAfford

print("You can afford", canAfford, "Wii's")
print("You need", neededMoney, "more to buy another one")
"""

"""
userInt = int(input("Enter a number: "))
factorial = 1
for x in range(1, userInt+1):
    factorial = factorial * x

print(factorial)
"""

factorList = []
userInt = int(input("Choose a number: "))
for x in range(1 , userInt + 1):
    if userInt % x == 0:
        factorList.append(x)
        print(x)
print(factorList)

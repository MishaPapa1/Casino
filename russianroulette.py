import random

def russianrou(balance):
    print("Welcome to Russian Roulette!")
    print("What would you like to do? ")
    print("1.Load one bullet.")
    print("2.Load two bullets.")
    print("3.Load three bullets.")
    print("4.Load four bullets.")
    print("Press Q to quit.")
    choice = input("What do you choose? ")

    while choice != "q" and choice != "Q":
        if choice == "1":
            bet = int(input("How much would you like to bet? $"))
            y = input("In which chamber do you want to introduce the bullet? From 1-6 ")
            x = random.randint(0,100)
            if x < 16:
                balance = balance - bet
                print("You have lost. ")
                print(f"Your new balance is: {balance}")
            else:
                balance = balance + bet
                print("You have won.")
                print(f"Your new balance is now: ${balance}")
        if choice == "2":
            bet = int(input("How much would you like to bet? $"))
            y = int(input("In which chamber do you want to introduce the bullet? From 1-6 "))
            x = random.randint(0,100)
            if x < 33:
                balance = balance - bet
                print("You have lost. ")
                print(f"Your new balance is now: ${balance}")
            else:
                balance = balance + bet * 2
                print("You have won.")
                print(f"Your new balance is now: ${balance}")
        if choice == "3":
            bet = int(input("How much would you like to bet? $"))
            y = int(input("In which chamber do you want to introduce the bullet? From 1-6 "))
            x = random.randint(0,100)
            if x < 50:
                balance = balance - bet
                print("You have lost. ")
                print(f"Your new balance is now: ${balance}")
            else:
                balance = balance + bet * 3
                print("You have won.")
                print(f"Your new balance is now: ${balance}")
        if choice == "4":
            bet = int(input("How much would you like to bet? $"))
            y = int(input("In which chamber do you want to introduce the bullet? From 1-6 "))
            x = random.randint(0,100)
            if x < 66:
                balance = balance - bet
                print("You have lost. ")
                print(f"Your new balance is now: ${balance}")
            else:
                balance = balance + bet * 4
                print("You have won.")
                print(f"Your new balance is now: ${balance}")
        return balance


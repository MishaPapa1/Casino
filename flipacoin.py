import random
import time

def albaneagra(balance):
    print("Welcome to Flip-a-Coin")

    bet = int(input("How much would you like to bet? $"))
    choice = input("Heads or Tails? ").lower()
    print("You have chosen:",choice)

    result = random.randint(0,1)
    if result == 0:
        print("The coin has been flipped and is..")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("Tails")
    else:
        print("The coin has been flipped and is..")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("Heads")

    if choice == "heads" and result == 1:
        print("You have won")
        balance = balance + bet
    elif choice == "heads" and result == 0:
        print("You have lost")
        balance = balance - bet
    elif choice == "tails" and result == 1:
        print("You have lost")
        balance = balance - bet
    else:
        print("You have won")
        balance = balance + bet
    return balance


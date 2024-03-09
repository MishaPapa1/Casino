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
        balance = balance + bet
        print(f"You have won: ${bet}")
        print(f"Your new balance is now: ${balance}")
    elif choice == "heads" and result == 0:
        balance = balance - bet
        print(f"You have lost: ${bet}")
        print(f"Your new balance is now: ${balance}")
    elif choice == "tails" and result == 1:
        balance = balance - bet
        print(f"You have lost: ${bet}")
        print(f"Your new balance is now: ${balance}")
    else:
        balance = balance + bet
        print(f"You have won: ${bet}")
        print(f"Your new balance is now: ${balance}")
    return balance




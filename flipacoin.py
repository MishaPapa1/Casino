import random
import time

def albaneagra():
    print("Welcome to Flip-a-Coin")

    bet = input("How much would you like to bet? $")
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
    elif choice == "heads" and result == 0:
        print("You have lost")
    elif choice == "tails" and result == 1:
        print("You have lost")
    else:
        print("You have won")


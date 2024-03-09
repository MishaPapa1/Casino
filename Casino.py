from Deposit import deposit
from Menu import menu
from flipacoin import albaneagra
from russianroulette import russianrou
balance = 0

balance = int(deposit())

alegere = menu()

while alegere != "q" and alegere != "Q":
    if alegere == "1":
        print(f"Your balance is: {balance}$")
    elif alegere == "2":
        print(f"Your current balance is: {balance}$")
        new_ammount = input("How much would you like to add? $")
        if new_ammount.isdigit():
            new_ammount = int(new_ammount)
            balance += new_ammount
            print(f"Your new balance is now: {balance}$")
        else:
            print("Please input a valid number. ")
    elif alegere == "3":
        balance = albaneagra(balance)
    elif alegere == "4":
        balance = russianrou(balance)
    alegere = menu()

print(balance)

#bet shouln't be bigger than the balance





import albaneagra

def deposit():
    amount = input("How much would you like to deposit? $")
    while not amount.isdigit() or int(amount) < 0:
        print("You have to enter a valid positive number. ")
        amount = input("How much would you like to deposit? $")

    return amount

balance = int(deposit())

def menu():
    print("What would you like to do? ")
    print("1. Check your balance. ")
    print("2. Add to your balance. ")
    print("3. Play Flip-a-Coin. ")
    print("Press Q to quit. ")

    alegere = input("What is your choice? ")

    results = {"1", "2", "3", "Q", "q"}

    while alegere not in results:
        print("Please input a valid choice(1, 2, 3): ")
        alegere = input("What is your choice? ")
    return alegere

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
    alegere = menu()


#pana aici






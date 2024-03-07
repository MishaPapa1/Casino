def deposit():
    amount = input("How much would you like to deposit? $")
    while not amount.isdigit() or int(amount) < 0:
        print("You have to enter a valid positive number. ")
        amount = input("How much would you like to deposit? $")

    return amount
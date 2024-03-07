def menu():
    print("What would you like to do? ")
    print("1. Check your balance. ")
    print("2. Add to your balance. ")
    print("3. Play Flip-a-Coin. ")
    print("Press Q to quit. ")

    alegere = input("What is your choice? ")

    results = {"1", "2", "3", "Q", "q"}

    while alegere not in results:
        print("Please input a valid choice(1, 2, 3, Q): ")
        alegere = input("What is your choice? ")
    return alegere
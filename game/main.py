import random

def choose_option():
    options = ("piedra", "papel", "tijera")
    user_option = input("Elija piedra, papel o tijera: ")
    user_option = user_option.lower()
    if not user_option in options:
        print("No valid option")
        return None, None
    computer_option = random.choice(options)
    print("User option => ", user_option)
    print("Computer option => ", computer_option)
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print("Draw game")
    elif user_option == "piedra":
        if computer_option == "tijera":
            print("piedra gana a tijera, usted gana")
            user_wins += 1
        else:
            print("papel gana a piedra, usted pierde")
            computer_wins += 1
    elif user_option == "papel":
        if computer_option == "piedra":
            print("papel gana a piedra, usted gana")
            userWins += 1
        else:
            print("tijera gana a papel, usted pierde")
            computer_wins += 1
    elif user_option == "tijera":
        if computer_option == "papel":
            print("tijera gana a papel, usted gana")
            user_wins += 1
        else:
            print("piedra gana a tijera, usted pierde")
            computer_wins += 1
    return user_wins, computer_wins

def run_game():
    user_wins = 0
    computer_wins = 0
    rounds = 1

    while True:
        print("*" * 10)
        print("ROUND ", rounds)
        print("*" * 10)

        user_option, computer_option = choose_option()
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
        
        print('User wins: ', user_wins)
        print('Computer wins: ', computer_wins)
        rounds += 1

        # Refactor this the next weekend
        if computer_wins == 2:
            print("La máquina ha vencido")
            break
        if user_wins == 2:
            print("Usted ha vencido")
            break

run_game()
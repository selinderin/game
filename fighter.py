import random

def menu():
    print("Game mode choice:")
    print("1: Human vs Human")
    print("2: Human vs Robot")
    print("3: Human vs Strategy")
    
    choice = input("Select your game mode by pressing the right number: ")

    if choice == '1': 
        print("You chose Human vs Human mode")
        return 'human_vs_human'
    elif choice == '2':  
        print("You chose Human vs Robot mode")
        return 'human_vs_robot'
    elif choice == '3': 
        print("You chose Human vs Strategy mode")
        return 'human_vs_strategy'
    else:
        print("Your choice is invalid. Please enter the right number.")  
        return None


success_rates = {
    1: 1.0, 
    2: 0.9, 
    3: 0.8,  
    4: 0.7,   
    5: 0.6,  
    6: 0.5,   
    7: 0.4,   
    8: 0.3,   
    9: 0.2    
}


def hit_value(hv):
    if hv in success_rates:
        return random.random() < success_rates[hv]
    else:
        return False


def human_vs_human():
    hp1 = 50
    hp2 = 50

    while hp1 > 0 and hp2 > 0: 
        print("\nTurn of Player 1:")
        while True:
            try:
                frc1 = int(input("Player 1, please choose your attack (1-9): "))
                if frc1 < 1 or frc1 > 9:
                    print("Please enter a number between 1 and 9.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
        
        hit1 = hit_value(frc1)
        if hit1:
            hp2 -= frc1
            print(f"Nice one! Player 2 loses HP. Player 2's HP: {hp2}")
        else:
            print("You missed!")

        if hp2 <= 0:
            print("Player 1 wins!")
            break

        print("\nTurn of Player 2:")
        while True:
            try:
                frc2 = int(input("Player 2, please choose your attack (1-9): "))
                if frc2 < 1 or frc2 > 9:
                    print("Please enter a number between 1 and 9.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")

        hit2 = hit_value(frc2)
        if hit2:
            hp1 -= frc2
            print(f"Nice one! Player 1 loses HP. Player 1's HP: {hp1}")
        else:
            print("You missed!")

        if hp1 <= 0:
            print("Player 2 wins!")
            break


def human_vs_robot():
    hp1 = 50
    hp2 = 50

    while hp1 > 0 and hp2 > 0: 
        print("\nTurn of Human Player:")
        while True:
            try:
                frc1 = int(input("Player, please choose your attack (1-9): "))
                if frc1 < 1 or frc1 > 9:
                    print("Please enter a number between 1 and 9.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")

        hit1 = hit_value(frc1)
        if hit1:
            hp2 -= frc1
            print(f"Nice one! Robot loses HP. Robot's HP: {hp2}")
        else:
            print("You missed!")

        if hp2 <= 0:
            print("Player wins!")
            break

        print("\nTurn of Robot:")
        frc2 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
        print(f"Robot chooses attack: {frc2}")

        hit2 = hit_value(frc2)
        if hit2:
            hp1 -= frc2
            print(f"Robot hits! Human Player loses HP. Human Player's HP: {hp1}")
        else:
            print("Robot missed!")

        if hp1 <= 0:
            print("Robot wins!")
            break


def strategy(hp1, hp2):
    if hp1 <= 10:
        return random.choice([6, 7, 8, 9])
    elif hp2 <= 10:
        return random.choice([6, 7, 8, 9])
    else:
        return random.choice([1, 2, 3, 4, 5])


def human_vs_strategy():
    hp1 = 50
    hp2 = 50

    while hp1 > 0 and hp2 > 0:
        print("\nTurn of Human Player:")
        while True:
            try:
                frc1 = int(input("Player, please choose your attack (1-9): "))
                if frc1 < 1 or frc1 > 9:
                    print("Please enter a number between 1 and 9.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")

        hit1 = hit_value(frc1)
        if hit1:
            hp2 -= frc1
            print(f"Nice one! Strategic Bot loses HP. Bot's HP: {hp2}")
        else:
            print("You missed!")

        if hp2 <= 0:
            print("Player wins!")
            break

        print("\nTurn of Strategic Bot:")
        frc2 = strategy(hp1, hp2)
        print(f"Strategic Bot chooses attack: {frc2}")

        hit2 = hit_value(frc2)
        if hit2:
            hp1 -= frc2
            print(f"Strategic Bot hits! Human Player loses HP. Human Player's HP: {hp1}")
        else:
            print("Strategic Bot missed!")

        if hp1 <= 0:
            print("Strategic Bot wins!")
            break


def start_game():
    while True:
        game_mode = menu()  
        if game_mode == 'human_vs_human':
            human_vs_human()
        elif game_mode == 'human_vs_robot':
            human_vs_robot()
        elif game_mode == 'human_vs_strategy':
            human_vs_strategy()
        else:
            continue

start_game()
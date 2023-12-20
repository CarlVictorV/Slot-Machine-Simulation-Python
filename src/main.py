from os import system , name
import classes as c

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def start(): # Start the game
    clear()
    while True:
        print("Welcome to the game of Slots!")
        print("\nYou will first deposit money into your account.")
        print("Then you will place a bet.")
        print("Then you will spin the slots.")
        print("\nDo you wanna play or read instructions?")
        print("1. Play")
        print("2. Instructions")
        choice = input("Enter your choice: ")
        if choice == "1":
            return
        elif choice == "2":
            while True:
                instructions()
                choice = input("Enter your choice: ")
                if choice == "1":
                    return
                elif choice == "2":
                    continue
                else:
                    print("Invalid choice. Try again.")
                    continue
        else:
            print("Invalid choice. Try again.")
            start()
            try:
                choice = int(input("Do you want to play or see the instructions? (1/2) "))
                if choice == 1:
                    break
                elif choice == 2:
                    instructions()
                    break
                else:
                    print("Invalid choice. Try again.")
                    continue
            except ValueError:
                print("Invalid input. Try again.")
                continue

def instructions(): # Instructions for the game
    clear()
    print("You will first deposit money into your account.")
    print("Then you will place a bet.")
    print("Then you will spin the slots.")
    print("If you get three of the same symbols, you win!")
    
    # Show Example
    print("\nExample:")
    print("🍒 🍒 🍒")
    
    # Show Payouts
    print("\nPayouts:")
    print("🍒 - 2.05x")
    print("🍋 - 2.10x")
    print("🍎 - 2.15x")
    print("🍊 - 2.20x")
    print("🍇 - 2.25x")
    print("🍉 - 2.50x")
    print("🔔 - 2.75x")
    print("7 - 3.00x")
    
    # Explain the Stats
    print("\nStats:")
    print("Balance - How much money you have")
    print("Bet - How much money you are betting")
    print("Wins - How many times you have won")
    print("Winnings - How much money you have won")
    print("Losses - How many times you have lost")
    print("Balance - How much money you have lost")
    print("Time Played - How long you have played")

    # Explain the Advanced Stats
    print("\nAdvanced Stats:")
    print("Win Percentage - How often you win")
    print("Loss Percentage - How often you lose")
    print("Average Winnings - How much money you win on average")
    print("Average Losses - How much money you lose on average")
    print("Return on investment - How much money you get back on average")
    
    print("\nDo you wanna play or quit?")
    print("1. Play")
    print("2. Quit")
    
def play():
    clear()
    while True:
        try:
            money = int(input("How much money do you want to deposit? "))
            if money <= 0:
                print("Invalid input. Try again.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input. Try again.")
            continue
    
    return money
    

def main():
    start()
    money = play()
    
    # Create objects
    player = c.player(money)
    slot_machine = c.SlotMachine(player)
    
    # Start the game
    clear()
    while (player.balance) > 0.:
        
        bet = 0
        while bet <= 0:
            try:
                bet = float(input("How much do you want to bet? "))
                if bet <= 0:
                    print("Invalid input. Try again.")
                    continue
                elif bet > player.balance:
                    print(f"Your balance is {player.balance}")
                    print("You don't have enough money to bet that much. Try again.")
                    continue
                else:
                    break
            except ValueError:
                print("Invalid input. Try again.")
                continue
        clear()
        
        slot_machine.spin(bet)
        print(f"Your balance is {player.balance}")
        
        if player.balance <= 0:
            print("You don't have any money left. Game over.")
            slot_machine.quit()
            break
        
        choice = ""
        while choice != "y" and choice != "n":
            try:
                choice = input("Do you want to play again? (y/n) ")
                if choice == "n":
                    slot_machine.quit()
                    print("Thanks for playing!")
                    break
                elif choice == "y":
                    continue
                else:
                    print("Invalid choice. Try again.")
                    continue
            except ValueError:
                print("Invalid input. Try again.")
                continue
            
        if choice == "n":
            slot_machine.quit()
            print("Thanks for playing!")
            break
        
        elif choice == "y":
            continue
        
        else:
            print("Invalid choice. Try again.")
            continue    

if __name__ == "__main__":
    main()
    
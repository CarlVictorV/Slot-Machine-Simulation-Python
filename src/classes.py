import random
import time

class player():
    def __init__(self, deposit) -> None:
        self.__deposit = deposit
        self.__bets = 0
        self.__wins = 0
        self.__loss = 0
        self.__winnings = 0
        self.__losses = 0
        self.__balance = deposit
        self.__start_time = time.time()
        self.__stop_time = time.time()         

    # Properties (getters and setters)
  
    @property
    def deposit(self):
        return self.__deposit
    
    @property
    def bets(self):
        return self.__bets
    
    @bets.setter
    def bets(self, value):
        self.__bets = value
    
    @property
    def wins(self):
        return self.__wins
    
    @wins.setter
    def wins(self, value):
        self.__wins = value
        
    @property
    def loss(self):
        return self.__loss
    
    @loss.setter
    def loss(self, value):
        self.__loss = value
    
    @property
    def losses(self):
        return self.__losses
    
    @losses.setter
    def losses(self, value):
        self.__losses = value
    
    @property
    def winnings(self):
        return self.__winnings
    
    @winnings.setter
    def winnings(self, value):
        self.__winnings = value
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        self.__balance = value

    @property
    def start_time(self):
        return self.__start_time
    
    @property
    def stop_time(self):
        return self.__stop_time

    # Methods
    def inc_bet(self):
        self.__bets += 1
    def inc_wins(self):
        self.__wins += 1
    def inc_loss(self):
        self.__loss += 1
    def inc_winnings(self, winnings):
        self.__winnings += winnings
    def inc_losses(self, losses):
        self.__losses += losses
    def inc_balance(self, balance):
        self.__balance += balance
    
    def dec_winnings(self, winnings):
        self.__winnings -= winnings
    def dec_losses(self, losses):
        self.__losses -= losses
    def dec_balance(self, balance):
        self.__balance -= balance

    def stop_session(self):
        self.__stop_time = time.time()

    def stats(self):
        if self.__stop_time is None:
            self.stop_session()  # Stop session if not already stopped

        if self.__bets > 0:
            print(f"Balance: {self.__balance}")
            print(f"Bets: {self.__bets}")
            print(f"Wins: {self.__wins}")
            print(f"Losses: {self.__loss}")
            print(f"Losses: {self.__losses}")
            print(f"Winnings: {self.__winnings}")
            print(f"Time played: {self.__stop_time - self.__start_time} seconds")

            print("Advanced stats:")
            # Percentages
            print(f"Win rate: {(self.__wins / self.__bets) * 100}%")
            print(f"Loss rate: {(self.__loss / self.__bets) * 100}%")
            
            print(f"Average winnings: {(self.__winnings / self.__bets) }")
            print(f"Average losses: {self.__losses / self.__bets}")
            print(f"Return on investment: {(self.__winnings - self.__losses) / self.__bets}")
        else:
            print("No bets placed yet.")
    
    def reset(self):
        self.__bets = 0
        self.__wins = 0
        self.__loss = 0
        self.__winnings = 0
        self.__losses = 0
        self.__balance = 0
        self.__start_time = time.time()
        self.__stop_time = time.time()


class TerminalColors:
    COLORS = {
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "reset": "\033[0m",
    }

    @classmethod
    def color(cls, text, color):
        return f"{cls.COLORS[color]}{text}{cls.COLORS['reset']}"

class SlotSymbols:
    SYMBOLS = {
        "cherry": "🍒",
        "lemon": "🍋",
        "orange": "🍊",
        "apple": "🍎",
        "grapes": "🍇",
        "watermelon": "🍉",
        "bell": "🔔",
        "seven": TerminalColors.color("7", "red"),
    }

    @classmethod
    def symbol(cls, symbol):
        return cls.SYMBOLS[symbol]

class SlotMachine:
    def __init__(self, player):
        self.__player = player
        self.__symbols = ["cherry", "lemon", "orange", "apple", "grapes", "watermelon", "bell", "seven"]
        self.__slots = [None, None, None]
        # Can convert the above to a 3x3 matrix to make it look like a slot machine
        # If so, then need to change these methods: spin, display, check, reset

    def spin(self, bet):
        self.__player.inc_bet()
        # Change logic here to make it look like a slot machine
        for i in range(len(self.__slots)):
            self.__slots[i] = random.choice(self.__symbols)
        self.display()
        self.payout(bet)
        self.reset()
    
    # Change logic here to make it look like a slot machine
    def display(self):
        for slot in self.__slots:
            print(SlotSymbols.symbol(slot), end=" ")
        print()
    
    def check(self):
        # Change logic here to make it look like a slot machine
        if self.__slots[0] == self.__slots[1] == self.__slots[2]:
            win_percentage = 2
            if self.__slots[0] == "cherry":
                win_percentage +=.05
            elif self.__slots[0] == "lemon":
                win_percentage +=.1
            elif self.__slots[0] == "orange":
                win_percentage +=.2
            elif self.__slots[0] == "apple":
                win_percentage +=.15
            elif self.__slots[0] == "grapes":
                win_percentage +=.25
            elif self.__slots[0] == "watermelon":
                win_percentage +=.50
            elif self.__slots[0] == "bell":
                win_percentage +=.75
            elif self.__slots[0] == "seven":
                win_percentage +=1
            return win_percentage
        else:
            return 0
        
    def payout(self, bet):
        check = self.check()
        if check != 0:
            self.__player.inc_wins()
            self.__player.inc_winnings(bet * check)
            self.__player.inc_balance(bet * check)
            print(f"You won {bet * check}!")
        else:
            self.__player.inc_loss()
            self.__player.inc_losses(bet)
            self.__player.dec_balance(bet)
            print(f"You lost {bet}!")

    # Change logic here to make it look like a slot machine
    def reset(self):
        self.__slots = [None, None, None]
    
    def quit(self):
        self.__player.stop_session()
        self.__player.stats()
        self.__player.reset()


def main():
    P = player(1000)
    print(P.balance)
    G = SlotMachine(player(1000))
    i = 0
    while i < 10:
        G.spin(100)
        i += 1
    G.quit()
    
if __name__ == "__main__":
    main()
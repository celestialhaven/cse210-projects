from game.hilo import Hilo


class Director:
    # global variables for the cards
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.total_score = 300
        self.cards = {}
        self.is_playing = True
        self.guess = None
        self.bet = 1

    # start game function
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.play_card()
        print("Game is Over!")
    # playing cards in display function
    def play_card(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        self.cards = Hilo()
        print(f"The card is \033[93m{self.cards.card1}\033[00m")
        
        # asking for multiplier 
        multiply = input("\033[95mDo you want to increase the bet?\033[00m [y/n]:")
        while True:
            if multiply in ["y", "n"]:
                break
            print("Wrong answer! [y,n] only:")
            multiply = input("Do you want to increase the bet? [y/n]: ")
        if multiply == "y":
            self.bet = int(input("By how much? \033[94m[1, 2, 3]\033[00m times: "))
        
        # asking for the new card if it's high or low
        self.guess = input("\033[96mIs the next card higher or lower?\033[00m \033[93m[h/l]:\033[00m ")
        print(f"The next card is \033[93m{self.cards.card2}\033[00m ")
        if self.guess == "h":
            if self.cards.card2 > self.cards.card1:
                self.total_score += 100 * self.bet
            else:
                self.total_score -= 75 * self.bet
        elif self.guess == "l":
            if self.cards.card2 < self.cards.card1:
                self.total_score += 100 * self.bet
            else:
                self.total_score -= 75 * self.bet
        # prints total score
        print(f"Your score is: \033[94m{self.total_score}\033[00m")
        
        # for play agaid and breaks when the total scoe is below 0
        self.is_playing = True if self.total_score >= 0 else False
        if not self.is_playing:
            return
        play_again = input(f"\033[92mPlay again [y/n]: \033[00m")
        while True:
            if play_again in ["y","n"]:
                break
            print("Wrong input try again")
            play_again = input("Play again [y/n]: ")
        self.is_playing = True if play_again == "y" else False
        print("")
        
        
import random
"""The card is: 9
Higher or Lower? [h/l] l
Next card was: 5
Your score is: 400
Play again? [y/n]

"""
class Hilo:
    
    def __init__(self):
        self.card1 = random.randint(1, 13)
        self.card2 = random.randint(1, 13)
        while True:
            if self.card1 != self.card2:
                break
            self.card2 = random.randint(1, 13)
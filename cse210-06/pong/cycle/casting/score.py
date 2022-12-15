from game.casting.actor import Actor
from game.shared.point import Point
import constants


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self, color):
        super().__init__()
        self._cycle_color = color
        self._points = 0
        self.add_points(0)
        if self._cycle_color == constants.GREEN:
            x = int(constants.MAX_X) - 120
            y = 0
            self.set_position(Point(x, y))

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        if self._cycle_color == constants.GREEN:
            self.set_text(f"Green Score: {self._points}")
        else:
            self.set_text(f"RED Score: {self._points}")
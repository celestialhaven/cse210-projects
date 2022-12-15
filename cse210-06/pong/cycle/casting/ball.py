import random
from time import sleep
import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Ball(Actor):
    """
    A tasty item that snakes like to eat.
    
    The responsibility of Food is to select a random position and points that it's worth.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        "Constructs a new Food."
        super().__init__()
        self.set_text("O")
        self.set_color(constants.WHITE)
        self.reset()
        
    def reset(self):
        """Selects a random position and points that the food is worth."""
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)
        position = Point(x, y)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        x_sign = -1 if random.randint(0, 1) == 1 else 1
        y_sign = -1 if random.randint(0, 1) == 1 else 1
        velocity = Point(x_sign * constants.CELL_SIZE, y_sign * constants.CELL_SIZE)
        self.set_position(position)
        self.set_velocity(velocity)

    def move_ball_next(self):
        """Moves the actor to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        
        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        x = (self._position.get_x() + self._velocity.get_x()) % constants.MAX_X
        y = (self._position.get_y() + self._velocity.get_y()) % constants.MAX_Y
        if not x == 0 and not x > constants.MAX_X - 25:
            self._position = Point(x, y)
        else:
            self.set_velocity(self.get_velocity().reverse_x())
        
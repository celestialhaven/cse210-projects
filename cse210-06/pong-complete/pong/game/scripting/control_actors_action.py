import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)
        self._direction2 = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        snake = cast.get_first_actor("cycles")
        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)
            snake.turn_head(self._direction)
            snake.move_next()
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)
            snake.turn_head(self._direction)
            snake.move_next()
        
        # # up
        # if self._keyboard_service.is_key_down('w'):
        #     self._direction = Point(0, -constants.CELL_SIZE)
        
        # # down
        # if self._keyboard_service.is_key_down('s'):
        #     self._direction = Point(0, constants.CELL_SIZE)
    
        
        snake2 = cast.get_second_actor("cycles")

        # left
        if self._keyboard_service.is_key_down('j'):
            self._direction2 = Point(-constants.CELL_SIZE, 0)
            snake2.turn_head(self._direction2)
            snake2.move_next()
        
        # right
        if self._keyboard_service.is_key_down('l'):
            self._direction2 = Point(constants.CELL_SIZE, 0)
            snake2.turn_head(self._direction2)
            snake2.move_next()
        
        # up
        # if self._keyboard_service.is_key_down('i'):
        #     self._direction2 = Point(0, -constants.CELL_SIZE)
        
        # # down
        # if self._keyboard_service.is_key_down('k'):
        #     self._direction2 = Point(0, constants.CELL_SIZE)
        


        food = cast.get_first_actor("foods")

        if self._keyboard_service.is_key_down('w'):
            food.jump()

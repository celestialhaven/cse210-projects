import constants
import random
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._message = ''

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            # self._handle_food_collision(cast)
            # self._handle_segment_collision(cast)
            self._handle_game_over(cast)
            self._handle_ball_collision(cast)

    def _handle_ball_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score = cast.get_first_actor("scores")
        score2 = cast.get_second_actor("scores")

        ball = cast.get_first_actor("ball")
        snake = cast.get_first_actor("cycles").get_segments()[0]
        snake2 = cast.get_second_actor("cycles").get_segments()[0]

        snake_pos_x = snake.get_position().get_x()
        snake_pos_y = snake.get_position().get_y()
        if snake.get_position().equals(ball.get_position()) or (ball.get_position().get_x() in range(snake_pos_x, snake_pos_x + 135) and ball.get_position().get_y() == snake_pos_y):
            ball.set_velocity(ball.get_velocity().reverse_y())

        snake2_pos_x = snake2.get_position().get_x()
        snake2_pos_y = snake2.get_position().get_y()
        if snake2.get_position().equals(ball.get_position()) or (ball.get_position().get_x() in range(snake2_pos_x, snake2_pos_x + 135) and ball.get_position().get_y() == snake2_pos_y):
            ball.set_velocity(ball.get_velocity().reverse_y())

        if ball.get_position().get_y() <= 20: 
            ball.reset()
            score2.add_points(1)
        elif ball.get_position().get_y() >= constants.MAX_Y - 20:
            ball.reset()
            score.add_points(1)

    def _handle_food_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        pass
    
        score = cast.get_first_actor("scores")
        score2 = cast.get_second_actor("scores")
        foods = cast.get_actors("foods")
        snake = cast.get_first_actor("cycles")
        head = snake.get_head()

        snake2 = cast.get_second_actor("cycles")
        head2 = snake2.get_head()

        for food in foods:
            if head.get_position().equals(food.get_position()):
                points = food.get_points()
                snake.remove_tail(points)
                score.add_points(points)
                food.reset()

            if head2.get_position().equals(food.get_position()):
                points = food.get_points()
                snake2.grow_tail(points)
                score2.add_points(points)
                food.reset()

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        
        snake = cast.get_first_actor("cycles")
        head = snake.get_segments()[0]
        segments = snake.get_segments()[1:]
        
        snake2 = cast.get_second_actor("cycles")
        head2 = snake2.get_segments()[0]
        segments2 = snake2.get_segments()[1:]

        for segment in segments2:
            if head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._message = "Green is the Winner!"

        for segment in segments:
            if head2.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._message = "RED is the Winner!"
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            cycles = cast.get_actors("cycles")
            cycles[0]._cycle_color = constants.WHITE
            cycles[1]._cycle_color = constants.WHITE
            segments = cycles[0].get_segments() + cycles[1].get_segments()
            foods = cast.get_actors("foods")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text(self._message)
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)
            for food in foods:
                cast.remove_actor("foods", food)
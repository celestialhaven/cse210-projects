from game.scripting.action import Action
import random
import constants


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score = cast.get_first_actor("scores")
        food = cast.get_first_actor("foods")
        snake = cast.get_first_actor("cycles")
        segments = snake.get_segments()

        score2 = cast.get_second_actor("scores")
        # food = cast.get_second_actor("foods")
        snake2 = cast.get_second_actor("cycles")
        segments2 = snake2.get_segments()

        if not (snake.is_cycle_dead() or snake2.is_cycle_dead()) and random.randint(1, 4) == 4:
            # snake.grow_tail(1)
            # snake2.grow_tail(1)
            pass

        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actor(food)
        self._video_service.draw_actors(segments)
        self._video_service.draw_actors(segments2)
        self._video_service.draw_actor(score)
        self._video_service.draw_actor(score2)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()
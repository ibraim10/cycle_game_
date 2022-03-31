from turtle import update
import constants
from game.scripting.script import Script
from game.scripting.grow import Grow
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.score import Score
from game.services.keyboard_service import KeyboardService
from game.casting.cast import Cast
from game.casting.snake import Snake

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

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast, script)

    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snake = cast.get_first_actor("snakes")
        player2=cast.get_first_actor("player2")
        head = snake.get_segments()[0]
        head2= player2.get_segments()[0]
        segments = snake.get_segments()[1:]
        segments2 =player2.get_segments()[1:]
        score1=cast.get_first_actor("scores")
        score2=cast.get_first_actor("score2")
        # for segment in segments:
        #     if head.get_position().equals(segment.get_position()):
        #         self._is_game_over = True
        #         score2.add_points(1)
        #         snake.clear_segments()
        #         snake._prepare_body()
        #         player2.clear_segments()
        #         player2._prepare_body()
                
        for segment in segments:
            if head2.get_position().equals(segment.get_position()):
                self._is_game_over = True
                score1.add_points(1,'one')
                snake.clear_segments()
                snake._prepare_body(int(constants.MAX_X / 4),int(constants.MAX_Y / 2))
                player2.clear_segments()
                player2._prepare_body(int(constants.MAX_X / 2)+int(constants.MAX_X / 4),int(constants.MAX_Y / 2))
                
        for segment in segments2:
        #     if head2.get_position().equals(segment.get_position()):
        #         self._is_game_over = True
        #         score1.add_points(1)
        #         snake.clear_segments()
        #         snake._prepare_body()
        #         player2.clear_segments()
        #         player2._prepare_body()
                
            if head.get_position().equals(segment.get_position()):
                self._is_game_over = True 
                score2.add_points(1,'two')
                snake.clear_segments()
                snake._prepare_body(int(constants.MAX_X / 4),int(constants.MAX_Y / 2))
                player2.clear_segments()
                player2._prepare_body(int(constants.MAX_X / 2)+int(constants.MAX_X / 4),int(constants.MAX_Y / 2))
                    

    def _handle_game_over(self, cast, script):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            snake = cast.get_first_actor("snakes")
            player2=cast.get_first_actor("player2")
            segments = snake.get_segments()
            segments2= player2.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)
            script.remove_action ("update", script.get_actions ("update")[2] ) 
            
            """makes the color of the snakes white"""
            for segment in segments:
                segment.set_color(constants.WHITE)
            for segment in segments2:
                segment.set_color(constants.WHITE)
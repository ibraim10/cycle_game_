from pickle import TRUE
from game.scripting.action import Action
import constants

class Grow(Action):

    def __init__(self):
        self._add=True

    def execute(self, cast, script):
        """gets the two players"""
        snake = cast.get_first_actor("snakes")
        player2 = cast.get_first_actor("player2")
        """makes the tails grow in their respective colors (if the game
        is still going)"""
        if self._add:
            snake.grow_tail(1,constants.GREEN)
            player2.grow_tail(1,constants.BLUE)
            self._add=False
        else:
            self._add=True
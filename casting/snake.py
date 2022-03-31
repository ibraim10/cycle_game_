import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Snake(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self,x,y):
        """calls the '__init__()' method of the super class (Actor)
        builds the segment list
        builds the snake by calling the 'prepare_body()' method"""
        super().__init__()
        self._segments = []
        self._prepare_body(x,y)

    def get_segments(self):
        """gets the segments of the snake"""
        return self._segments

    def move_next(self):
        """moves the segments of the snake to the input direction 
        at the set velocity"""
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        """determines which index will be the head of the snake"""
        return self._segments[0]

    def grow_tail(self, number_of_segments, color):
        """grows the snake's tail by adding segments"""
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(color)
            self._segments.append(segment)

    def turn_head(self, velocity):
        """moves the head towards the input direction at the set speed"""
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self,x,y):
        """builds the snake's body for the game to start"""
        # x = int(constants.MAX_X / 4)
        # y = int(constants.MAX_Y / 2)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            if x==int(constants.MAX_X / 4):
                color = constants.YELLOW if i == 0 else constants.GREEN
            else:
                color = constants.YELLOW if i == 0 else constants.BLUE
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)
    def clear_segments(self):
        """clears all segments from its list"""
        self._segments.clear()
import random
from constants import *


class Food:
    def __init__(self, pos: tuple[int, int] = None):
        """
        :param pos: defaults to random
        """
        if pos is None:
            self.pos = (random.randint(0, GRID_SIZE[0]), random.randint(0, GRID_SIZE[1]))
        else:
            self.pos = pos
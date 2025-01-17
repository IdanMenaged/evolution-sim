import random

from constants import GRID_SIZE, TILE_SIZE
from simulation.food import Food


class Animal:
    def __init__(self, pos: tuple[int, int] = None, sight_range: int = 1):
        """
        :param pos: defaults to random
        :param sight_range: range of sight, works as a rectangle that extends <sight_range> tiles to the right
        and <sight_range> tiles upwards
        """
        if pos is None:
            self.pos = (random.randint(0, GRID_SIZE[0]), random.randint(0, GRID_SIZE[1]))
        else:
            self.pos = pos

        self.sight_range = sight_range

    def look(self, objects: set):
        """
        what objects are in range of sight?
        :param objects: all objects in the world
        :return: objects that are in range
        """
        can_see = set()
        for obj in objects:
            if abs(self.pos[0] - obj.pos[0]) <= self.sight_range and abs(self.pos[1] - obj.pos[1]) <= self.sight_range:
                can_see.add(obj)
        return can_see

    def move(self, target: tuple[int, int], step_size: int = 1):
        """
        take a single step towards a target
        :param target: target location
        :param step_size: how many tiles at a time? default 1
        :return: None
        """
        # Unpack the current and target positions (assuming 2D grid)
        x1, y1 = self.pos
        x2, y2 = target

        # Calculate the differences between the current position and target position
        dx = x2 - x1
        dy = y2 - y1

        # Move only horizontally or vertically, depending on which axis has the greater difference
        if abs(dx) > abs(dy):
            # Move horizontally
            if dx > 0:
                new_x = x1 + step_size
            elif dx < 0:
                new_x = x1 - step_size
            else:
                new_x = x1
            new_y = y1  # No change in y position
        else:
            # Move vertically
            if dy > 0:
                new_y = y1 + step_size
            elif dy < 0:
                new_y = y1 - step_size
            else:
                new_y = y1
            new_x = x1  # No change in x position

        # Ensure the new position doesn't overshoot the target (if step_size is too large)
        if abs(new_x - x2) < step_size:
            new_x = x2
        if abs(new_y - y2) < step_size:
            new_y = y2

        # Print and return the new position
        self.pos = (new_x, new_y)

    def determine_target(self, objects_in_range: set):
        """
        decide where to go (towards closest food. if there's no food than explore)
        :param objects_in_range: can be obtained with self.look()
        :return: coords to go to
        """
        # is there food?
        foods = set()
        for obj in objects_in_range:
            if obj is Food:
                foods.add(obj)

        if not bool(foods):
            return random.randint(0, GRID_SIZE[0]), random.randint(0, GRID_SIZE[1])
        else:
            return self.find_closest_food()

    def find_closest_food(self):
        # todo: implement
        pass

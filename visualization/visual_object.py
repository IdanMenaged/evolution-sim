import pyglet

from constants import *

class VisualObject(pyglet.shapes.Rectangle):
    def __init__(self, sim_obj, color: tuple[int, int, int] = (255, 255, 255)):
        super().__init__(sim_obj.pos[0] * TILE_SIZE, sim_obj.pos[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE, color=color)
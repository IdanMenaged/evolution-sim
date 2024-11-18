import time

import pyglet.window

from constants import GRID_SIZE, TILE_SIZE
from simulation.animal import Animal
from simulation.food import Food
from visualization.visual_object import VisualObject

window = pyglet.window.Window(GRID_SIZE[0] * TILE_SIZE, GRID_SIZE[1] * TILE_SIZE)

food_sim = Food((0, 0))
animal = Animal((1, 1))


@window.event
def on_draw():
    window.clear()
    VisualObject(food_sim, color=(255, 0, 0)).draw()
    VisualObject(animal).draw()

    time.sleep(.5)
    animal.move((3, 1), 1)

pyglet.app.run()
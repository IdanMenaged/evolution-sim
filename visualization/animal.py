import pyglet.shapes

from constants import TILE_SIZE, FOV_COLOR
from simulation.animal import Animal
from visualization.visual_object import VisualObject


class AnimalVO(VisualObject):
    def __init__(self, animal_sim: Animal, show_fov: bool = False):
        """
        :param animal_sim: Animal object
        :param show_fov: should program visualize fov?
        """
        super().__init__(animal_sim)

        if show_fov:
            fov = set()
            for x in range(animal_sim.pos[0] - animal_sim.sight_range, animal_sim.pos[0] + animal_sim.sight_range + 1):
                    for y in range(animal_sim.pos[1] - animal_sim.sight_range, animal_sim.pos[1] + animal_sim.sight_range + 1):
                        # Skip the center tile (animal_sim.pos[0], animal_sim.pos[1])
                        if x == animal_sim.pos[0] and y == animal_sim.pos[1]:
                            continue
                        fov.add((x, y))

            # translating the grid tiles to pyglet objects
            fov_objects = set()
            for x, y in fov:
                fov_objects.add(pyglet.shapes.Rectangle(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE,
                                                        color=FOV_COLOR))

            self.fov = fov_objects
        else:
            self.fov = set()

    def draw(self) -> None:
        """
        draw self + fov if needed
        :return: None
        """
        super().draw()
        for rect in self.fov:
            rect.draw()
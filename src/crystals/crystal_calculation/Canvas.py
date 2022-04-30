import numpy as np
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from crystal_calculation.Crystal import Crystal
class Canvas:
    def __init__(self, crystal: "Crystal", radius: int):
        start = crystal.inject_circle()
        self.pos = np.array([start[0], start[1]])
        # TODO: pixels out of the crystal class or crystal created within the canvas
        # TODO: make canvas a dataclass?
        self.canvas = np.zeros(shape=(crystal.pixels, crystal.pixels))
        self.canvas[crystal.mid_point, crystal.mid_point] = 1 # Sets the seed
        
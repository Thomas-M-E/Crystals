import random
from typing import Tuple

import numpy as np


class Crystal:
    """
    Class for a crystal and it's growth
    """

    def __init__(self):
        self.pixels = 255
        self.mid_point = int((self.pixels - 1) / 2)
        self.inject_radius = 3
        self.num_of_injections = 10000
        self.crystal_loc = [(self.mid_point, self.mid_point)]

    def inject_circle(self) -> Tuple[int, int]:
        """This injects particles inwards from a circle"""
        theta = random.random() * 2 * np.pi
        r = self.inject_radius
        x, y = (r * np.cos(theta) + self.mid_point, r * np.sin(theta) + self.mid_point)
        # return integers as they have to be on the pixel grid
        return int(x), int(y)

    def update_radius(self) -> int:
        """
        Updates the radius of the injection and kill circles if the
        crystal is getting too close to them
        """
        return int(np.ceil(self.inject_radius + 2))

    @staticmethod
    def norm(x, y) -> float:
        return np.sqrt(x ** 2 + y ** 2)

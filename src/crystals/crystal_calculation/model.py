from dataclasses import dataclass
import numpy as np
import random
from typing import Tuple
import logzero

LOGGER = logzero()

class InjectionCircle:
    def __init__(self, inject_radius: int, origin: Tuple[int, int]):
        self.inject_radius = inject_radius
        self.origin = origin

    def inject_particle(self) -> Tuple[int, int]:
        """Injects a particle from a random location on the circle

        Returns:
            Tuple[int, int]: origin of the particle injected
        """
        theta = 2 * np.pi * random.random()
        x = self.inject_radius * np.cos(theta) + self.origin[0]
        y = self.inject_radius * np.sin(theta) + self.origin[1]
        # return integers as they have to be on the pixel grid
        return int(x), int(y)

    def update_radius(self):
        """ Updates the radius of the injection and kill circles if the
            crystal is getting too close to them"""
        self.inject_radius = int(np.ceil(self.inject_radius + 2))

    @staticmethod
    def norm(x,y): 
        return np.sqrt(x**2 + y**2)

@dataclass
class Canvas:
    pixels: int
    canvas: 'np.array'

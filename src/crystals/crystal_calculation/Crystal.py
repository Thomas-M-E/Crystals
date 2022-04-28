import numpy as np
import random
from typing import Tuple
import logging

# TODO: set up a canvas class for storing the info of the crystal
# TODO: finish the run() method

class Crystal:
    """ Class for a crystal and it's growth
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
        x, y = (r*np.cos(theta) + self.mid_point, r*np.sin(theta) + self.mid_point)
        # return integers as they have to be on the pixel grid
        return int(x), int(y)

    def update_radius(self):
        """ Updates the radius of the injection and kill circles if the
            crystal is getting too close to them"""
        return int(np.ceil(self.inject_radius + 2))

    @staticmethod
    def norm(x, y): 
        return np.sqrt(x**2 + y**2)

class Canvas:
    def __init__(self, crystal: "Crystal", radius: int):
        start = crystal.inject_circle()
        self.pos = np.array([start[0], start[1]])
        # TODO: pixels out of the crystal class or crystal created within the canvas
        # TODO: make canvas a dataclass?
        self.canvas = np.zeros(shape=(crystal.pixels, crystal.pixels))
        self.canvas[crystal.mid_point, crystal.mid_point] = 1 # Sets the seed
        
def run():
    c = Crystal()
    can = Canvas(crystal=c, radius=3)
    __DIR_CHOICE = np.array([[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]])
    __CLUSTERS = 10
    for b in range(__CLUSTERS):
        killcount  = 0
        INJECT = True
        count = 0

        while(INJECT):
            count = count + 1 # Counts the number of injections
            WALK = True
            while(WALK):
                for step in range(8): # Checks the neighbour sites of the particle position to check if any are in the crystal
                    adjacent = can.pos + __DIR_CHOICE[step,]
                    if(can.canvas[adjacent[0], adjacent[1]] == 1):
                        can.canvas[can.pos[0], can.pos[1]] = 1 # Adds the position to the crystal if it is neighbouring the crystal
                        c.crystal_loc.append([can.pos[0], can.pos[1]]) 
                        size = np.sqrt((can.pos[0] - c.mid_point)**2 + (can.pos[1] - c.mid_point)**2)
                        # Calculates how far from the centre the new particle on the edge of the crystal is
                        if(size > c.inject_radius - 1): # Checks if the crystal is too close to the injection circle
                            c.inject_radius = c.update_radius() # Increases the size of the injection circle
                            if(c.inject_radius >= (c.pixels - 1 - c.mid_point)): # Ends the process if the crystal is too close to the edge
                                logging.info("Edge Reached")
                                INJECT = False
                        WALK = False
                        continue
                
                __DIREC = random.choice([0, 1, 2, 3, 4, 5, 6, 7])
                # Steps for the random walk
                can.pos[0] = can.pos[0] + __DIR_CHOICE[__DIREC,][0]
                can.pos[1] = can.pos[1] + __DIR_CHOICE[__DIREC,][1]

                #### Kills on the edge ####
                if(can.pos[0] in {c.pixels - 1, 0} or can.pos[1] in {c.pixels-1, 0}):
                    WALK = False
                #### Kill Circle ####
                if(np.linalg.norm(can.pos - np.array([c.mid_point, c.mid_point])) > c.inject_radius + 5):
                    killcount = killcount + 1
                    WALK = False   # Breaks the loop for this random walk if it goes out
                                   # of bounds
            if(count > c.num_of_injections):
                logging.info("Injections completed")
                INJECT = False # Ends the process if all the particles have been injected for this crystal
        L = 20
        area = np.zeros(L)
        rseq = 5 * list(range(L))
        for k in range(L):
            for l in range(len(c.crystal_loc)):    
                if(c.norm(c.crystal_loc[l][0]- c.mid_point, c.crystal_loc[l][1] - c.mid_point) < rseq[k]):
                    area[k] = area[k] + 1 # Counts the number of occupied sites within radius rseq[k]
                    # sums all the numbers of occupied sites for each crystal
                    
    average_area = sum(area) / CLUSTERS # Averages the sums
    end_time = time.time()
    logging.info('Elapsed time = ', repr(end_time - start_time))

if __name__ == "__main__":
    run()
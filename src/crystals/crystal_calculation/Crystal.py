import numpy as np
import random
from typing import Tuple

# TODO: set up a canvas class for storing the info of the crystal
# TODO: finish the run() method

__DIR_CHOICE = np.array([[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]])

class Crystal:
    """ Class for a crystal and it's growth
    """
    def __init__(self):
        self.pixels = 255
        self.mid_point = int(self.pixels - 1) / 2
        self.inject_radius = 3
        self.num_of_injections = 10000
        self.crystal_loc = [c.mid_point,c.mid_point]

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
        self.inject_radius = int(np.ceil(self.inject_radius + 2))

    @staticmethod
    def norm(x,y): 
        return np.sqrt(x**2 + y**2)

class Canvas:
    def __init__(self, crystal: "Crystal", radius: int):
        start = crystal.inject_circle(r, crystal.mid_point)
        self.pos = np.array([start[0], start[1]])
        # TODO: pixels out of the crystal class or crystal created within the canvas
        # TODO: make canvas a dataclass?
        self.canvas = np.zeros(shape(c.pixels, c.pixels))
        self.canvas[c.mid_point,c.mid_point] = 1 # Sets the seed
        
def run():
    c = Crystal()
    can = Canvas(crystal=c, radius=3)
    CLUSTERS = 10
    for b in range(CLUSTERS):
        killcount  = 0
        INJECT = True
        count = 0

        while(INJECT):
            count = count + 1 # Counts the number of injections
            WALK = True
            while(WALK):
                for i in range(8): # Checks the neighbour sites of the particle position to check if any are in the crystal
                    adjacent = can.pos + __DIR_CHOICE[i,]
                    if(s[adjacent[0], adjacent[1]]==1):
                        can.canvas[pos[0], can.pos[1]] = 1 #Adds the position to the crystal if it is neighbouring the crystal
                        c.crystal_loc.append([can.pos[0], can.pos[1]]) 
                        size = np.sqrt((can.pos[0] - c.mid_point)**2 + (pos[1]-c.mid_point)**2)
                        # Calculates how far from the centre the new particle on the edge of the crystal is
                        if(size > radius - 1):# Checks if the crystal is too close to the injection circle
                            radius = updateRadius(size) # Increases the size of the injection circle
                            if(radius >= (N - 1 - c.mid_point)):# Ends the process if the crystal is too close to the edge
                                print("Edge Reached")
                                INJECT = False

                        WALK = False
                        continue
                    
                __DIREC = random.choice([0, 1, 2, 3, 4, 5, 6, 7])
                # Steps for the random walk
                pos[0] = pos[0] + __DIR_CHOICE[__DIREC,][0]
                pos[1] = pos[1] + __DIR_CHOICE[__DIREC,][1]

                #### Kills on the edge ####
                if(pos[0] in {N-1, 0} or pos[1] in {N-1, 0}):
                    WALK = False
                #### Kill Circle ####
                if(np.linalg.norm(pos - np.array([c.mid_point, c.mid_point])) > radius+5):
                    killcount = killcount + 1
                    WALK = False   #Breaks the loop for this random walk if it goes out
                                    #of bounds
            if(count > injections):
                print("Injections completed")
                INJECT = False #Ends the process if all the particles have been injected for this crystal
            
        q = len(c.crystal_list)
        area = np.zeros(L)
        for k in range(L):
            for l in range(q):    
                if(c.norm(crystalList[l][0]- c.mid_point, crystalList[l][1] - c.mid_point) < rseq[k]):
                    area[k] = area[k]+1 #Counts the number of occupied sites within radius rseq[k]
                
                
        averageArea = averageArea + area #sums all the numbers of occupied sites for each crystal

    averageArea = averageArea/clusters #Averages the sums
    end_time=time.time()
    print('Elapsed time = ',repr(end_time-start_time))

if __name__ == __main__:
    run()
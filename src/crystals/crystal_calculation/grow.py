from dataclasses import dataclass
import numpy as np
import random
from typing import Tuple
import logzero
import crystals.crystal_calculation.model as model

logging = logzero()

def walk():
    pass

def grow(pixels: int, radius, origin, ):
    circle = InjectionCircle(radius, origin)
    can = model.Canvas(pixels=pixels, canvas=np.zeros(shape=(pixels, pixels)))
    for injection in circle.injections:
        # Counts the number of injections
        count = count + 1 
        WALK = True
        while(WALK):
            # Checks the neighbour sites of the particle position to check if any are in the crystal
            for i in range(8): 
                adjacent = can.pos + __DIR_CHOICE[i,]
                if(s[adjacent[0], adjacent[1]]==1):
                    can.canvas[can.pos[0], can.pos[1]] = 1 #Adds the position to the crystal if it is neighbouring the crystal
                    c.crystal_loc.append([can.pos[0], can.pos[1]]) 
                    size = np.sqrt((can.pos[0] - c.mid_point)**2 + (pos[1]-c.mid_point)**2)
                    # Calculates how far from the centre the new particle on the edge of the crystal is
                    if(size > c.inject_radius - 1):# Checks if the crystal is too close to the injection circle
                        c.inject_radius = c.update_radius(size) # Increases the size of the injection circle
                        if(c.inject_radius >= (c.pixels - 1 - c.mid_point)):# Ends the process if the crystal is too close to the edge
                            logging.info("Edge Reached")
                            INJECT = False

                    WALK = False
                    continue
                
            __DIREC = random.choice([0, 1, 2, 3, 4, 5, 6, 7])
            # Steps for the random walk
            can.pos[0] = can.pos[0] + __DIR_CHOICE[__DIREC,][0]
            can.pos[1] = can.pos[1] + __DIR_CHOICE[__DIREC,][1]

            #### Kills on the edge ####
            if(can.pos[0] in {N-1, 0} or can.pos[1] in {N-1, 0}):
                WALK = False
            #### Kill Circle ####
            if(np.linalg.norm(can.pos - np.array([c.mid_point, c.mid_point])) > radius + 5):
                killcount = killcount + 1
                WALK = False   # Breaks the loop for this random walk if it goes out
                                #of bounds
        if(count > injections):
            logging.info("Injections completed")
            INJECT = False # Ends the process if all the particles have been injected for this crystal
        
    q = len(c.crystal_list)
    area = np.zeros(L)
    for k in range(L):
        for l in range(q):    
            if(c.norm(c.cryatal_list[l][0]- c.mid_point, c.cryatal_list[l][1] - c.mid_point) < rseq[k]):
                area[k] = area[k]+1 # Counts the number of occupied sites within radius rseq[k]
            
            
    averageArea = averageArea + area # sums all the numbers of occupied sites for each crystal

averageArea = averageArea/clusters # Averages the sums
end_time = time.time()
print('Elapsed time = ', repr(end_time - start_time))

if __name__ == "__main__":
    grow()
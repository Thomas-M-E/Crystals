from dataclasses import dataclass
import numpy as np
import random
import logzero
import crystal_calculation.model as model

logging = logzero()

__DIR_CHOICE = ((1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1))

def grow(canvas: model.Canvas, circle: model.InjectionCircle, crystal: model.Crystal) -> :
    # Checks the neighbour sites of the particle position to check if
    # any are in the crystal
    pos = circle.inject_particle()
    for i in __DIR_CHOICE:
        adjacent = pos + i
        if(canvas.canvas[adjacent[0], adjacent[1]] == 1):
            # Adds the position to the crystal if it is neighbouring 
            # the crystal
            canvas.canvas[pos[0], pos[1]] = 1
            circle.crystal_loc.append([pos[0], pos[1]])

def check_size():
    size = canvas.calc_crystal_radius(pos)
    # Checks if the crystal is too close to the injection circle
    if(size > circle.inject_radius - 1):
        # Increases the size of the injection circle
        circle.inject_radius = circle.update_radius(size)

        # Ends the process if the crystal is too close to the edge
        if(circle.inject_radius >= (circle.pixels - 1 - circle.mid_point)):
            logging.info("Edge Reached")
            return False

def walk():
    __DIREC = random.choice([0, 1, 2, 3, 4, 5, 6, 7])

    # Steps for the random walk
    pos = pos + __DIR_CHOICE[__DIREC]

    #### Kills on the edge ####
    if(pos[0] in {canvas.pixels - 1, 0} or pos[1] in {canvas.pixels - 1, 0}):
        WALK = False

    #### Kill Circle ####
    if(np.linalg.norm(pos - np.array([canvas.mid_point, canvas.mid_point])) > circle.inject_radius + 5):
        killcount = killcount + 1
        WALK = False   # Breaks the loop for this random walk if it goes out
                        # of bounds


    q = len(c.crystal_list)
    area = np.zeros(L)
    for k in range(L):
        for l in range(q):    
            if(c.norm(c.cryatal_list[l][0]- c.mid_point, c.crystal_list[l][1] - c.mid_point) < rseq[k]):
                area[k] = area[k]+1 # Counts the number of occupied sites within radius rseq[k]
            
            
    averageArea = averageArea + area # sums all the numbers of occupied sites for each crystal

averageArea = averageArea/clusters # Averages the sums
end_time = time.time()
print('Elapsed time = ', repr(end_time - start_time))

if __name__ == "__main__":
    grow()
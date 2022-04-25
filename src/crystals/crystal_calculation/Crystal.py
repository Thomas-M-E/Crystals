import numpy as np
import random
from typing import Tuple

# TODO: set up a canvas class for storing the info of the crystal
# TODO: finish the run() method


class Crystal:
    """ Class for a crystal and it's growth
    """
    def __init__(self):
        self.pixels = 255
        self.mid_point = int(self.pixels - 1) / 2
        self.inject_radius = 3
        self.num_of_injections = 10000
        self.clusters = 10

    def inject_circle(self, r:float) -> Tuple[int, int]:
        """This injects particles inwards from a circle"""
        theta = random.random() * 2 * np.pi
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
    
def run():
    c = Crystal()
    for b in range(clusters):
        s = np.zeros(shape=(N,N)) #creates the area the crystal can grow on
        s[mid,mid] = 1 #Sets the seed
        killcount  = 0
        radius = 3 #Sets the injection circle near the seed
        INJECT = True
        count = 0
        crystalList = [] #Stores all the locations of occupied sites in the lattice
        crystalList.append([mid,mid]) #Adds the seed to the list
        dirChoice = np.array([[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]])

        while(INJECT):
            count = count + 1 # Counts the number of injections
            start = circle(radius,mid)
            pos = np.array([start[0],start[1]]) # Sets the initial particle location for random walk

            # dirChoice sets the possible steps of the random walk
            WALK = True
            while(WALK):
                for i in range(8): #Checks the neighbour sites of the particle position to check if any are in the crystal
                    adjacent = pos+dirChoice[i,]

                    if(s[adjacent[0],adjacent[1]]==1):
                        s[pos[0],pos[1]] = 1 #Adds the position to the crystal if it is neighbouring the crystal
                        crystalList.append([pos[0],pos[1]]) 
                        size = np.sqrt((pos[0]-mid)**2+(pos[1]-mid)**2)
                        #Calculates how far from the centre the new particle on the edge of the crystal is
                        if(size>radius-1):#Checks if the crystal is too close to the injection circle
                            radius = updateRadius(size) #Increases the size of the injection circle
                            if(radius>=(N-1-mid)):#Ends the process if the crystal is too close to the edge
                                print("Edge Reached")
                                WALK = False
                                INJECT = False

                        WALK = False #Ends the while loop

                        break #breaks for loop
                direc = random.choice([0,1,2,3,4,5,6,7])
                #Steps for the random walk
                pos[0] = pos[0] + dirChoice[direc,][0]
                pos[1] = pos[1] + dirChoice[direc,][1]

                #### Kills on the edge ####
                if(pos[0]==N-1 or pos[1]==N-1 or pos[0]==0 or pos[1]==0):
                    WALK = False #breaks while
                #### Kill Circle ####
                if(np.linalg.norm(pos - np.array([c.mid_, mid])) > radius+5):
                    killcount = killcount + 1
                    WALK = False   #Breaks the loop for this random walk if it goes out
                                    #of bounds
            if(count > injections):
                print("Injections completed")
                INJECT = False #Ends the process if all the particles have been injected for this crystal
            
        q = len(crystalList)
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
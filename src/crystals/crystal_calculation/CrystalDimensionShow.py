# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 17:05:31 2020

@author: Thomas Everard
"""
import numpy as np
import random
import matplotlib.pyplot as plt
import time
from scipy import stats
'''This code calculates the fractal dimension of crystals grown via a random walk
sticking process. First it creates the crystals then it measures the area covered by
crystal in circles of increasing radius. These values are averaged over multiple
crystals and plotted. The fractal dimension is taken to be the gradient of this
line in the middle section as this is the most accurate part.'''



start_time=time.time()
#### Injection Circle ####
#Injects particles in a random walk towards the seed
def circle(r,mid):
    theta = random.random() * 2 * np.pi
    x = r*np.cos(theta)+mid
    y = r*np.sin(theta)+mid
    return [int(x),int(y)]

def updateRadius(size): 
#updates the radius of the injection and kill circles if the
# crystal is getting too close to them
    newRadius = int(np.ceil(size+2))
    return newRadius
def norm(x,y): #Needed to get norm of a list
    EuclidNorm = np.sqrt(x**2+y**2)
    return EuclidNorm

N = 255 #sets the size of the area the crystal can grow in
mid = int((N-1)/2) #finds the midpoint to set the seed
injections = 10000
rseq = np.linspace(0.5,127.5,128) #Sequence of radii
L = len(rseq)
averageArea = np.zeros(L)


'''Number of clusters can be lowered to greatly increase computation speed'''
'''Number used for the project plots is 25'''
clusters = 10


for b in range(clusters):
    s = np.zeros(shape=(N,N)) #creates the area the crystal can grow on
    s[mid,mid] = 1 #Sets the seed
    killcount  = 0
    radius = 3 #Sets the injection circle near the seed
    INJECT = True
    count = 0
    crystalList = [] #Stores all the locations of occupied sites in the lattice
    crystalList.append([mid,mid]) #Adds the seed to the list
    
    while(INJECT):
        count = count + 1 #Counts the number of injections
        start = circle(radius,mid)
        pos = np.array([start[0],start[1]]) #Sets the initial particle location for random walk

        dirChoice = np.array([[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]])
        #dirChoice sets the possible steps of the random walk
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
            if(np.linalg.norm(pos - np.array([mid,mid]))>radius+5):
                killcount = killcount + 1
                WALK = False   #Breaks the loop for this random walk if it goes out
                                #of bounds
        if(count>injections):
            print("Injections completed")
            INJECT = False #Ends the process if all the particles have been injected for this crystal
        
    q = len(crystalList)
    area = np.zeros(L)
    for k in range(L):
        for l in range(q):    
            if(norm(crystalList[l][0]-mid,crystalList[l][1]-mid)<rseq[k]):
                area[k] = area[k]+1 #Counts the number of occupied sites within radius rseq[k]
            
            
    averageArea = averageArea + area #sums all the numbers of occupied sites for each crystal

averageArea = averageArea/clusters #Averages the sums
end_time=time.time()
print('Elapsed time = ',repr(end_time-start_time))

#%%
#This code cell performs statistics and calculates the fractal dimension on the
#data created by the crystals.
larea = np.log(averageArea)

plt.scatter(np.log(rseq),larea,c='blue')
plt.scatter(np.log(rseq[10:25]),larea[10:25],c='red')
#plots a scatter plot of the log of the radius and the log of the average number of occupied sites within that radius
plt.title("Log-Log plot of Occupied Sites Against Radius")
plt.xlabel("Log(Radius)")
plt.ylabel("Log(Number of Occupied Sites)")

grad, intercept, r_value, p_val, std = stats.linregress(np.log(rseq[5:25]),larea[5:25])
#Performs a linear regression on the middle section of the graph
print("Gradient estimate: ", grad)
print("Standard Error of line: ", std)
CIlower = grad-2.58*std #99% confidence interval
CIhigher = grad+2.58*std
print("Confidence interval: ", "(",CIlower,",", CIhigher,")")
xx = np.linspace(np.log(rseq[10]),np.log(rseq[25]))
plt.plot(xx,grad*xx+intercept,c='black') #Plots the line of best fit back on the data


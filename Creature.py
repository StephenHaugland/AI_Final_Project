# Stephen Haugland and Shane Snediker
# Artificial Intelligence Spring 2020
# This file contains the creature class 

import random # used for randomly seeding DNA


# Creature Class
# This class contains all data pertaining to the agents that will be navigating our maze
class Creature:
    currentOrientation = None # Specifies which direction the creature is facing
    currentLocation = [0,0] # Start each creature at the starting point of the maze
    DNA = [None] * 50 # This will hold the list of actions that the creature will take


    # initial randomized constructor, to be used to create first generation
    def __init__(self):
        self.currentOrientation = 'E' # Start all creatures facing towards the right
        # generate 50 random actions/movements to seed the first generation
        for x in range(50):
            self.DNA[x] = random.choice(['L', 'F', 'R'])

    # Test function to display DNA
    def printDNA(self):
        print(self.DNA)

    # constructor used in crossover
    #def __init__(self, mom, dad):
        


test = Creature()
test.printDNA()


# Stephen Haugland and Shane Snediker
# Artificial Intelligence Spring 2020
# This file contains the creature class 

import random # used for randomly seeding DNA


# Creature Class
# This class contains all data pertaining to the agents that will be navigating our maze
class Creature:

    currentOrientation = 0 # Specifies which direction the creature is facing, utilizes unit circle degrees
    currentPosition = [1,1] # Start each creature at the starting point of the maze
    DNA = [None] * 50 # This will hold the list of actions that the creature will take


    # initial randomized constructor, to be used to create first generation
    def __init__(self):
        # generate 50 random actions/movements to seed the first generation
        for x in range(50):
            self.DNA[x] = random.choice(['L', 'F', 'R'])


    # update the creatures orientation according to which direction it turns
    def turn(self,dir):
        # Degrees updated based on unit circle orientation
        if dir == 'L':
            self.currentOrientation += 90
            print("I just turned left.")
        elif dir == 'R':
            self.currentOrientation -= 90
            print("I just turned right.")
        # if turned a full 360 degrees, reset to 0
        if self.currentOrientation == 360 or self.currentOrientation == -360:
            self.currentOrientation = 0
        print("I am now facing " + str(self.currentOrientation)) 

    # Calculates the next position if movement were to be carried out based on current orientation
    def calculateNextPos(self, action):
        # calculate the next position
        nextPos = self.currentPosition
        # If facing up/north
        if self.currentOrientation == 90 or self.currentOrientation == -270:
            if action == 'F':
                nextPos[1] -= 1
            elif action == 'L':
                nextPos[0] -= 1
            elif action == 'R':
                nextPos[0] += 1
        # If facing down/south
        elif self.currentOrientation == 270 or self.currentOrientation == -90:
            if action == 'F':
                nextPos[1] += 1
            elif action == 'L':
                nextPos[0] += 1
            elif action == 'R':
                nextPos[0] -= 1
        # If facing right/east
        elif self.currentOrientation == 0 or self.currentOrientation == -360 or self.currentOrientation == 360:
            if action == 'F':
                nextPos[0] += 1
            elif action == 'L':
                nextPos[1] -= 1
            elif action == 'R':
                nextPos[1] += 1
        # If facing left/west
        elif self.currentOrientation == 180 or self.currentOrientation == -180:
            if action == 'F':
                nextPos[0] -= 1
            elif action == 'L':
                nextPos[1] += 1
            elif action == 'R':
                nextPos[1] -= 1
        
        # change orientation according to what action took place
        self.turn(action)

        return nextPos

    # function that moves the agent to its next position if a wall is not present
    def move(self, actionIterator, Maze):
        # determine next position
        action = self.DNA[actionIterator]
        print("I am about to move: " + action)
        nextPosition = self.calculateNextPos(action)
        # If the next position is not blocked, move there
        if Maze[nextPosition[1]][nextPosition[0]] == 0:
            # change previously held position back to a zero
            Maze[Ricky.currentPosition[1]][Ricky.currentPosition[0]] = 0
            self.currentPosition = nextPosition
            print("After moving I am at position " + str(self.currentPosition))
            # print on the maze where the creature is with an X
            Maze[Ricky.currentPosition[1]][Ricky.currentPosition[0]] = 'X'
        else:
            print("Agent ran into wall")

       
    # constructor used in crossover
    #def __init__(self, mom, dad):

    # Test function to display DNA
    def printDNA(self):
        print(self.DNA)

    


# Testing movement and object collision detection
Ricky = Creature()
Ricky.printDNA()


# note about 2D arrays
# elements can be accessed according to the following:
# The first index is the row or Y coordinate and the second index is the column or X coordinate
# Ex: Maze1[y][x]
Maze1 = [[1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 1]]


# Test loop to see how collision works
for x in range(5):
    Ricky.move(x,Maze1)
    print(Maze1[0])
    print(Maze1[1])
    print(Maze1[2])
    print(Maze1[3])
    print(Maze1[4])

    



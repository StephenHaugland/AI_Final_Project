# Stephen Haugland and Shane Snediker
# Artificial Intelligence Spring 2020
# This file contains the agent class 

import random # Used for randomly seeding DNA
import copy # Used to create deep copy of variables


# agent class
# This class contains all data pertaining to the agents that will be navigating our maze
class Agent:

    #########################################
    #### Class Attributes 
    #########################################

    current_orientation = 0 # Specifies which direction the agent is facing, utilizes unit circle degrees
    previous_position = [1,20] # Store the agent's previous position to repaint black on the screen
    current_position = [1,20] # Start each agent at the starting point of the maze
    DNA_length = 500 # Allow for dynamic DNA length to be easily changed
    DNA = [None] * DNA_length # This will hold the list of actions that the agent will take
    fitness_score = 0 # Stores the agents fitness score computed after final movement has been made, LOWER score is better!
    DNA_mutate_strand = (DNA_length // 10) # A holder variable that captures an integer value representing 10 percept of an agent's DNA

    #########################################
    #### Class Methods 
    #########################################

    # initial randomized constructor, to be used to create first generation
    def __init__(self, maze, DNA_array = None):
        # Overloading constructors in Python involves handing all possible
        # instances of the constructor within 1 method
        # So, we start with the first implementation: the case where we are
        # initializing the seed population by giving them a random DNA sequence
        if DNA_array == None:
            # generate 50 random actions/movements to seed the first generation
            for x in range(self.DNA_length):
                self.DNA[x] = random.choice(['L', 'F', 'R'])
            # spawn the agent at the start of the maze
            self.current_position = copy.deepcopy(maze.MAZE_START)
            self.previous_position = copy.deepcopy(maze.MAZE_START)
        # Now we turn to the secondary implementaiton for agents which happens
        # during reproduction when a new child is born
        else:
            # Another constructor to be used in the crossover function for creating new agents
            # This constructor takes an array of DNA resulting from reproduction between 2 parents
            self.DNA = DNA_array    # Give this agent his new DNA sequence
            # spawn the agent at the start of the maze
            self.current_position = copy.deepcopy(maze.MAZE_START)
            self.previous_position = copy.deepcopy(maze.MAZE_START)

    # update the agents orientation according to which direction it turns
    # dir: direction agent moves
    def turn(self,dir):
        # Degrees updated based on unit circle orientation
        if dir == 'L':
            self.current_orientation += 90
            print("I just turned left.")
        elif dir == 'R':
            self.current_orientation -= 90
            print("I just turned right.")
        # if turned a full 360 degrees, reset to 0
        if self.current_orientation == 360 or self.current_orientation == -360:
            self.current_orientation = 0
        print("I am now facing " + str(self.current_orientation)) 

    # Calculates the next position if movement were to be carried out
    # action: an action derived from DNA i.e. L, F, or R
    def calculate_next_pos(self, action):
        # calculate the next position
        # TODO: Find out how to copy variable contents, this is where bug occurs
        next_pos = copy.deepcopy(self.current_position)
        # If facing up/north
        if self.current_orientation == 90 or self.current_orientation == -270:
            if action == 'F':
                next_pos[1] -= 1
            elif action == 'L':
                next_pos[0] -= 1
            elif action == 'R':
                next_pos[0] += 1
        # If facing down/south
        elif self.current_orientation == 270 or self.current_orientation == -90:
            if action == 'F':
                next_pos[1] += 1
            elif action == 'L':
                next_pos[0] += 1
            elif action == 'R':
                next_pos[0] -= 1
        # If facing right/east
        elif self.current_orientation == 0 or self.current_orientation == -360 or self.current_orientation == 360:
            if action == 'F':
                next_pos[0] += 1
            elif action == 'L':
                next_pos[1] -= 1
            elif action == 'R':
                next_pos[1] += 1
        # If facing left/west
        elif self.current_orientation == 180 or self.current_orientation == -180:
            if action == 'F':
                next_pos[0] -= 1
            elif action == 'L':
                next_pos[1] += 1
            elif action == 'R':
                next_pos[1] -= 1
        
        # change orientation according to what action took place
        self.turn(action)

        return next_pos

    # function that moves the agent to its next position if a wall is not present
    # maze: 2D array agent is navigation through
    # action_iterator: integer expressing index of current genome/action being expressed from DNA
    def move(self, action_iterator, maze):
        changed_position = False

        # determine next position
        action = self.DNA[action_iterator]
        print("I am about to move: " + action)
        next_position = self.calculate_next_pos(action)

        # If the next position is not blocked, move there
        if maze[next_position[1]][next_position[0]] == 0:
            # Set the flag that the agent has moved
            changed_position = True
            # change previously held position back to a zero
            ## maze[self.current_position[1]][self.current_position[0]] = 0

            # since movement has occured, change previous position to current and update current to next
            self.previous_position = copy.deepcopy(self.current_position)
            self.current_position = copy.deepcopy(next_position)

            print("After moving I am at position " + str(self.current_position))
            # print on the maze where the agent is with an X
            ## maze[self.current_position[1]][self.current_position[0]] = 'X'
        # If the next position is occupied by an obstacle
        else:
            print("Agent movement is blocked by a wall")

        # Once the agent has completed its last action, calculate fitness
        # TODO move this to controller 
        if (action_iterator == (self.DNA_length - 1)):
            self.calculate_fitness(maze)

        return changed_position

    # Function that gives definition to an agent's DNA mutation
    # We choose to use a scrambled version of DNA mutation where 
    # we take a DNA strand that is a predetermined percentage of
    # an agent's total DNA size and we scramble the contents of
    # that strand and then put the scrambled strand back in place
    # Our current predetermined DNA mutation strand percentage 
    # (represented by DNA_mutate_strand) is 10%
    def mutate(self):
        # We need to find a random starting index within this agent's DNA strand to begin the mutation
        # We declare a variable that captures a random integer.  This random integer has to be 
        # less than the difference between the length of the agent's DNA strand and the length
        # of the mutating strand so that we can mutate from any random index within the DNA sequence
        start_index = random.randint(0, (len(self.DNA) - self.DNA_mutate_strand))
        
        # Initialize an array that will hold the DNA sequence to be scrambled
        mutation_sequence = []

        # Now we begin filling our mutation array with the specific sequence
        # of DNA from this agent that will be scrambled
        # Iterate through this agent's DNA sequence for the length of the
        # predetermined mutation DNA sequence
        # We need our iterator to start at zero on account of array indices beginning at zero
        i = 0
        # Initialize a loop that will iterate once for every gene in the mutation strand
        for i in range(self.DNA_mutate_strand - 1):
            # Load the mutation sequence array with the agent's DNA sequnence
            # beginning at the random starting index
            mutation_sequence.append(self.DNA[(start_index + i)])

        # Now that we've captured the strand to be scrambled, we scramble it
        mutation_sequence.scramble()

        # Now that the sequence has been scrambled, we can put it back
        k = 0
        # Initialize a loop that will iterate once for every gene in the strand that has now been mutated
        for k in range(self.DNA_mutate_strand - 1):
            # Find the place in the agent's DNA strand where the mutation sequence was pulled
            # and start at that index replacing indices with the scrambled values
            self.DNA[(start_index + k)] = mutation_sequence[k]

        # return the mutated agent
        return self
            

    # Test function to display DNA
    def print_DNA(self):
        print(self.DNA)


    # TODO crossover constructor
    # constructor used in crossover
    #def __init__(self, mom, dad):
        # figure out algorithm to combine two agents DNA


    # TODO mutation
    def mutate(self):
        pass



    # maze: 2D array agent is navigating through
    def calculate_fitness(self, maze):
        # calculate distance from final agent position to maze exit
        # d = sqrt((mazeX - agentX)^2 + (mazeY-agentY)^2)
        # save operation complexity by not square rooting

        # TODO We're catching an exception with our distance function in this next line of code.  Something about 
        # an array not having an argument equivalent to maze.MAZE_EXIT

        distance = (maze.MAZE_EXIT[1] - self.current_position[1])**2 + (maze.MAZE_EXIT[0] - self.current_position[0])**2
        # arbitrary number chosen to subtract distance from to make fitter agents have higher scores
        score = 150 - distance
        self.fitness_score = score
    



# Testing movement and object collision detection
# Ricky = Agent()
# Ricky.print_DNA()


# note about 2D arrays
# elements can be accessed according to the following:
# The first index is the row or Y coordinate and the second index is the column or X coordinate
# Ex: maze1[y][x] or maze1[row][column]

# maze1 = [[1, 1, 1, 1],
#         [1, 0, 0, 1],
#         [1, 0, 0, 1],
#         [1, 0, 0, 1],
#         [1, 1, 1, 1]]


# Test loop to see how collision works
# for x in range(50):
#     Ricky.move(x,maze1)
#     print(maze1[0])
#     print(maze1[1])
#     print(maze1[2])
#     print(maze1[3])
#     print(maze1[4])

# print("Ricky's fitness score was: " + str(Ricky.fitness_score))

    



# Stephen Haugland and Shane Snediker
# Artificial Intelligence Spring 2020
# This file contains the agent class defining the little bots that will navigate the maze 

import random   # Used for randomly seeding DNA
import copy     # Used to create deep copy of variables
import math     # Used to calculate distance

# Agent class
# This class contains all data pertaining to the individual agents that will be navigating our maze
class Agent:

    #########################################
    #### Class Attributes 
    #########################################

    current_orientation = 0     # Specifies which direction the agent is facing, utilizing unit circle degrees
    previous_position = [1,20]  # Store the agent's previous position to repaint black on the screen. In the form of [x,y]
    current_position = [1,20]   # Variable holding the agent's current position, which will begin at the maze entrance. In the form of [x,y]
    DNA_length = 500            # Variable representing the length of an agent's DNA structure
    fitness_score = 0           # Stores the agents overall fitness score computed after the final movement
    DNA_mutate_strand = (DNA_length // 10) # A holder variable that captures an integer value representing 10 percent of an agent's DNA
    agent_hit_wall = 0          # Variable that tracks how many time this agent hits the wall to assess a fitness penalty

    #########################################
    #### Class Methods 
    #########################################

    # Agent constructor includes two implementations of agents
    # One for the first generation, and one for subsequent generations
    # Parameters:  maze: a maze object that this agent will be connected to
    #              dna_length: an integer representing this agent's DNA sequence length
    #              DNA_array: a list of string values representing this agent's genes
    def __init__(self, maze, dna_length, DNA_array = None):
        # Overloading constructors in Python involves handling all possible
        # instances of the constructor within 1 method
        # We begin by establishing 2 variables that every agent will have
        # An integer variable holding the length of their DNA structure
        self.DNA_length = dna_length
        # And a DNA array to hold their DNA sequence (which is really a list of actions that the agent will take)
        self.DNA = [] 
        # Now we start with the first implementation: the case where we are
        # initializing the seed population by giving them a random DNA sequence
        # This is the implementation that is used because when calling the constructor 
        # you do not include the DNA-array parameter
        if DNA_array == None:
            # generate 50 random actions/movements to seed the first generation
            for _ in range(self.DNA_length):
                self.DNA.append(random.choice(['L', 'F', 'R']))
        # Now we turn to the secondary implementaiton for agents which happens
        # during reproduction when a new child is born
        else:
            # Another constructor to be used in the crossover function for creating new agents
            # This constructor takes an array of DNA resulting from reproduction between 2 parents
            self.DNA = DNA_array    # Give this agent his new DNA sequence
        # spawn the agent at the start of the maze
        self.current_position = copy.deepcopy(maze.MAZE_START)
        self.previous_position = copy.deepcopy(maze.MAZE_START)

    # Update the agent's orientation according to which direction it turns
    # Parameters:  dir: A char containing one of 3 directions ('L' for left, 'R' for right, or 'F' for straight forward)
    def turn(self,dir):
        # Degrees updated based on unit circle orientation

        # If this turn is left, then we need to add 90 degrees to the agent's current orientation
        if dir == 'L':
            self.current_orientation += 90
        # If this turn is right, then we need to subtract 90 degrees from the agent's current orientation    
        elif dir == 'R':
            self.current_orientation -= 90
        # If the agent turned a full 360 degrees, reset to 0
        if self.current_orientation == 360 or self.current_orientation == -360:
            self.current_orientation = 0 

    # Calculates the next position if movement were to be carried out
    # Parameter:  action: A char representing the agent's next directional movement
    # Return:     next_pos: A list containing the next maze coordinates where the agent will move in the form of [x,y]
    def calculate_next_pos(self, action):
        # Begin by setting next position variable equal to the agent's current position
        # next_pos is an array with the first element tracking the x direction and the second element tracking the y direction
        # So next_pos[0] adjustments move agent left and right, while next_pos[1] adjustments move agent up and down
        # Start the next position at the current position and make modifications from there
        next_pos = copy.deepcopy(self.current_position)
        # If the agent is currently facing up/north, determine its next position based on its current action
        if self.current_orientation == 90 or self.current_orientation == -270:
            if action == 'F':
                next_pos[1] -= 1
            elif action == 'L':
                next_pos[0] -= 1
            elif action == 'R':
                next_pos[0] += 1
        # If the agent is currently facing down/south, determine its next position based on its current action
        elif self.current_orientation == 270 or self.current_orientation == -90:
            if action == 'F':
                next_pos[1] += 1
            elif action == 'L':
                next_pos[0] += 1
            elif action == 'R':
                next_pos[0] -= 1
        # If the agent is currently facing right/east, determine its next position based on its current action
        elif self.current_orientation == 0 or self.current_orientation == -360 or self.current_orientation == 360:
            if action == 'F':
                next_pos[0] += 1
            elif action == 'L':
                next_pos[1] -= 1
            elif action == 'R':
                next_pos[1] += 1
        # If the agent is currently facing left/west,determine its next position based on its current action
        elif self.current_orientation == 180 or self.current_orientation == -180:
            if action == 'F':
                next_pos[0] -= 1
            elif action == 'L':
                next_pos[1] += 1
            elif action == 'R':
                next_pos[1] -= 1
        # return the next position in the form [x,y]
        return next_pos

    # Function that moves the agent to its next position if a wall is not present
    # Parameters: action_iterator: An integer to iterate through the agent's DNA structure
    #             maze: 2D maze array that the agent is navigating
    # Return:     changed_position: the next maze location where the agent will step to
    def move(self, action_iterator, maze):
        # Establish a boolean flag that stores whether or not the agent has changed position, assume no movement
        changed_position = False
        # Determine next position by capturing the next gene representing a directional movement
        action = self.DNA[action_iterator]
        # Calculate the next position of this agent based on the DNA instruction
        next_position = self.calculate_next_pos(action)
        
        # if agent makes it to exit, increase fitness score to incentivize getting there ASAP
        if (self.current_position[0] == maze.MAZE_EXIT[0] and self.current_position[1] == maze.MAZE_EXIT[1]) or (next_position[0] == maze.MAZE_EXIT[0] and next_position[1] == maze.MAZE_EXIT[1]):
            print("Agent made it to exit!!!!!!!!!!!!! ")
            # for every round of movement before the end of the DNA, add 5 points per "saved" action
            self.fitness_score += 5
        # Check to see if the next grid location contains an obstacle, if not blocked move there
        elif maze.MAZE_GRID[next_position[1]][next_position[0]] == 0:
            # Set the flag to represent the agent's movement
            changed_position = True
            # since movement has occured, change previous position to current and update current to the next position
            self.previous_position = copy.deepcopy(self.current_position)
            self.current_position = copy.deepcopy(next_position)
        # However, if the next position is occupied by an obstacle the agent can't move
        else:
            self.agent_hit_wall += 1


        # Regardless of if the agents changed positions, update its orientation accordingly
        self.turn(action)  
        # Return the flag status of this movement
        return changed_position

    # Function that gives definition to an agent's DNA mutation
    # We choose to use a scrambled version of DNA mutation where 
    # we take a DNA strand that is a predetermined percentage of
    # an agent's total DNA size and we scramble the contents of
    # that strand and then put the scrambled strand back in place.
    # Our current predetermined DNA mutation strand percentage 
    # (represented by DNA_mutate_strand) is 10%
    # No parameters
    # Return: self: the mutated agent
    # def mutate(self):
    #     # We need to find a random starting index within this agent's DNA strand to begin the mutation
    #     # We declare a variable that captures a random integer.  This random integer has to be 
    #     # less than the difference between the length of the agent's DNA strand and the length
    #     # of the mutating strand so that we can mutate from any random index within the DNA sequence
    #     start_index = random.randint(0, (len(self.DNA) - self.DNA_mutate_strand))
        
    #     # Initialize an array that will hold the DNA sequence to be scrambled
    #     mutation_sequence = []

    #     # Now we begin filling our mutation array with the specific sequence
    #     # of DNA from this agent that will be scrambled
    #     # Iterate through this agent's DNA sequence for the length of the
    #     # predetermined mutation DNA sequence
    #     # We need our iterator to start at zero on account of array indices beginning at zero
    #     i = 0
    #     # Initialize a loop that will iterate once for every gene in the mutation strand
    #     for i in range(self.DNA_mutate_strand - 1):
    #         # Load the mutation sequence array with the agent's DNA sequnence
    #         # beginning at the random starting index
    #         mutation_sequence.append(self.DNA[(start_index + i)])

    #     # Now that we've captured the strand to be scrambled, we scramble it
    #     random.shuffle(mutation_sequence)

    #     # Now that the sequence has been scrambled, we can put it back
    #     k = 0
    #     # Initialize a loop that will iterate once for every gene in the strand that has now been mutated
    #     for k in range(self.DNA_mutate_strand - 1):
    #         # Find the place in the agent's DNA strand where the mutation sequence was pulled
    #         # and start at that index replacing indices with the scrambled values
    #         self.DNA[(start_index + k)] = mutation_sequence[k]

    #     # return the mutated agent
    #     return self

    #-------- Alternative variation to our mutation function as of Monday 5-11 -----------------------------------

    # Function that gives definition to an agent's DNA mutation
    # In this implementation, we use a new DNA sequence version 
    # of DNA mutation where we take a DNA strand that is a 
    # predetermined percentage of an agent's total DNA size and 
    # we remove it, replacing it with a new random sequence of DNA.
    # Our current predetermined DNA mutation strand percentage 
    # (represented by DNA_mutate_strand) is 10%
    # No parameters
    # Return: self: the mutated agent
    def mutate(self):
        # We need to find a random starting index within this agent's DNA strand to begin the mutation
        # We declare a variable that captures a random integer.  This random integer has to be 
        # less than the difference between the length of the agent's DNA strand and the length
        # of the mutating strand so that we can mutate from any random index within the DNA sequence
        start_index = random.randint(0, (len(self.DNA) - self.DNA_mutate_strand))
        
        # Initialize an array that will hold the new DNA mutation sequence
        mutation_sequence = []

        # First let's create a brand new random sequence of DNA instructions of size DNA_mutate_strand
        for _ in range(self.DNA_mutate_strand):
            mutation_sequence.append(random.choice(['L', 'F', 'R']))

        # Now we replace the mutation strand of the agent with the new mutated values
        # We need our iterator to start at zero on account of array indices beginning at zero
        i = 0
        # Initialize a loop that will iterate once for every gene in the mutation strand
        for i in range(self.DNA_mutate_strand - 1):
            # Replace the current gene value with the new mutated value
            self.DNA[(start_index + i)] = mutation_sequence[i]

        # return the mutated agent
        return self



    # -------------------- END OF ALTERNATIVE MUTATION IMPLENTATION ---------------------

    # Test function to display DNA
    def print_DNA(self):
        print(self.DNA)

    # # Function that calculates an agent's fitness at the conclusion of a generation of maze navigating
    # # Parameters:  maze: 2D array that the agent is navigating
    # def calculate_fitness(self, maze):
    #     # calculate distance from final agent position to maze exit
    #     # d = sqrt((mazeX - agentX)^2 + (mazeY-agentY)^2)
    #     # save operation complexity by not square rooting
    #     distance = (abs(maze.MAZE_EXIT[1] - self.current_position[1])) + (abs(maze.MAZE_EXIT[0] - self.current_position[0]))
    #     # arbitrary number chosen to subtract distance from to make fitter agents have higher scores
    #     score = 100 - distance
    #     self.fitness_score = score   

    
    
    #-------------------- Alternative variation to our fitness function as of 5-11 ---------------
    # This variation penalizes an agent for hitting the wall and for not at least making 
    # it halfway across the maze


    # Function that calculates an agent's fitness at the conclusion of a generation of maze navigating
    # Parameters:  maze: 2D array that the agent is navigating
    def calculate_fitness(self, maze):
        
        # Begin by tallying the positive fitness score by rewarding
        # the movements of agents that avoid obstacles and traverse
        # closer to the maze exit
        # calculate distance from final agent position to maze exit
        # d = sqrt((mazeX - agentX)^2 + (mazeY-agentY)^2)
        # save operation complexity by not square rooting
        #distance = math.sqrt(((maze.MAZE_EXIT[1] - self.current_position[1])** 2) + ((maze.MAZE_EXIT[0] - self.current_position[0])** 2 ))
        distance = (abs(maze.MAZE_EXIT[1] - self.current_position[1])) + (abs(maze.MAZE_EXIT[0] - self.current_position[0]) )
        # To avoid getting caught by a local minimum situation, let's give a bonus to 
        # agents that at least make it half way through the maze
        if distance > 35:
           distance -= 5
        
        # Now we pick an arbitrary number to subtract our current fitness score (distance) 
        # from this number to ensure that fitness scores will increase in value.
        # Because the distance calculated above favors smaller distances, we use this 
        # calculation to invert the values so that shorter distances from the maze exit
        # are reflected with higher fitness scores

        
        # Finally we need to punish the agent for hitting the wall
        # We subtract from the agent's positive distance score a point for every time they hit a wall
        # We've incremented each agent's member variable to track their collisions
        #score = score - (.25 * self.agent_hit_wall)
        self.fitness_score += (100 - distance)
         

    #------------------- END OF ALTERNATIVE FITNESS FUNCTION DEFINITION -------------------------

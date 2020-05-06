# Stephen Haugland and Shane Snediker
# Artificial Intelligence Spring 2020
# This file creates a population of agents 
# and defines the DNA crossover of successive populations as well as mutations

import Agent        # Import user defined class that defines individual agents
import random       # Import Python random library for generating random numbers

# Population class
# Class for organinizing the agent population and reproduction
class Population:

    #########################################
    #### Class Attributes 
    #########################################

    pop_size = None             # The size of each generation of agents
    Agent_quiver = [None]       # An array containing pop_size Agent objects
    number_of_survivors = 20    # A constant value representing the top 20 agents of each generation


    #########################################
    #### Class Methods 
    #########################################

    # Population constructor to initiate a population of agents to traverse the maze
    def __init__(self, agents, size):
        self.pop_size = size
        self.Agent_quiver = agents

    # This method takes in a generation of agents,
    # orders them from fittest to weakest and returns 
    # a randomized order of the surviving parents 
    def kill_the_weak(self):
        # First we have to kill off the weakest from the previous generation
        # Survival of the fittest is gruesome
        # Begin by aligning the population of agents from the fittest to the weakest
        Ordered_agents = sorted(self.Agent_quiver, key = self.Agent_quiver.fitness, reverse = True)
        # Now we kill half of the population
        # Let's initialize an array half the size of our population
        # to hold the survivors
        Fittest = [self.number_of_survivors]
        # Now we iterate through the list of ordered agents saving the top half
        for agent in range((self.number_of_survivors)):
            Fittest.append(Ordered_agents[agent])
        # We want this reproductive process to be random between the surviving parents
        # Therefore we need to randomize the order or the parent array
        Fittest.shuffle()

        return Fittest
                
    # Function to define DNA crossover reproduction
    # Because the directional order of an agent's movements will lead to
    # increased fitness within individual agents, we adopt a version
    # of reproduction called ordered crossover.  In ordered crossover,
    # large segments of DNA get chunked together and passed on to successive generations
    # Throughout this method, we often refer to the first parent in a genetic 
    # combination as p1, and the second parent as p2
    def  crossover(self):
        # We begin by killing the weakest half of the population
        self.kill_the_weak()
        # Initialize an array to hold our new crossover generation
        new_pop = []

        # Ultimately, in this version of crossover we want to take a DNA strand
        # of random size from p1 plucked from a random location within p1's DNA sequence
        # We then place that random strand at a random location within the child's DNA sequence
        # At that point we begin filling in the other half of the child's DNA structure with 
        # p2's DNA

        # Initialize a dynamic array that will hold the specific sequence of DNA
        # from p1 that will be passed to the child
        DNA_holder = []

        # Now that we have a randomized order within the surviving parent list
        # we can start the reproductive process.  This will be a pretty detailed
        # for loop that will iterate through the shuffled parent list 
        # combining specific DNA segments and genes to create children
        # Each iteration of the first nested loop combines 2 agents from 
        # the parent array and creates a child
        # i will be tied to p1 and j will be tied to p2
        for i, j in range(Fittest.len()):
            # Create a random integer from 50 to the size of an agent's DNA strand
            # We will pull a strand of DNA of this random size from p1
            p1_DNA_strand = random.randint(50, self.Agent_quiver.DNA_length)
            # Create a random integer from 0 up to the size of DNA bits 
            # that are not getting pulled from p1 to represent the index 
            # where we will place the DNA strand from p1
            # In other words, we're going to place the random sized DNA
            # segment from p1 at a random location in the child's DNA
            # structure, and this random integer variable will help us
            # avoid an out of bounds error
            pull_DNA_strip = random.randint(0, (self.Agent_quiver.DNA_length - p1_DNA_strand))
            # Iterate through the p1 DNA structure capturing a chunk of size p1_DNA_strand
            for k in range(p1_DNA_strand):
                # Hold the DNA segment
                DNA_holder.append(Fittest.Agent_quiver.DNA[k])
                
                #----------------------------------------------
                # Here is where I left off.  I need to figure out a where to test
                # the code that I've written in this file.  Currently I'm working on the
                # 2nd nest of this loop which will do the work of ordering the DNA into
                # a new child DNA structure.  I think that within this nested loop it will
                # also be best to do mutation.  A good line of code to handle mutation will
                # be something like: if random.random() <= .05, then randomly switch the values 
                # of a couple indices within the child DNA structure.  This represents allowing
                # mutation to take place 5% of the time.  Also, a lot of my thoughts about this 
                # process are based off of a generation size of 50.  We'll have to talk about 
                # the implications and consequences of changing that number or allowing for
                # user-defined generation size.  Either way, next in this area is to specifically
                # build a child DNA strand using a specific segment from parent 1 and filling in
                # the remaining indices with parent 2's DNA
                #----------------------------------------------


            # Capture the in tact DNA strand from p1
            #preserved_strand = 

        


        return new_pop
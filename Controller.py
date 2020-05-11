# Stephen Haugland and Shane Snediker
# Artificial Intelligence Spring 2020
# This file links our agent with our graphical grid
# Controller also contains the main program loop

import pygame # import pygame library to display graphics
import Agent  # import user defined agent class to represent maze navigating agents
import Maze   # import user defined Maze class to represent the environment
import Cross  # import user defined Population Class
import copy

# Define our maze colors
BLACK = (0, 0, 0)          # Background color
RED = (255, 0, 0)          # Maze obstacle colors
WHITE = (255, 255, 255)    # Agent test color
BLUE = (50, 50, 255)       # Agent test color

# global variable that control the time clock and the drawable screen
clock = None
screen = None

# initialize pygame
def pygame_setup(maze):
    # Initialize the pygame library that facilitates the graphical maze
    pygame.init()
    # create a screen to draw the maze on
    global screen
    screen = pygame.display.set_mode([maze.MAZE_SIZE[0], maze.MAZE_SIZE[1] + 100])
    # Set title of screen
    pygame.display.set_caption("Artificial Intelligence Final Project Spring 2020")
    # Declaration of a clock variable that utilizes a clock function
    # from the pygame library that mediates the speed of the screen updates
    global clock
    clock = pygame.time.Clock()
    # Set the screen background
    screen.fill(BLACK)

# display the maze to the screen
def draw_maze(maze): 
    # Draw the maze one time before entering the game loop
    # For every row in the grid
    for row in range(41):
        # And every column as well              
        for column in range(70):
            # Let's make the background black
            color = BLACK
            # Now we iterate through our 2 dimensional array and print obstacle locations in red              
            if maze.MAZE_GRID[row][column] == 1:
                color = RED
            # The pygame draw.rect function takes 3 primary arguments:
            # The first argument is the surface on which the rectangle will be drawn
            # The second is the desired color of the rectangle
            # The third is a list/tuple with the following values in this order:
            # x coordinate, y coordinate, width of rectangle, Height of rectangle, and the thickness of the rectangle lines
            # If no argument is given for the thickness parameter (like in our case), then the default is to fill the rectangle with the color argument
            pygame.draw.rect(screen,
                             color,
                             # x coordinate is the product of the cell width and the current column 
                             [maze.CELL_SIZE * column,   
                             # y coordinate is the product of the cell height and the current row     
                             maze.CELL_SIZE * row,     
                             # rectangle width
                             maze.CELL_SIZE,             
                             # rectangle height
                             maze.CELL_SIZE])    
    # Update the screen with what has been drawn
    pygame.display.update()        

# This moves every agent in the population one time
def move_population_once(pop):
    # Bool variable that gets SET if agent could move and changed positions
    Moved = False 
    global actionNumber, done_moving
    # Check if agents still have moves to execute
    if (actionNumber < pop.agent_DNA_length):
        # move every agent once
        for x in range(pop.pop_size):
            Moved = pop.Agent_quiver[x].move(actionNumber,pop.maze)
        
            # If an agent changes positions, update the screen
            if Moved == True:
                #change the previous position to black
                color = BLACK
                #Peek line 66 for draw.rect() argument explanation
                pygame.draw.rect(screen, color, [pop.maze.CELL_SIZE * pop.Agent_quiver[x].previous_position[0], pop.maze.CELL_SIZE * pop.Agent_quiver[x].previous_position[1], pop.maze.CELL_SIZE, pop.maze.CELL_SIZE])
                #update the new position to white
                color = WHITE
                pygame.draw.rect(screen, color, [pop.maze.CELL_SIZE * pop.Agent_quiver[x].current_position[0], pop.maze.CELL_SIZE * pop.Agent_quiver[x].current_position[1], pop.maze.CELL_SIZE, pop.maze.CELL_SIZE])
                # Update the screen with what has been drawn
                pygame.display.update()
        # increment which DNA gene is firing, which action the agent is taking
        actionNumber += 1
    else:
        done_moving = True
        # print("This should only happen once at the end")

def reset_population(pop):

    # Draw over all agents with black, clean the board
    for x in range(pop.pop_size):
        # change the previous position to black
        color = BLACK
        pygame.draw.rect(screen, color, [pop.maze.CELL_SIZE * pop.Agent_quiver[x].current_position[0], pop.maze.CELL_SIZE * pop.Agent_quiver[x].current_position[1], pop.maze.CELL_SIZE, pop.maze.CELL_SIZE])
    
    # Reset all the agents positions to the start of the maze
    pop.reset()

    # Draw all of the agents at the start
    for y in range(pop.pop_size):
        # update the new position to white
        color = WHITE
        pygame.draw.rect(screen, color, [pop.maze.CELL_SIZE * pop.Agent_quiver[y].current_position[0], pop.maze.CELL_SIZE * pop.Agent_quiver[y].current_position[1], pop.maze.CELL_SIZE, pop.maze.CELL_SIZE])
    # update what we've drawn
    pygame.display.update()
    pygame.time.delay(250)
  
######### Highlight all the agents that are selected to get eaten ###########
def highlight_weak(pop):
    fittest = pop.kill_the_weak()
    color = RED
    for x in range(len(fittest)):
        pygame.draw.rect(screen, color, [maze_instance.CELL_SIZE * fittest[x].current_position[0], maze_instance.CELL_SIZE * fittest[x].current_position[1], maze_instance.CELL_SIZE, maze_instance.CELL_SIZE])
    # Update the screen with what has been drawn
    pygame.display.update()
    pygame.time.delay(3000)

######## Highlight all the selected parents #######
def highlight_parents(pop):
    # Select parents
    selected = copy.deepcopy(pop.selection())
    color = BLUE
    for x in range(len(selected) - 1):
        pygame.draw.rect(screen, color, [maze_instance.CELL_SIZE * pop.Agent_quiver[selected[x]].current_position[0], maze_instance.CELL_SIZE * pop.Agent_quiver[selected[x]].current_position[1], maze_instance.CELL_SIZE, maze_instance.CELL_SIZE])
    # Update the screen with what has been drawn
    pygame.display.update()
    pygame.time.delay(3000)


# create a maze object
maze_instance = Maze.Maze()
# Seed the first population to navigate the maze
test_population = Cross.Population(100, maze_instance, 150) # (pop_size, maze, DNA_length)
# setup pygame display
pygame_setup(test_population.maze)
# display the maze to the pygame window
draw_maze(test_population.maze)


# create a font object. 
# 1st parameter is the font file 
# which is present in pygame. 
# 2nd parameter is size of the font 
font = pygame.font.Font('freesansbold.ttf', 32) 
# create a text suface object, 
# on which text is drawn on it. 
text = font.render('Average Fitness: 0 Top fitness: 0', True, RED, BLUE) 
# create a rectangular object for the 
# text surface object 
textRect = text.get_rect()  
# set the center of the rectangular object. 
textRect.center = ((maze_instance.MAZE_SIZE[1] // 2) + 55 , (maze_instance.MAZE_SIZE[0] // 2) + 80) 
# copying the text surface object 
# to the display surface object  
# at the center coordinate. 
screen.blit(text, textRect) 




# TODO I think this might be where we will add code to allow the user to choose 
# the amount of agents in the simulation


########################################################
# Basic Genetic Algorithm Pseudo Code from my understanding:
# 1: Seed first generation
# 2: do while(TerminationCondition != True):
# 3:    population.move()
# 4:    population.calculate_fitness()
# 5:    population.select_parents()
# 6:    population.crossover&mutate()
# 7:    population.kill_the_weak()
# 8:    population.reset()
#########################################################


# -------- Start of Main Program Loop -----------

done_moving = False     # The flag that allows the maze to loop until the user clicks the close button
actionNumber = 0 # This is the DNA index for the agent to execute each loop
FPS = 100         # defines game loop frames per second; lower numbers can be used to more closely observe agent movement
exited = False

for generation in range(10):
    while ((not exited) and (not done_moving)):
        # Defines how many frames per second the simulation runs at
        clock.tick(FPS) # should be called once per frame
        # Checks if exit is clicked on
        for event in pygame.event.get():  
            # First, if the user clicks the close button, we need to close the window down
            if event.type == pygame.QUIT:
                # by changing the loop flag to True
                exited = True

        #####################
        # Population movement
        #####################
        
        # move the entire populatio one step forward
        move_population_once(test_population)
        
    # Only continue with program, if window has not been exited
    if not exited:
        # RESET variables so next generation can spawn in
        done_moving = False
        actionNumber = 0
        
        ########################
        ## Calculate Fitess
        ########################
        test_population.calculate_fitness()
        test_population.get_fitness_stats()

        ########################
        ## Select Parents
        ########################
        test_population.selection()
        ## highlight_parents(test_population)

        ########################
        ## Produce children through crossover and mutation
        ########################

        ########################
        ## Kill the weak
        ########################
        ##test_population.kill_the_weak()

        #############################
        ## Reset for next generation
        #############################
        reset_population(test_population)
    
# --------  End of Main Program Loop -----------


###################################
### Fitness and Selection Tests ###
###################################




####### Display the fitness of each agent to console ########
# for x in range(test_population.pop_size):
#     print(test_population.Agent_quiver[x].fitness_score)

# Print the top and average fitness scores
# test_population.get_fitness_stats()




# highlight_parents(test_population)


######### Highlight the fittest x percentage of population ##################
# top_percent = .20
# color = BLUE
# for x in range(test_population.pop_size - 1,int(round(test_population.pop_size * (1-top_percent))),-1):
#     pygame.draw.rect(screen, color, [maze_instance.CELL_SIZE * test_population.Agent_quiver[x].current_position[0], maze_instance.CELL_SIZE * test_population.Agent_quiver[x].current_position[1], maze_instance.CELL_SIZE, maze_instance.CELL_SIZE])
# # Update the screen with what has been drawn
# pygame.display.update()
# pygame.time.delay(5000)








# Be IDLE friendly. If you forget this line, the program will 'hang' on exit.
pygame.quit()


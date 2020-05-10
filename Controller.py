# Stephen Haugland and Shane Snediker
# Artificial Intelligence Spring 2020
# This file links our agent with our graphical grid
# Controller also contains the main program loop

import pygame # import pygame library to display graphics
import Agent  # import user defined agent class to represent maze navigating agents
import Maze   # import user defined Maze class to represent the environment
import Cross  # import user defined Population Class

# Define our maze colors
BLACK = (0, 0, 0)          # Background color
RED = (255, 0, 0)          # Maze obstacle colors
WHITE = (255, 255, 255)    # Agent test color
MAGENTA = (255, 0, 255)    # Agent test color

# global variable that control the time clock and the drawable screen
clock = None
screen = None


def pygame_setup(maze):
    # Initialize the pygame library that facilitates the graphical maze
    pygame.init()
    # create a screen to draw the maze on
    global screen
    screen = pygame.display.set_mode(maze.MAZE_SIZE)
    # Set title of screen
    pygame.display.set_caption("Artificial Intelligence Final Project Spring 2020")
    # Declaration of a clock variable that utilizes a clock function
    # from the pygame library that mediates the speed of the screen updates
    global clock
    clock = pygame.time.Clock()
    # Set the screen background
    screen.fill(BLACK)

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
  

# create a maze object
maze_instance = Maze.Maze()
# setup pygame display
pygame_setup(maze_instance)
# display the maze to the pygame window
draw_maze(maze_instance)
# Update the screen with what has been drawn
pygame.display.update()





# Seed the first population to navigate the maze
test_population = Cross.Population(25, maze_instance, 100)



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
#########################################################

# -------- Main Program Loop -----------

done = False # The flag that allows the maze to loop until the user clicks the close button
actionNumber = 0 #This is the DNA index for the agent to execute each loop
FPS = 10  # defines game loop frames per second; lower numbers can be used to more closely observe agent movement

while not done:
    # Defines how many frames per second the simulation runs at
    clock.tick(FPS) # should be called once per frame

    # Checks if exit is clicked on
    for event in pygame.event.get():  
        # First, if the user clicks the close button, we need to close the window down
        if event.type == pygame.QUIT:
            # by changing the loop flag to True
            done = True

    ################
    # Agent movement
    ################

    # Bool variable that gets SET if agent could move and changed positions
    Moved = False 

    # Check if agents still have moves to execute
    if (actionNumber < test_population.agent_DNA_length):
        # move every agent once
        for x in range(test_population.pop_size):
            Moved = test_population.Agent_quiver[x].move(actionNumber,test_population.maze)
        
            # If an agent changes positions, update the screen
            if Moved == True:
                #change the previous position to black
                color = BLACK
                #Peek line 66 for draw.rect() argument explanation
                pygame.draw.rect(screen, color, [maze_instance.CELL_SIZE * test_population.Agent_quiver[x].previous_position[0], maze_instance.CELL_SIZE * test_population.Agent_quiver[x].previous_position[1], maze_instance.CELL_SIZE, maze_instance.CELL_SIZE])
                #update the new position to white
                color = WHITE
                pygame.draw.rect(screen, color, [maze_instance.CELL_SIZE * test_population.Agent_quiver[x].current_position[0], maze_instance.CELL_SIZE * test_population.Agent_quiver[x].current_position[1], maze_instance.CELL_SIZE, maze_instance.CELL_SIZE])
        # increment which DNA gene is firing, which action the agent is taking
        actionNumber += 1
    # once a full round of movement has occurred, exit loop
    else:
        done = True
        print("This should only happen once at the end")

    # Update the screen with what has been drawn
    pygame.display.update()
    
# Display the fitness of each agent
test_population.calculate_fitness()
for x in range(test_population.pop_size):
    print(test_population.Agent_quiver[x].fitness_score)


# Be IDLE friendly. If you forget this line, the program will 'hang' on exit.
pygame.quit()


# Stephen Haugland and Shane Snediker
# Artificial Intelligence Spring 2020
# This file links our agent with our graphical grid
# Controller also contains the main program loop

import pygame # import pygame library to display graphics
import Agent  # import user defined agent class to represent maze navigating agents
import Maze   # import user defined Maze class to represent the environment


# Initialize the pygame library that facilitates the graphical maze
pygame.init()
 
# create a maze object
Maze = Maze.Maze()


# create a screen to draw the maze on
screen = pygame.display.set_mode(Maze.MAZE_SIZE)

# Set title of screen
pygame.display.set_caption("Artificial Intelligence Final Project Spring 2020")
 

 
# Declaration of a clock variable that utilizes a clock function
# from the pygame library that mediates the speed of the screen updates
clock = pygame.time.Clock()

# Define our maze colors
BLACK = (0, 0, 0)    # Background color
RED = (255, 0, 0)    # Maze obstacle colors
WHITE = (255, 255, 255)    # Agent test color
 
# Set the screen background
screen.fill(BLACK)

# Draw the maze one time before entering the game loop
# For every row in the grid
for row in range(41):
    # And every column as well              
    for column in range(70):
        # Let's make the background black
        color = BLACK
        # Now we iterate through our 2 dimensional array and print obstacle locations in red              
        if Maze.MAZE_GRID[row][column] == 1:
            color = RED
        # Here we need to insert a snippet of code that prevents our diagonal 
        # obstacles from showing as jagged lines.  Because our maze is built off 
        # the structure of a grid, diagonal obstacles show as rough jagged lines
        # Here we manually insert pygame lines to make the maze look better
        # The first line is the 2nd obstacle in the maze - a diagonal line from the top left corner of the maze down and to the right
        pygame.draw.line(screen, color, (90, 40), (200, 150), 20)
        # The second line is the 3rd obstacle in the maze - a diagonal line from the lower left corner of the maze up and to the right
        pygame.draw.line(screen, color, (90, 369), (200, 259), 20)
        # The third and fourth lines here cover the double diagonal obstacle in the center of our maze
        pygame.draw.line(screen, color, (296, 201), (379, 118), 27)
        pygame.draw.line(screen, color, (295, 202), (383, 290), 25)
        # The pygame draw.rect function takes 3 primary arguments:
        # The first argument is the surface on which the rectangle will be drawn
        # The second is the desired color of the rectangle
        # The third is a list/tuple with the following values in this order:
        # x coordinate, y coordinate, width of rectangle, Height of rectangle, and the thickness of the rectangle lines
        # If no argument is given for the thickness parameter (like in our case), then the default is to fill the rectangle with the color argument
        pygame.draw.rect(screen,
                            color,
                            # x coordinate is the product of the cell width and the current column 
                            [Maze.CELL_SIZE * column,   
                            # y coordinate is the product of the cell height and the current row     
                            Maze.CELL_SIZE * row,     
                            # rectangle width
                            Maze.CELL_SIZE,             
                            # rectangle height
                            Maze.CELL_SIZE])            





# Create an agent to navigate the maze
Ricky = Agent.Agent(Maze)
Ricky.print_DNA()

# -------- Main Program Loop -----------

# The flag that allows the maze to loop until the user clicks the close button
done = False
actionNumber = 0 #This is the DNA index for the agent to execute each loop

while not done:
    # TODO I think this might be where we will add code to allow the user to choose 
    # the amount of agents in the simulation
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

    # check if agent still has moves to execute
    if (actionNumber < Ricky.DNA_length):
        # For every frame, move the agent once
        Moved = Ricky.move(actionNumber, Maze.MAZE_GRID)
        # iterate which action will be performed
        actionNumber += 1
        # if the agent changed positions update the screen accordingly
        if Moved == True:
            # change the previous position to black
            color = BLACK
            # Peek line 66 for draw.rect() argument explanation
            pygame.draw.rect(screen, color, [Maze.CELL_SIZE * Ricky.previous_position[0], Maze.CELL_SIZE * Ricky.previous_position[1], Maze.CELL_SIZE, Maze.CELL_SIZE])
            # update the new position to white
            color = WHITE
            pygame.draw.rect(screen, color, [Maze.CELL_SIZE * Ricky.current_position[0], Maze.CELL_SIZE * Ricky.current_position[1], Maze.CELL_SIZE, Maze.CELL_SIZE])

    
    pygame.time.wait(250)

    # Limit to 60 frames per second
    clock.tick(60)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.update()

# Be IDLE friendly. If you forget this line, the program will 'hang' on exit.
pygame.quit()




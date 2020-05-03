# Stephen Haugland and Shane Snediker
# Artificial Intelligence Spring 2020
# This file defines the grid that holds the sprite collision data

import pygame 

# Define some colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Let's set the parameters of a grid location so that we
# break our whole maze out into 5x5 cells
Width = 10
Height = 10

# Now we need to create a 2-dimensional array (a list of lists)
grid = []                           # declare the 2 dimensional array
for row in range(40):               # begin a loop that will iterate through every row of the grid (a row being 5 pixels long so 400/5 = 80)
    grid.append([])                 # add an empty array that will hold every cell location in this row
    for column in range(70):       # begin a loop that will iterate through every column (a column being 5 pixels wide so 700/5 = 140)
        grid[row].append(0)         # establish a cell at this grid location giving it a default value of zero which will be the value of a cell not containing a maze obstacle





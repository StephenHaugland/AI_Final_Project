# Stephen Haugland and Shane Snediker
# Artificial Intelligence Spring 2020
# This file defines the grid that holds the sprite collision data

# Let's set the paramters of a grid location
Width = 1
Height = 1

# Now we need to create a 2-dimensional array (a list of lists)
grid = []                           # declare the 2 dimensional array
for row in range(600):              # begin a loop that will iterate through every row of the grid
    grid.append([])                 # add an empty array that will hold every cell location in this row
    for column in range(1000):      # begin a loop that will iterate through every column 
        grid[row].append(0)         # establish a cell at this grid location giving it a default value of zero


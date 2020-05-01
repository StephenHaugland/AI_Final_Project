# Stephen Haugland and Shane Snediker
# Artificial Intelligence Spring 2020
# This file contains our main function and maze definition


from graphics import *  # Accessing the graphical library functions

# Define a function to easily create line objects
def line(x1, y1, x2, y2):
    return Line(Point (x1, y1), Point(x2, y2))


# The main body of the program
def main () :
    maze = GraphWin("My Window", 1000, 600)     # Create the initial window that will pop up on the screen
    maze.setBackground(color_rgb(0, 0, 0))       # Sets the background of the window to black

    # The following is the part of the program where we use line objects to draw the maze lines
    # I've separated the border walls and obstacles code segments

    # Left Wall border
    # Roughly halfway in the left wall there is a hole where the AI sprites will enter the maze
    left_top_border = line(0, 2, 0, 287)                                # top of sprite's entrance hole begins at y coordinate 287
    left_bottom_border = line(0, 308, 0, 599)                           # bottom of sprite's entrance hole ends at y coordinate 308 
    left_top_border.setOutline(color_rgb(255, 0, 0))
    left_top_border.setWidth(5)
    left_bottom_border.setOutline(color_rgb(255, 0, 0))
    left_bottom_border.setWidth(5)
    left_top_border.draw(maze)
    left_bottom_border.draw(maze)

    # Top Wall Border
    top_wall_border = line(0, 0, 1000, 0)
    top_wall_border.setOutline(color_rgb(255, 0, 0))
    top_wall_border.setWidth(7)
    top_wall_border.draw(maze)

    # Right Wall Border
    # Roughly halfway in the right wall is the maze exit where the sprites are trying to navigate
    right_top_border = line(1000, 0, 1000, 287)                             # Top of sprite's exit hole starts at y coordinate 287
    right_bottom_border = line(1000, 308, 1000, 600)                        # Bottom of sprite's exit hole starts at y coordinate 308
    right_top_border.setOutline(color_rgb(255, 0, 0))
    right_top_border.setWidth(7)
    right_bottom_border.setOutline(color_rgb(255, 0, 0))
    right_bottom_border.setWidth(7)
    right_top_border.draw(maze)
    right_bottom_border.draw(maze)

    # Bottom Wall Border
    bottom_border = line(0, 600, 1000, 600)
    bottom_border.setOutline(color_rgb(255, 0, 0))
    bottom_border.setWidth(7)
    bottom_border.draw(maze)

    # First obstacle
    obstacle1 = line(50, 275, 50, 325)                  
    obstacle1.setOutline(color_rgb(255, 0, 0))
    obstacle1.setWidth(20)          
    obstacle1.draw(maze)                            

    # 2nd and 3rd Obstacles - diagonal lines
# Bottom of sprite's exit hole starts at y coordinate 308
    obstacle2 = line(100, 100, 200, 200)
    obstacle3 = line(125, 475, 175, 350)
    obstacle2.setOutline(color_rgb(255, 0, 0))
    obstacle2.setWidth(20)
    obstacle3.setOutline(color_rgb(255, 0, 0))
    obstacle3.setWidth(20)
    obstacle2.draw(maze)
    obstacle3.draw(maze)

    # 4th Obstacle
    obstacle4_top_diagonal = line(400, 300, 480, 220)
    obstacle4_bottom_diagonal = line(400, 300, 480, 380)
    obstacle4_top_diagonal.setOutline(color_rgb(255, 0, 0))
    obstacle4_top_diagonal.setWidth(20)
    obstacle4_bottom_diagonal.setOutline(color_rgb(255, 0, 0))
    obstacle4_bottom_diagonal.setWidth(20)
    obstacle4_top_diagonal.draw(maze)
    obstacle4_bottom_diagonal.draw(maze)
    
    # 5th and 6th obstacles
    obstacle5_horizontal = line(580, 480, 680, 480)
    obstacle5_vertical = line(680, 480, 680, 380)
    obstacle5_horizontal.setOutline(color_rgb(255, 0, 0))
    obstacle5_horizontal.setWidth(20)
    obstacle5_vertical.setOutline(color_rgb(255, 0, 0))
    obstacle5_vertical.setWidth(20)
    obstacle5_horizontal.draw(maze)
    obstacle5_vertical.draw(maze)

    obstacle6_horizontal = line(580, 120, 680, 120)
    obstacle6_vertical = line(680, 120, 680, 220)
    obstacle6_horizontal.setOutline(color_rgb(255, 0, 0))
    obstacle6_horizontal.setWidth(20)
    obstacle6_vertical.setOutline(color_rgb(255, 0, 0))
    obstacle6_vertical.setWidth(20)
    obstacle6_horizontal.draw(maze)
    obstacle6_vertical.draw(maze)

    # 7th obstacle
    obstacle7 = line(800, 250, 800, 350)
    obstacle7.setOutline(color_rgb(255, 0, 0))
    obstacle7.setWidth(20)
    obstacle7.draw(maze)

    maze.getMouse()                              #Allows the window to stay put until you click on it with the mouse
    maze.close()

main()


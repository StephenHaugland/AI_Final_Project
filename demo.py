# Stephen Haugland and Shane Snediker
# Artificial Intelligence Spring 2020
# This file contains our main function and maze definition


from graphics import *  # Accessing the graphical library functions

# Define a function to easily create line objects
def line(x1, y1, x2, y2):
    return Line(Point (x1, y1), Point(x2, y2))

# ---------------------The main body of the program------------------------------------
def main () :
    maze = GraphWin("My Window", 700, 400)       # Create the initial window that will pop up on the screen
    maze.setBackground(color_rgb(0, 0, 0))       # Sets the background of the window to black

    obstacle_width = 10
    
    # The following is the part of the program where we use line objects to draw the maze lines
    # I've separated the border walls and obstacles code segments

    # Left Wall border
    # Roughly halfway in the left wall there is a hole where the AI sprites will enter the maze
    left_top_border = line(0, 0, 0, 188)                                # top of sprite's entrance hole begins at y coordinate 287
    left_bottom_border = line(0, 208, 0, 400)                           # bottom of sprite's entrance hole ends at y coordinate 308 
    left_top_border.setOutline(color_rgb(255, 0, 0))
    left_top_border.setWidth(obstacle_width)
    left_bottom_border.setOutline(color_rgb(255, 0, 0))
    left_bottom_border.setWidth(obstacle_width)
    left_top_border.draw(maze)
    left_bottom_border.draw(maze)

    # Top Wall Border
    top_wall_border = line(0, 0, 700, 0)
    top_wall_border.setOutline(color_rgb(255, 0, 0))
    top_wall_border.setWidth(obstacle_width)
    top_wall_border.draw(maze)

    # Right Wall Border
    # Roughly halfway in the right wall is the maze exit where the sprites are trying to navigate
    right_top_border = line(700, 0, 700, 188)                             # Top of sprite's exit hole starts at y coordinate 287
    right_bottom_border = line(700, 208, 700, 400)                        # Bottom of sprite's exit hole starts at y coordinate 308
    right_top_border.setOutline(color_rgb(255, 0, 0))
    right_top_border.setWidth(obstacle_width)
    right_bottom_border.setOutline(color_rgb(255, 0, 0))
    right_bottom_border.setWidth(obstacle_width)
    right_top_border.draw(maze)
    right_bottom_border.draw(maze)

    # Bottom Wall Border
    bottom_border = line(0, 400, 700, 400)
    bottom_border.setOutline(color_rgb(255, 0, 0))
    bottom_border.setWidth(obstacle_width)
    bottom_border.draw(maze)

    # First obstacle
    obstacle1 = line(50, 175, 50, 225)                  
    obstacle1.setOutline(color_rgb(255, 0, 0))
    obstacle1.setWidth(obstacle_width)          
    obstacle1.draw(maze)                            

    # 2nd and 3rd Obstacles - diagonal lines
    obstacle2 = line(100, 50, 200, 150)
    obstacle3 = line(125, 355, 175, 230)
    obstacle2.setOutline(color_rgb(255, 0, 0))
    obstacle2.setWidth(obstacle_width)
    obstacle3.setOutline(color_rgb(255, 0, 0))
    obstacle3.setWidth(obstacle_width)
    obstacle2.draw(maze)
    obstacle3.draw(maze)

    # 4th Obstacle
    obstacle4_top_diagonal = line(288, 200, 368, 120)
    obstacle4_bottom_diagonal = line(295, 200, 375, 280)
    obstacle4_top_diagonal.setOutline(color_rgb(255, 0, 0))
    obstacle4_top_diagonal.setWidth(obstacle_width)
    obstacle4_bottom_diagonal.setOutline(color_rgb(255, 0, 0))
    obstacle4_bottom_diagonal.setWidth(obstacle_width)
    obstacle4_top_diagonal.draw(maze)
    obstacle4_bottom_diagonal.draw(maze)
    
    # 5th and 6th obstacles
    obstacle5_horizontal = line(480, 330, 585, 330)
    obstacle5_vertical = line(580, 330, 580, 230)
    obstacle5_horizontal.setOutline(color_rgb(255, 0, 0))
    obstacle5_horizontal.setWidth(obstacle_width)
    obstacle5_vertical.setOutline(color_rgb(255, 0, 0))
    obstacle5_vertical.setWidth(obstacle_width)
    obstacle5_horizontal.draw(maze)
    obstacle5_vertical.draw(maze)

    obstacle6_horizontal = line(480, 70, 585, 70)
    obstacle6_vertical = line(580, 70, 580, 170)
    obstacle6_horizontal.setOutline(color_rgb(255, 0, 0))
    obstacle6_horizontal.setWidth(obstacle_width)
    obstacle6_vertical.setOutline(color_rgb(255, 0, 0))
    obstacle6_vertical.setWidth(obstacle_width)
    obstacle6_horizontal.draw(maze)
    obstacle6_vertical.draw(maze)

    # 7th obstacle
    obstacle7 = line(650, 150, 650, 250)
    obstacle7.setOutline(color_rgb(255, 0, 0))
    obstacle7.setWidth(obstacle_width)
    obstacle7.draw(maze)

    maze.getMouse()                              #Allows the window to stay put until you click on it with the mouse
    maze.close()

main()


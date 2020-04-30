# Shane Snediker and Stephen Haugland Artificial Intelligence Final Project

# This is a simple program for me to just mess around with graphics and try
# to get an initial maze working 


from graphics import *  # Accessing the graphical library functions

def main () :
    maze = GraphWin("My Window", 1000, 600)     # Create the initial window that will pop up on the screen
    maze.setBackground(color_rgb(0, 0, 0))       # Sets the background of the window to black

    # Everything with python graphics runs off points.  You create Point objects and manipulate them
    # The following is the part of the program where I use points to draw the maze lines
    # I've separated the code into specific labeled areas

    # Left Wall border
    # Roughly halfway in the left wall there is a hole where the AI sprites will enter the maze
    top_left_point = Point(0, 2)
    left_mid_point = Point(0, 295)                                      # top of sprite hole begines at y coordinate 295
    left_mid_top_point = Point(0, 301)                                  # bottom of sprite hole ends at y coordinate 301 
    bottom_left_point = Point(0, 599)
    left_top_line = Line(top_left_point, left_mid_point)
    left_bottom_line = Line(left_mid_top_point, bottom_left_point)
    left_top_line.setOutline(color_rgb(255, 0, 0))
    left_bottom_line.setOutline(color_rgb(255, 0, 0))
    left_top_line.draw(maze)
    left_bottom_line.draw(maze)

    # Top Wall Border
    top_left_thick_point = Point(0, 1)
    top_right_thick_point = Point(999, 1)
    top_top_line = Line(top_left_thick_point, top_right_thick_point)
    top_top_line.setOutline(color_rgb(255, 0, 0))
    top_right_point = Point(999, 2)
    top_line = Line(top_left_point, top_right_point)
    top_line.setOutline(color_rgb(255, 0, 0))
    top_top_line.draw(maze)
    top_line.draw(maze)

    # Right Wall Border
    bottom_right_point = Point(999, 599)
    right_line = Line(top_right_point, bottom_right_point)
    right_line.setOutline(color_rgb(255, 0, 0))
    right_line.draw(maze)

    # Bottom Wall Border
    bottom_line = Line(bottom_left_point, bottom_right_point)
    bottom_line.setOutline(color_rgb(255, 0, 0))
    bottom_line.draw(maze)

    # First obstacle
    begin_point1 = Point(50, 275)              
    end_point1 = Point(50, 325)                
    line1 = Line(begin_point1, end_point1)      
    line1.setOutline(color_rgb(255, 0, 0))          
    line1.draw(maze)                            

    # 2nd and 3rd Obstacles - diagonal lines

    begin_point2 = Point(100, 100)
    end_point2 = Point(200, 200)
    begin_point3 = Point(125, 475)
    end_point3 = Point(175, 350)
    Obstacle2 = Line(begin_point2, end_point2)
    Obstacle3 = Line(begin_point3, end_point3)
    Obstacle2.setOutline(color_rgb(255, 0, 0))
    Obstacle3.setOutline(color_rgb(255, 0, 0))
    Obstacle2.draw(maze)
    Obstacle3.draw(maze)


    maze.getMouse()                              #Allows the window to stay put until you click on it with the mouse
    maze.close()

main()


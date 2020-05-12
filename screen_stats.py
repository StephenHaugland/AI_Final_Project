# Stephen Haugland and Shane Snediker
# Artificial Intelligence Spring 2020
# This file contains the information for printing generational stats to the screen

import pygame       # Import pygame library to display graphics
import Population   # Import user defined population class to access generational stats

# screen_stats class
# This class organizes the data that we display to the demo screen
class screen_stats:

    ##########################
    #### CLASS ATTRIBUTES
    #########################

    # Colors
    TEAL = (0, 128, 128)       # Stat counters
    BLACK = (0, 0, 0)          # Background color

    pygame.init()

    gen_title_font = pygame.font.Font('freesansbold.ttf', 24)
    gen_display_font = pygame.font.Font('freesansbold.ttf', 24)
    ave_title_font = pygame.font.Font('freesansbold.ttf', 24)
    ave_display_font = pygame.font.Font('freesansbold.ttf', 24)
    top_score_title_font = pygame.font.Font('freesansbold.ttf', 24)
    top_score_display_font = pygame.font.Font('freesansbold.ttf', 24)
    
    gen_title_text = gen_title_font.render('Currently featuring generation: ', True, TEAL, BLACK)
    gen_display_text = gen_display_font.render(str(population.global_gen_counter + 1), True, TEAL, BLACK)
    ave_title_text = gen_title_font.render('Previous generation average fitness: ', True, TEAL, BLACK)
    ave_display_text = ave_display_font.render(str(population.average_fitness), True, TEAL, BLACK)
    top_score_title_text = top_score_title_font.render('Previous generation top score: ', True, TEAL, BLACK)
    top_score_display_text = top_score_display_font.render(str(population.top_score), True, TEAL, BLACK) 
    
    gen_title_Rect = None
    gen_display_Rect = None
    ave_title_Rect = None
    ave_display_Rect = None
    top_score_title_Rect = None
    top_score_display_Rect = None

    font_holder = [gen_title_font, gen_display_font, ave_title_font, ave_display_font, top_score_title_font, top_score_display_font]
    rect_holder = [gen_title_Rect, gen_display_Rect, ave_title_Rect, ave_display_Rect, top_score_title_Rect, top_score_display_Rect]

    # Constructor
    def __init__(self, maze, population, screen):
        # Create our font objects to give our display boxes a font and font size
        # The 1st parameter is the font file which pygame contains and the second parameter is the font size
        self.font_holder[0] = self.gen_title_font 
        self.font_holder[1] = self.gen_display_font
        self.font_holder[2] = self.ave_title_font
        self.font_holder[3] = self.ave_display_font
        self.font_holder[4] = self.top_score_title_font
        self.font_holder[5] = self.top_score_display_font

        # Create our text surfaces on which our fonts will be applied
        # 1st parameter is what gets written, 2nd is a special pygame antialias boolean
        # that needs to be set to True, the 3rd is the font color, and the 4th is the background color 
        

        # Now we create rectangle objects for our text surfaces to be placed in
        self.gen_title_Rect = gen_title_text.get_rect() 
        self.rect_holder[0] = self.gen_title_Rect
        self.gen_display_Rect = gen_display_text.get_rect()
        self.rect_holder[1] = self.gen_display_Rect
        self.ave_title_Rect = ave_title_text.get_rect()
        self.rect_holder[2] = self.ave_title_Rect
        self.ave_display_Rect = ave_display_text.get_rect()
        self.rect_holder[3] = self.ave_display_Rect
        self.top_score_title_Rect = top_score_title_text.get_rect()
        self.rect_holder[4] = self.top_score_title_Rect
        self.top_score_display_Rect = top_score_display_text.get_rect()
        self.rect_holder[5] = self.top_score_display_Rect

        # Now we place our rectangles on our maze: 1st parameter is the x coordinate of the upper left corner of the rectangle
        # The 2nd parameter is the y coordinate of the upper left corner of the rectangle
        self.gen_title_Rect.center = ((maze.MAZE_SIZE[1] // 2) + 45 , (maze.MAZE_SIZE[0] // 2) + 80)
        self.gen_display_Rect.center = ((maze.MAZE_SIZE[1] // 2) + 245 , (maze.MAZE_SIZE[0] // 2) + 80)
        self.ave_title_Rect.center = ((maze.MAZE_SIZE[1] // 2) + 55 , (maze.MAZE_SIZE[0] // 2) + 110)
        self.ave_display_Rect.center = ((maze.MAZE_SIZE[1] // 2) + 305 , (maze.MAZE_SIZE[0] // 2) + 110)
        self.top_score_title_Rect.center = ((maze.MAZE_SIZE[1] // 2) + 45 , (maze.MAZE_SIZE[0] // 2) + 140)
        self.top_score_display_Rect.center = ((maze.MAZE_SIZE[1] // 2) + 260 , (maze.MAZE_SIZE[0] // 2) + 140) 


    def get_fonts(self):
        return self.font_holder

    def get_rects(self):
        return self.rect_holder


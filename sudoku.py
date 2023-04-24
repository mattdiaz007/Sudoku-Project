# this is the main executable for the sudoku project
# this will incorporate all the classes that we have created up to this point

#def main():


#if __name__ == '__main__':
#    main()

import pygame, sys
from constants import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
# sets the caption of the opening window to the input string
pygame.display.set_caption("Sudoku: Paradise Lost")
square_font = pygame.font.Font(NUM_FONT, NUM_SIZE)
# changes the color of the background to white
#screen.fill(BG_COLOR)

def draw_grid():
    for i in range(1, BOARD_ROWS):
        # pygame.draw.line will is a function to draw lines
        # 1st parameter is screen
        # 2nd parameter is the start_pos
        # 3rd parameter is the end_pos
        # 4th parameter is the line width
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i * SQUARE_SIZE),
            (WIDTH, i * SQUARE_SIZE),
            LINE_WIDTH_BOLD
        )
    # draw the 9 cell border horizontal lines
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i* (SQUARE_SIZE/3)),
            (WIDTH, i * (SQUARE_SIZE/3)),
            LINE_WIDTH_CELL
        )
    # draw 3 main vertical lines for the 3x3 boxes
    for i in range(1, BOARD_COLS):
        pygame.draw.line(
        screen,
        LINE_COLOR,
        (i * SQUARE_SIZE, 0),
        (i * SQUARE_SIZE, HEIGHT),
        LINE_WIDTH_BOLD
        )
    # draw the 9 cell border vertical lines
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
        screen,
        LINE_COLOR,
        (i * (SQUARE_SIZE/3), 0),
        (i * (SQUARE_SIZE/3), HEIGHT),
        LINE_WIDTH_CELL
        )

        # draw the 9 horizontal cell lines
        #for i in range(1, CELL_ROWS):
            # pygame.draw.line will is a function to draw lines
            # 1st parameter is screen
            # 2nd parameter is the start_pos
            # 3rd parameter is the end_pos
            # 4th parameter is the line width
        #    pygame.draw.line(
        #        screen,
        #        LINE_COLOR,
        #        (0, i * (SQUARE_SIZE/3)),
        #        (WIDTH, i * (SQUARE_SIZE/3),
        #        LINE_WIDTH_CELL
        #    )
        # draw the 9 vertical cell lines
        #for i in range(1, CELL_COLS):
        #    pygame.draw.line(
        #    screen,
        #    LINE_COLOR,
        #    (i * (SQUARE_SIZE/3), 0),
        #    (i * (SQUARE_SIZE/3), HEIGHT),
        #    LINE_WIDTH_CELL
        #    )

def draw_num():
    # first we will define a surface, the num surface that will appear on the grid





# following are notes in drawing a grid
# I want to use this in order to draw the initial 3x3 box grid
# then I want to put in additional 2 vertical line and 2 horizontal lines in each one of the squares
# giving the constants that we have the initial window is a 600x600
    # each square is 200x200, SQUARE_SIZE = 200
    #
    # 0 ----- 200 ----- 400 ----- 600
    #
    # the upper left hand corner horizontal line will be given by (0,200)
        # (0, 1*SQUARE_SIZE)
    # the lower left hand corner horizontal line will be given by (0,400)
    # the middle part of the upper line can be defined by (200,400)
        # (WIDTH, 1*SQUARE_SIZE)
    # the final upper right hand corner of the line can be defined by (600,200)
        # (0, 2*SQUARE_SIZE)
    # the lower right hand corner horizontal line will be given by (0,400)
        # (WIDTH, 2*SQUARE_SIZE)
            # starting point = (0, i*SQUARE_SIZE)
            # ending point = (WIDTH, i*SQUARE_SIZE)
                # i = 1,2
    # VERTICAL LINES
        # use a similar strat w vertical lines
            # start point (i*SQUARE_SIZE, 0)
                # i = 1,2
                # (200,0) , (400,0)
            # ending point (i*SQUARE_SIZE, HEIGHT)
                # i = 1,2
                # (200,600), (400,600)

screen.fill(BG_COLOR)
draw_grid()


while True:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit


    pygame.display.update()
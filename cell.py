# this class represents a single cell in the sudoku board
from constants import *
import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        # constructor for the cell class
        # value will be a number 0-9
        # instance attributes set up in the constructor
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.selected = False



    def set_cell_value(self, value):
        # setter for the cell value
        self.value = value

    def set_sketched_value(self, value):
        # setter for the cells sketched value
        self.sketched_value = value


    def draw(self):
        if self.selected:
            #  pygame.draw.line will is a function to draw lines
                #  1st parameter is screen
                #  2nd parameter is line color
                #  3rd parameter is the start_pos
                #  4th parameter is the end_pos
                #  5th parameter is the line width
            for i in (0, CELL_D):
                # draw a vert line
                pygame.draw.line(
                    self.screen,
                    CELL_SELECTED,
                    (self.col * CELL_D + i, self.row * CELL_D - LINE_WIDTH_CELL // 2),
                    (self.col * CELL_D + i, self.row * CELL_D + CELL_D + LINE_WIDTH_CELL // 2),
                    LINE_WIDTH_BOLD
                )
                # draw a horz line
                pygame.draw.line(
                    self.screen,
                    CELL_SELECTED,
                    (self.col * CELL_D - LINE_WIDTH_CELL // 2, self.row * CELL_SIZE_D + i),
                    (self.col * CELL_D + CELL_D + LINE_WIDTH_CELL // 2, self.row * CELL_D + i),
                    LINE_WIDTH_BOLD
                )
        if self.value != 0:
            # define the number surface
            # draw the number surface
            value_font = pygame.font.Font(None, 80)
            value_text = "" if self.value == 0 else str(self.value)  # Set 0 to no value
            value_surf = value_font.render(str(value_text), False, NUM_COLOR)
            x_pos = ((CELL_D * self.col) + (CELL_D * self.col + CELL_D)) / 2
            y_pos = ((CELL_D * self.row) + (CELL_D * self.row + CELL_D)) / 2
            value_rect = value_surf.get_rect(center=(x_pos, y_pos))
            self.screen.blit(value_surf, value_rect)
        if self.sketched_value != 0:
            # define the sketch surface
            # draw the sketch surface
            sketch_font = pygame.font.Font(None, 60)
            sketch_surf = sketch_font.render(str(self.sketched_value), False, COLOR_SKETCH)
            sketch_rect = sketch_surf.get_rect(left=CELL_D * self.col + 5, top=CELL_D * self.row + 5)
            self.screen.blit(sketch_surf, sketch_rect)




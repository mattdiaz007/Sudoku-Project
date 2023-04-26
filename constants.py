# this will be a file that contains all the constants that our sudoku file can actually use to
# define the the dimensions of our boxes, lines, and to also give us the colors that we want to use throughout our
# sudoku game

# centralized color variables with tuple codes that any other variable can draw upon

RED = (255, 0, 0, 255)
BLACK = (0, 0, 0, 255)
GRAY =  (190, 190, 190, 255)
GOLD = (255, 215, 0, 255),
WHITE = (255, 255, 255, 255)
VIOLET = (238, 130, 238, 255)



# dimensions of the board and cells

WIDTH = 900
HEIGHT = 900
CELL_D = 100
BOX_D = 300
BOTTOM_B  = HEIGHT - CELL_D # bottom box
SQUARE_SIZE = 300
# need to look through my class files,
# i dont remember using SQUARE_SIZE, perhaps I used it while following Professor Zhou tic tac toe example



# additional variables binding num boxes, cols, rows

BOARD_ROWS = 3
BOARD_SIZE = 9
BOARD_COLS = 3
SPACE = 55



# width of the cell (reg_width) and box lines (bold_lines)

LINE_WIDTH_BOLD = 7
LINE_WIDTH_CELL = 3
WIN_LINE_WIDTH = 15



# color of different objects in the game

BG_COLOR = VIOLET
LINE_COLOR = BLACK
CELL_NOT_SELECTED = BLACK
CELL_SELECTED = RED
NUM_COLOR = GOLD
BUTTON_TEXT_COLOR = GOLD
COLOR_SKETCH = GRAY

# size of font for different text surfaces

NUM_SIZE = 80
GAME_WIN_FONT = 40
GAME_LOSS_FONT = 40




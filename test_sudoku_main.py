import pygame
from constants import *
from board import Board


def game_start(screen):
    # initialize the font of title, button, game_diff
    initial_title_font = pygame.font.Font(None,120)
    button_font = pygame.font.Font(None, BUTTON_TEXT_SIZE)
    game_diff_font = pygame.font.Font(None, 100)


    # fill in the background color of the pygame
    screen.fill(BG_COLOR)

    # define the title surface to appear on the pygame board
    title_surf = initial_title_font.render("Welcome to Paradise Lost", True, LINE_COLOR)

    # define the rectangle to specify the location of my surface
    title_rect = title_surf.get_rect(
        center = ((WIDTH // 2), (HEIGHT // 2 - 200)))

    # screen.blit to draw the surface onto the pygame window
    # 1st arg is surface, 2nd arg is the rectangle above the location of the surface
    screen.blit(title_surf, title_rect)

    game_diff_surf = game_diff_font.render("Pick Difficulty of Puzzle:", True, LINE_COLOR)
    game_diff_rect = game_surf.get_rect(
        center=((WIDTH // 2),(HEIGHT // 2)))
    screen.blit(game_diff_surf, game_diff_rect)

    # define a new surface with the specified text rendered on it (creating an image of the text)
    # then blit this text image onto another surface

    easy_text_surf = button_font.render('Easy', True, BUTTON_TEXT_COLOR)
    med_text_surf = button_font.render('Medium', True, BUTTON_TEXT_COLOR)
    hard_text_surf = button_font.render('Hard', True, BUTTON_TEXT_COLOR)

    # define the button object as a surface, then use fill (fill surf w/ COLOR)
    # blit the surface onto the game window

    easy_button_surf = pygame.Surface(((easy_text_surf.get_size()[0]+30),(easy_text_surf.get_size()[1]+30)))
    easy_button_surf.fill(LINE_COLOR)

    # pygame.Surface.blit - letting us draw one image onto another
    # 1st arg == source surface (text) to be drawn on this surface (button)
    # 2nd arg == dest (pair of coordinates) to represent the position of upper left corner of the blit/rect
    easy_button_surf.blit(easy_text_surf, (12,12))

    med_button_surf = pygame.Surface(((med_text_surf.get_size()[0] + 30), (med_text_surf.get_size()[1] + 30)))
    med_button_surf.fill(LINE_COLOR)
    med_button_surf.blit(med_text_surf, (12, 12))

    hard_button_surf = pygame.Surface(((hard_text_surf.get_size()[0] + 30), (hard_text_surf.get_size()[1] + 30)))
    hard_button_surf.fill(LINE_COLOR)
    hard_button_surf.blit(hard_text_surf, (12, 12))

    # define the button rectangle object
    easy_button_rect = easy_button_surf.get_rect(
        center=((WIDTH // 2 - 180 ), (HEIGHT // 2 + 180))
    )
    med_button_rect = med_button_surf.get_rect(
        center=((WIDTH // 2), (HEIGHT // 2 + 180))
    )
    hard_button_rect = hard_button_surf.get_rect(
        center=((WIDTH // 2 + 180), (HEIGHT // 2 + 180))
    )

    # screen.blit to bring buttons to the screen
    screen.blit(easy_button_surf,easy_button_rect)
    screen.blit(med_button_surf,med_button_rect)
    screen.blit(hard_button_surf,hard_button_rect)

    # make a while loop that updates board w the difficulty chosen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button_rect.collidepoint(event.pos):
                    return 30
                if med_button_rect.collidepoint(event.pos):
                    return 40
                if hard_button_rect.collidepoint(event.pos):
                    return 50
        pygame.display.update()



def game_loss(screen):
    # function for loss occurrence, format screen in the instance of a loss
    loss_font = pygame.font.Font(None, GAME_LOSS_FONT)
    button_font = pygame.font.Font(None, BUTTON_TEXT_SIZE)

    screen.fill(BG_COLOR)

    loss_surf = loss_font.render('GAME OVER :(', True, LINE_COLOR)
    loss_rect = loss_surf.get_rect(
        center = ((WIDTH // 2), (HEIGHT // 2 - 200)))
    screen.blit(loss_surf,loss_rect)

    # format screen for restart
    restart_text_surf = button_font.render('Restart', True, BG_COLOR)
    restart_button_surf = pygame.Surface(((restart_text_surf.get_size()[0]+30),(restart_text_surf.get_size()[1]+30)))
    restart_button_surf.fill(LINE_COLOR)
    restart_button_surf.blit(restart_text_surf,(12,12))

    restart_button_rect = restart_button_surf.get_rect(
        center = ((WIDTH // 2), (HEIGHT // 2 )))

    # bring the restart button to the screen
    screen.blit(restart_button_surf,restart_button_rect)

    while True:
        # the loop for quitting or for restarting the game
        for event in pygame.event.get():
            # player wants to quit
            if event.type == pygame.QUIT:
                pygame.quit()
            # player wants to restart and the main() is re-entered
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button_rect.collidepoint(event.pos):
                    main()
        pygame.display.update()

def game_won(screen):
    # function for win occurence, format screen in the instance of a win
    # similar setup as our loss game function
    win_font = pygame.font.Font(None, GAME_WIN_FONT)
    button_font = pygame.font.Font(None, BUTTON_TEXT_SIZE)

    screen.fill(BG_COLOR)

    win_surf = win_font.render("You win!", True, LINE_COLOR)
    win_rect = win_surf.get_rect(
        center=((WIDTH // 2), (HEIGHT // 2 - 200)))
    screen.blit(win_surf, win_rect)


    # exit button to appear on screen

    exit_text_surf = button_font.render('Exit Game!', True, BG_COLOR)

    exit_button_surf = pygame.Surface(
        ((exit__surf.get_size()[0] + 30), (restart_text_surf.get_size()[1] + 30)))
    exit_button_surf.fill(LINE_COLOR)
    exit_button_surf.blit(exit_text_surf, (12, 12))

    exit_button_rect = exit_button_surf.get_rect(
        center = ((WIDTH // 2), (HEIGHT // 2 )))

    screen.blit(exit_button_surf, exit_button_rect)

    # while loop for win occurance
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button_rect.collidepoint(event.pos):
                    pygame.quit()

        pygame.display.update()







def main():
    # start the main function
    # start the screen and the variables to carry into the game and the player options selected
    game_over = False
    pygame.init()
    pygame.display.set_caption('Sudoku: Paradise Lost')
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    difficulty = game_start(screen)

    game_board = Board(WIDTH,HEIGHT,screen,difficulty)
    game_board.draw()
    reset_rect = game_board.draw()
    restart_rect = game_board.draw()
    exit_rect = game_board.draw()
    select = False

###############################################################################################################

    while True:
        # mouse click event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    # This if statement accounts for when the game is actively being played
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = event.pos
                column, row = current_board.click(x, y)
                # This if statement accounts for the reset, restart, and quit implementations
                if reset_rect.collidepoint(x, y):
                    game_board.reset_to_original()
                if exit_rect.collidepoint(x, y):
                    pygame.quit()
                if restart_rect.collidepoint(x, y):
                    main()
                if 0 <= row <= 8 and 0 <= column <= 8:
                    if game_board.original[int(row)][int(column)] == 0:
                        current_cell = current_board.select(row, column)
                        selected = True
                        current_board.draw()
            pygame.display.update()
        # This while loop accounts for when a specific cell is selected
        while select:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        current_cell.set_cell_value(0)
                    # This accounts for every case of either adding or deleting a cell
                    if event.key == pygame.K_1:
                        current_cell.set_cell_value(1)
                    if event.key == pygame.K_2:
                        current_cell.set_cell_value(2)
                    if event.key == pygame.K_3:
                        current_cell.set_cell_value(3)
                    if event.key == pygame.K_4:
                        current_cell.set_cell_value(4)
                    if event.key == pygame.K_5:
                        current_cell.set_cell_value(5)
                    if event.key == pygame.K_6:
                        current_cell.set_cell_value(6)
                    if event.key == pygame.K_7:
                        current_cell.set_cell_value(7)
                    if event.key == pygame.K_8:
                        current_cell.set_cell_value(8)
                    if event.key == pygame.K_9:
                        current_cell.set_cell_value(9)
                    # This if statement accounts for deleting the value in the cell
                    if event.key == pygame.K_BACKSPACE:
                        current_cell.set_cell_value(0)
                        current_cell.selected = True
                        current_board.draw()
                        pygame.display.update()
                    current_board.update_board()
                    current_cell.draw(screen)
                    current_board.check_board()
                    current_cell.selected = True
                    current_board.draw()
                    # This statement checks for the win condition if the board is full
                    if current_board.is_full():
                        if current_board.check_board():
                            draw_game_win(screen)
                        else:
                            draw_game_loss(screen)
                        game_over = True
                        selected = False
                # This accounts for the reset, restart, and quit functions
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if reset_rect.collidepoint(x, y):
                        current_board.reset_to_original()
                    if exit_rect.collidepoint(x, y):
                        pygame.quit()
                    if restart_rect.collidepoint(x, y):
                        main()
                    column, row = current_board.click(x, y)
                    if 0 <= row <= 8 and 0 <= column <= 8:
                        if current_board.original[int(row)][int(column)] == 0:
                            current_cell = current_board.select(row, column)
                            selected = True
                            current_board.draw()
                pygame.display.update()
            pygame.display.update()









# start the program!!!
if __name__ == "__main__":
    main()



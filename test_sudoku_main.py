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
    # I am not sure if anything in this loops makes sense but i tried
     while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if reset_rect.collidepoint(mouse_pos):
                    game_board.reset()
                    select = False
                elif restart_rect.collidepoint(mouse_pos):
                    difficulty = game_board.difficulty
                    game_board = Board(WIDTH,HEIGHT,screen,difficulty)
                    game_board.draw()
                    reset_rect = game_board.reset_button_rect
                    restart_rect = game_board.restart_button_rect
                    exit_rect = game_board.exit_button_rect
                    select = False
                elif exit_rect.collidepoint(mouse_pos):
                    game_over = True
                else:
                    if not select:
                        select = game_board.select_cell(mouse_pos)
                    else:
                        game_board.input_number(mouse_pos)
                        if game_board.game_won():
                            game_over = True
                        else:
                            continue
                 
                        select = False
        
        # update screen
        pygame.display.update()

    pygame.quit()

    # needs more work, I am not understanding the implimentation of the other executables
    # will be looking at Professor Zhou's tic tac toe example again



# start the program!!!
if __name__ == "__main__":
    main()

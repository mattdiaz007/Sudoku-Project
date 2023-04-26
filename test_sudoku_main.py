import pygame
from constants import *
from board import Board


def game_start(screen):
    # initialize the font of title, button, game_diff
    initial_title_font = pygame.font.Font(None,120)
    button_font = pygame.font.Font(None, 80)
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

    game_surf = game_diff_font.render("Pick Difficulty of Puzzle:", True, LINE_COLOR)
    game_rect = game_surf.get_rect(
        center=((WIDTH // 2),(HEIGHT // 2)))
    screen.blit(game_surf, game_rect)

    # define the surface of the button text
    easy_text_surf = button_font.render('Easy', True, BUTTON_TEXT_COLOR)
    med_text_surf = button_font.render('Medium', True, BUTTON_TEXT_COLOR)
    hard_text_surf = button_font.render('Hard', True, BUTTON_TEXT_COLOR)

def game_loss(screen):


def game_won(screen):

def main():
    




# start the program!!!
if __name__ == "__main__":
    main()


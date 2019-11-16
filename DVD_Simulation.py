import pygame
import random  # Used for when choosing starting movement for logo
import os

# Constants
DVD_LOGO = 'DVD logo.png'  # This is the dvd logo that will move around.
WINDOW_WIDTH = 1000  # X
WINDOW_HEIGHT = 800  # Y
REFRESH_RATE = 60
finish = False  # Used for knowing when the user wants to end the game
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
len_x = 178  # Length of the actual logo in pixels
len_y = 82  # Length of the actual logo in pixels
HOW_FAST = 3  # Used to determine how fast the logo will go


# Functions
def case_1(y_pos):  # Checking if the logo hit the bottom floor(need to increase Y)
    return y_pos + len_y >= WINDOW_HEIGHT


def case_2(y_pos):  # Checking if the logo hit the top floor(need to decrease Y)
    return y_pos - len_y <= 0


def case_3(x_pos):  # Checking if the logo hit the right side(need to decrease X)
    return x_pos + len_x >= WINDOW_WIDTH


def case_4(x_pos):  # Checking if the logo hit the left side(need to decrease X)
    return x_pos - len_x <= 0


def choose_rand(start_value=0, end_value=0):
    """This function creates a random number that is either HOW_FAST or -HOW_FAST if no params were given,
    if params were given it will return a random between the ones given"""
    if start_value and end_value != 0:
        return random.randint(start_value, end_value - len_x)  # Subtract the len of x so
        # That logo does not spawn outside.
    if random.random() < 0.5:
        return HOW_FAST
    else:
        return -HOW_FAST


# Init screen
pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("DVD Simulation")
clock = pygame.time.Clock()
logo = pygame.image.load(DVD_LOGO)  # This loads the dvd logo into the variable logo
logo_x_pos = choose_rand(1, WINDOW_WIDTH)  # Chooses a random value for X to start from
logo_y_pos = choose_rand(1, WINDOW_HEIGHT)  # chooses a random value for Y to start from
X_CHANGER = choose_rand()  # Automatically gives them either how_fast or -HOW_FAST
Y_CHANGER = choose_rand()  # Automatically gives them either how_fast or -HOW_FAST
pygame.display.flip()

while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Checking if the user has pressed the quit quit button on the application
            finish = True
            pygame.quit()
            os._exit(1)  # Terminates the program
    screen.fill(BLACK)
    logo_x_pos = logo_x_pos + X_CHANGER
    logo_y_pos = logo_y_pos + Y_CHANGER
    if not logo_y_pos + len_y in range(1, WINDOW_HEIGHT) or not logo_y_pos in range(1, WINDOW_HEIGHT) \
            or not logo_x_pos + len_x in range(1, WINDOW_WIDTH) or not logo_x_pos in range(1, WINDOW_WIDTH):
        # This big if checks if the logo has touched one of the sides
        if case_1(logo_y_pos):  # Logo it hitting the bottom floor
            Y_CHANGER = -HOW_FAST
        if case_2(logo_y_pos):  # Logo is hitting the top floor
            Y_CHANGER = HOW_FAST
        if case_3(logo_x_pos):  # Logo is hitting the right side
            X_CHANGER = -HOW_FAST
        if case_4(logo_x_pos):  # Logo is hitting the left side
            X_CHANGER = HOW_FAST
    screen.blit(logo, (logo_x_pos, logo_y_pos))  # Printing the new logo
    pygame.display.flip()
    clock.tick(REFRESH_RATE)

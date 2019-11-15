import pygame
import random  # Used for when choosing starting movement for ball
import time
import math

# Constants
WINDOW_WIDTH = 800  # X
WINDOW_HEIGHT = 600  # Y
REFRESH_RATE = 60
finish = False  # Used for knowing when the user wants to end the game
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
RADIUS = 5


def case_1(y_pos):  # Checking if the ball hit the bottom floor(need to increase Y)
    return y_pos + RADIUS >= WINDOW_HEIGHT


def case_2(y_pos):  # Checking if the ball hit the top floor(need to decrease Y)
    return y_pos - RADIUS <= 0


def case_3(x_pos):  # Checking if the ball hit the right side(need to decrease X)
    return x_pos + RADIUS >= WINDOW_WIDTH


def case_4(x_pos):  # Checking if the ball hit the left side(need to decrease X)
    return x_pos - RADIUS <= 0


def choose_rand(start_value=0, end_value=0):
    """This function creates a random number that is either -1 or 1 if no params were given,
    if params were given it will return a random between the ones given"""
    if start_value and end_value !=0:
        return random.randint
    if random.random() < 0.5:
        return 1
    else:
        return -1


# Init screen
pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("DVD Simulation")
clock = pygame.time.Clock()
ball_x_pos = WINDOW_WIDTH/2
ball_y_pos = WINDOW_HEIGHT/2
X_CHANGER = choose_rand()  # Automatically gives them either 1 or -1
Y_CHANGER = choose_rand()  # Automatically gives them either 1 or -1
pygame.display.flip()

while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
            pygame.quit()
    pygame.display.flip()
    ball_x_pos = ball_x_pos + X_CHANGER
    ball_y_pos = ball_y_pos + Y_CHANGER
    if not ball_y_pos + RADIUS in range(1,WINDOW_HEIGHT) or not ball_y_pos - RADIUS in range(1,WINDOW_HEIGHT)\
            or not ball_x_pos + RADIUS in range(1,WINDOW_WIDTH) or not ball_x_pos - RADIUS in range(1,WINDOW_WIDTH):
        # This big if checks is the ball has touched one of the sides
        if case_1(ball_y_pos):  # Ball it hitting the bottom floor
            Y_CHANGER = -1
        if case_2(ball_y_pos):  # Ball is hitting the top floor
            Y_CHANGER = 1
        if case_3(ball_x_pos):  # Ball is hitting the right side
            X_CHANGER = -1
        if case_4(ball_x_pos):  # Ball is hitting the left side
            X_CHANGER = 1
    pygame.draw.circle(screen, WHITE, [ball_x_pos, ball_y_pos], RADIUS)
    pygame.display.flip()
    clock.tick(REFRESH_RATE)


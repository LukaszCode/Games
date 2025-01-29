# Game interface for the pong game

import pygame
from paddle import Paddle
from ball import Ball

# Define game colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREY = (128, 128, 128)

def draw_window(game_window, paddles, ball, width, height):
    """
    Draws the game window, including paddles, ball, and center line.

    Parameters:
    - game_window: The Pygame window surface to draw on.
    - paddles: A list of paddle objects to draw.
    - ball: The ball object to draw.
    - width: The width of the game window.
    - height: The height of the game window.
    """
    game_window.fill(BLACK)

    for paddle in paddles:
        draw_paddle(paddle, game_window)

    draw_center_line(game_window, width, height)
    draw_ball(ball, game_window)

    pygame.display.update()

"""
Draws the paddle on the game window.

Parameters:
- paddle: The paddle object to draw.
- game_window: The Pygame window surface to draw on.
"""
def draw_paddle(paddle, game_window):

    pygame.draw.rect(game_window, WHITE, (paddle.x, paddle.y, paddle.width, paddle.height))


"""
Draws the center line on the game window.

Parameters:
- game_window: The Pygame window surface to draw on.
- width: The width of the game window.
- height: The height of the game window.
"""
def draw_center_line(game_window, width, height):

    for i in range(0, height, height // 30):
        pygame.draw.line(game_window, GREY, (width // 2, i), (width // 2, i + height // 30), 2)

"""
Draws the ball on the game window.
Parameters:
- ball: The ball object to draw.
- game_window: The Pygame window surface to draw on.
"""
def draw_ball(ball, game_window):

    pygame.draw.circle(game_window, WHITE, (ball.x, ball.y), ball.radius)

"""
Draws the point board on the game window.

def draw_pointBoard(game_window, pointBoard, width, height):
    font = pygame.font.Font(None, 36)
    text = font.render(f"{pointBoard[0]} : {pointBoard[1]}", True, WHITE)
    textRect = text.get_rect()
    textRect.center = (width // 2, height // 10)
    game_window.blit(text, textRect)

"""

# Game interface for the pong game

import pygame

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
        paddle.draw_paddle(game_window)

    draw_center_line(game_window, width, height)
    ball.draw(game_window)

    pygame.display.update()

def draw_paddle(self, game_window):
    """
    Draws the paddle on the game window.

    Parameters:
    - self: The paddle object to draw.
    - game_window: The Pygame window surface to draw on.
    """
    pygame.draw.rect(game_window, self.COLOR, (self.x, self.y, self.width, self.height))


def draw_center_line(game_window, width, height):
    """
    Draws the center line on the game window.

    Parameters:
    - game_window: The Pygame window surface to draw on.
    - width: The width of the game window.
    - height: The height of the game window.
    """
    for i in range(0, height, height // 30):
        pygame.draw.line(game_window, GREY, (width // 2, i), (width // 2, i + height // 30), 2)
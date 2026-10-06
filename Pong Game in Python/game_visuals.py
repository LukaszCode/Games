# Game interface for the pong game
# Author : LukaszCode
# Version : 1.1

# This code defines the game interface for a pong game, including functions to draw the game window, paddles, ball, and center line. 
# It uses Pygame library to create a graphical interface for the game.

import pygame
from paddle import Paddle
from ball import Ball

# Define game colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREY = (128, 128, 128)

def draw_menu(window, width, height, WHITE, BLACK, RED, GREY):
    """
    Draws the main menu of the game.

    Parameters:
    - window: The Pygame window surface to draw on.
    - width: The width of the game window.
    - height: The height of the game window.
    - WHITE: The color for the text.
    - BLACK: The color for the background.
    - RED: The color for the buttons.
    - GREY: The color for the center line.
    """
    window.fill(BLACK)
    title_font = pygame.font.Font(None, 80)
    button_font = pygame.font.Font(None, 36)
    
    title = title_font.render("PONG Game", True, WHITE)
    window.blit(title, title.get_rect(center=(width // 2, 120)))
    
    buttons = {}
    options = [
        ("single player", "Player vs Computer Game"),
        ("two players", "Player vs Player Game"),
        ("credits", "Game credits"),
    ]
    
    for index, (action, label) in enumerate(options):
        rect = pygame.Rect(width // 2 - 150, 230 + index * 80, 300, 60)
        hovered = rect.collidepoint(pygame.mouse.get_pos())
        
        color = GREY if hovered else WHITE
        
        pygame.draw.rect(window, color, rect, border_radius=10)
        
        text = button_font.render(label, True, BLACK)
        window.blit(text, text.get_rect(center=rect.center))
        buttons[action] = rect
        
    pygame.display.update()
    return buttons

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

    for index in range(0, height, height // 30):
        pygame.draw.line(game_window, GREY, (width // 2, index), (width // 2, index + height // 30), 2)

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

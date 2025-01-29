# Paddles class and objects for the pong game.

import pygame
from game_visuals import WHITE

class Paddle:
    COLOR = WHITE
    VELOCITY = 4

    """
    Initializes a new instance of a paddle with specified coordinates and dimensions.

    Args:
        coordinate_x (float): The x-coordinate of the paddle's position.
        coordinate_y (float): The y-coordinate of the paddle's position.
        paddle_width (float): The width of the paddle.
        paddle_height (float): The height of the paddle.
    """
    def __init__(self, coordinate_x, coordinate_y, paddle_width, paddle_height):
        self.x = coordinate_x
        self.y = coordinate_y
        self.width = paddle_width
        self.height = paddle_height

    def move(self, up, height):
        if up and self.y >= 0:
            self.y -= self.VELOCITY
        elif not up and self.y < height - self.height:
            self.y += self.VELOCITY

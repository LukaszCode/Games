# Paddles class and objects for the pong game.

import pygame
from game_visuals import WHITE

class Paddle:
    COLOR = WHITE
    VELOCITY = 4

    def __init__(self, coordinate_x, coordinate_y, paddle_width, paddle_height):
        self.x = coordinate_x
        self.y = coordinate_y
        self.width = paddle_width
        self.height = paddle_height

    def draw_paddle(self, game_window):
        pygame.draw.rect(game_window, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up, height):
        if up and self.y >= 0:
            self.y -= self.VELOCITY
        elif not up and self.y < height - self.height:
            self.y += self.VELOCITY

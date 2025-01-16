# Ball object for the pong game.

import pygame
from game_visuals import WHITE

class Ball:
    COLOR = WHITE
    MAX_VELOCITY = 5

    def __init__(self, coordinate_x, coordinate_y, radius):
        self.x = coordinate_x
        self.y = coordinate_y
        self.radius = radius
        self.x_vel = self.MAX_VELOCITY
        self.y_vel = 0

    def draw(self, game_window):
        pygame.draw.circle(game_window, self.COLOR, (self.x, self.y), self.radius)

    def move(self, height):
        self.x += self.x_vel
        self.y += self.y_vel

        # Bounce off top and bottom walls
        if self.y - self.radius <= 0 or self.y + self.radius >= height:
            self.y_vel *= -1

# Ball object for the pong game.

import pygame

"""
Ball object for the pong game.

Attributes:
- MAX_VELOCITY (int): The maximum velocity of the ball.

Args:
- coordinate_x (float): The x-coordinate of the ball's position.
- coordinate_y (float): The y-coordinate of the ball's position.
- radius (float): The radius of the ball.
- x_vel (float): The x-velocity of the ball.
- y_vel (float): The y-velocity of the ball.
"""
class Ball:
    MAX_VELOCITY = 5

    def __init__(self, coordinate_x, coordinate_y, radius):
        self.x = coordinate_x
        self.y = coordinate_y
        self.radius = radius
        self.x_vel = self.MAX_VELOCITY
        self.y_vel = 0

    """
    Moves the ball based on its velocity and handles collisions with the top and bottom walls.
    """
    def move(self, height, paddles):
        self.x += self.x_vel
        self.y += self.y_vel

        # Bounce off top and bottom walls
        if self.y - self.radius <= 0 or self.y + self.radius >= height:
            self.y_vel *= -1

         # Check for collision with paddles
        for paddle in paddles:
            if self.check_collision(paddle):
                self.x_vel *= -1  # Reverse direction
                # Optionally add some randomness to the y-velocity for more dynamic behavior
                self.y_vel += (0.2 * (self.y - (paddle.y + paddle.height / 2)))  # Add slight angle effect
                break
    
    """
    Resets the ball to the center of the screen with a random velocity.
    """
    def reset(self, width, height):
        self.x = width // 2
        self.y = height // 2
        self.x_vel = self.MAX_VELOCITY
        self.y_vel = 0
    
    """
    Checks for collision between the ball and a paddle.
    """ 
    def check_collision(self, paddle):
        # Check if the ball is within the x-range of the paddle
        if self.x - self.radius <= paddle.x + paddle.width and self.x + self.radius >= paddle.x:
            # Check if the ball is within the y-range of the paddle
            if self.y - self.radius <= paddle.y + paddle.height and self.y + self.radius >= paddle.y:
                return True
        return False

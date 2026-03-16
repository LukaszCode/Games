# Ball object for the pong game with updated physics

import pygame
import math

"""
Ball object for the pong game.

Attributes:
- START_SPEED (int): The starting speed of the ball
- MAX_SPEED (int): The maximum speed of the ball
- SPEED_INCREMENT (int): The speed difference to add realism after the ball bounces against the paddle.
- MAX_BOUNCE_ANGLE (int): The maximum angle the ball bounces of the paddle (adds physics to ball trajectory)

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

        START_SPEED = 350
        MAX_SPEED = 900
        SPEED_INCREMENT = 35
        MAX_BOUNCE_ANGLE = math.radians(60)
        
        self.start_x = coordinate_x
        self.start_y = coordinate_y
        self.radius = radius
        self.x = float(coordinate_x)
        self.y = float(coordinate_y)
        self.radius = radius

        self.speed = self.START_SPEED
        self.x_vel = self.speed
        self.y_vel = 0

    """
    Move the ball using frame-independent motion and handle collisions.
    """
    def move(self, height, paddles, dt):
        self.x += self.x_vel * dt
        self.y += self.y_vel * dt

        # Bounce off top wall
        if self.y - self.radius <= 0:
            self.y = self.radius
            self.y_vel *= 1

        # Bounce off bottom wall
        elif self.y + self.radius >= height:
            self.y = height - self.radius
            self.y_vel *= 1

         # Check for collision with paddles
        for paddle in paddles:
            if self.check_collision(paddle):
                self.handle_paddle_collision(paddle)

    """
    Handle paddle collision

    The function handles the behaviour when the ball bounces off the paddle 
    with an angle based on hit position
    """
    def handle_paddle_collision(self, paddle):
                
                # Hit near centre of the paddle - flat bounce
                paddle_center = paddle.y + paddle.height / 2
                ball_center = self.y
                
                # Hit near top of the paddle - sharper upward bounce
                paddle_ball_intersection = ball_center - paddle_center
                normalised_paddle_ball_intersection  = (paddle_ball_intersection / (paddle.height / 2))

                # Clamp between -1 and 1 (attach ball to paddle)
                # Hit near bottom of the paddle - sharper downward bounce
                normalised_paddle_ball_intersection = max(-1, min(1, normalised_paddle_ball_intersection))
                bounce_angle = normalised_paddle_ball_intersection * self.MAX_BOUNCE_ANGLE

                # Increase speed gradually 
                self.speed = min(self.speed + self.SPEED_INCREMENT, self.MAX_SPEED)

                
                # Determine new horizontal direction based on incoming velocity
                if self.x_vel < 0:
                     self.x = paddle.x + paddle.width + self.radius
                     self.x_vel = self.speed * math.cos(bounce_angle)
                else:
                     self.x = paddle.x - self.radius
                     self.x_vel = self.speed * math.cos(bounce_angle)
                
                self.y_vel = self.speed * math.sin(bounce_angle)
    
    """
    Resets the ball to the center of the screen.
    """
    def reset(self, width, height, direction=1):
        self.x = width // 2
        self.y = height // 2
        self.speed = self.START_SPEED

        angle = math.radians(25)
        self.x_vel  = direction * self.speed * math.cos(angle)
        self.y_vel = self.speed * math.sin(angle)
    
    """
    Checks for collision between the ball and a paddle.
    """ 
    def check_collision(self, paddle):
        # Check collision between ball and paddle
        closest_x = max(paddle.x, min(self.x, paddle.x, paddle.width))
        closest_y = max(paddle.y, min(self.y, paddle.y, paddle.height))

        distance_x = self.x - closest_x
        distance_y = self.y - closest_y
        
        return (distance_x ** 2 + distance_y ** 2) <= self.radius ** 2


import pygame
import sys

# Initialize Pygame
pygame.init()
# Set a maximum frame rate so the game is smoother
clock = pygame.time.Clock()

# Set window size 
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Cap the frame rate to 60 frames per second
game_time = clock.tick(60)

# Set title 
pygame.display.set_caption("Simple pong")

# Set colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set paddle properties 
paddle_width = 10
paddle_height = 100
paddle_speed = 10

# Player and oponent positions
player_x = 50
player_y = ((screen_height // 2) - (paddle_height // 2))
opponent_x = ((screen_width - 50) - paddle_width)
opponent_y = ((screen_height // 2) - (paddle_height // 2))

# Ball properties
ball_width = 10
ball_height = 10
ball_speed_x = 7
ball_speed_y = 7
ball_x = ((screen_width // 2) - (ball_width // 2))
ball_y = ((screen_height // 2) - (ball_height // 2))

# Adjust paddle speed by specific time set by the clock

paddle_time = game_time / 1000.0
paddle_speed_adjusted = paddle_speed * paddle_time

# Main Game loop

while True:
    # Event loop to include user inputs and allow clean game close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Ball movement 
    ball_x += ball_speed_x 
    ball_y += ball_speed_y

    # Ball collides with top and bottom of the game window - point count?
    if ball_y <= 0 or ball_y >= screen_height - ball_height:
        ball_speed_y *= -1

    # Ball collides with right and left part of the game board - point for oposite team
    
    

    # Ball collides with paddles - ping-pong
    if (((ball_x <= player_x + paddle_width) and (player_y < ball_y < player_y + paddle_height)) \
    or ((ball_x >= opponent_x - paddle_width) and (opponent_y < ball_y < opponent_y + paddle_height))):
        ball_speed_x *= -1
    
    # Set the screen color
    screen.fill(BLACK)

    # Draw paddles and ball 
    pygame.draw.rect(screen, WHITE, (player_x, player_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (opponent_x, opponent_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, ball_width, ball_height))

    # Update the window
    pygame.display.flip()
    
    # Add player controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= paddle_speed_adjusted
    if keys[pygame.K_DOWN] and player_y < screen_height - paddle_height:
        player_y += paddle_speed_adjusted

    
    # Basic AI game component
    if opponent_y + paddle_height / 2 < ball_y:
        opponent_y += paddle_speed_adjusted
    else:
        opponent_y -= paddle_speed_adjusted


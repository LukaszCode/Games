# Main gameplay loop for the pong game

import pygame
from paddle import Paddle
from ball import Ball
from game_visuals import draw_window, WHITE, BLACK, RED, GREY

# Initialize pygame
pygame.init()
clock = pygame.time.Clock()

# Define game inputs
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple_Pong_Game")
FPS = 60

def handle_key_paddle_movement(keys, left_paddle, right_paddle, dt):
    if keys[pygame.K_w]:
        left_paddle.move(up=True, height=HEIGHT, dt=dt)
    elif keys[pygame.K_s]:
        left_paddle.move(up=False, height=HEIGHT, dt=dt)

    if keys[pygame.K_UP]:
        right_paddle.move(up=True, height=HEIGHT, dt=dt)
    elif keys[pygame.K_DOWN]:
        right_paddle.move(up=False, height=HEIGHT, dt=dt)


def main():
    run = True
    left_score = 0
    right_score = 0

    def reset_game():
        """Resets the ball and paddles to their initial positions."""
        left_paddle = Paddle(10, HEIGHT // 2 - 50, 20, 100)
        right_paddle = Paddle(WIDTH - 30, HEIGHT // 2 - 50, 20, 100) 
        ball = Ball(WIDTH // 2, HEIGHT // 2, 10)
        return left_paddle, right_paddle, ball

    left_paddle, right_paddle, ball = reset_game()

    while run:
        # Give time in seconds
        dt = clock.tick(FPS) / 1000 
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
        keys = pygame.key.get_pressed()
        handle_key_paddle_movement(keys, left_paddle, right_paddle, dt)
        
        # Pass paddles to ball.move() for collision detection
        ball.move(HEIGHT, [left_paddle, right_paddle], dt)

        # Check for ball going out of bounds
        if ball.x - ball.radius <= 0:
            right_score += 1
            left_paddle, right_paddle, ball = reset_game()
        elif ball.x + ball.radius >= WIDTH:
            left_score += 1
            left_paddle, right_paddle, ball = reset_game()

        draw_window(WINDOW, [left_paddle, right_paddle], ball, WIDTH, HEIGHT)

    pygame.quit()

if __name__ == '__main__':
    main()

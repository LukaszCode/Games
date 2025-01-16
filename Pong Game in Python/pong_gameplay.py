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

def handle_key_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w]:
        left_paddle.move(up=True, height=HEIGHT)
    elif keys[pygame.K_s]:
        left_paddle.move(up=False, height=HEIGHT)

    if keys[pygame.K_UP]:
        right_paddle.move(up=True, height=HEIGHT)
    elif keys[pygame.K_DOWN]:
        right_paddle.move(up=False, height=HEIGHT)

def main():
    run = True

    left_paddle = Paddle(10, HEIGHT // 2 - 50, 20, 100)
    right_paddle = Paddle(WIDTH - 30, HEIGHT // 2 - 50, 20, 100)
    ball = Ball(WIDTH // 2, HEIGHT // 2, 10)

    while run:
        clock.tick(FPS)
        draw_window(WINDOW, [left_paddle, right_paddle], ball, WIDTH, HEIGHT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        handle_key_paddle_movement(keys, left_paddle, right_paddle)

        ball.move(HEIGHT)

    pygame.quit()

if __name__ == '__main__':
    main()

import pygame
from game import Game

pygame.init()
pygame.display.set_caption("My Game")


# Примечание:
# Нужно чтобы высота и штрина экрана ровно делилаcь на STEP(шаг змейки)

STEP = 10

WIDTH = 800
HEIGHT = 600

RADIUS = 5
UPDATE_INTERVAL = 50

screen = pygame.display.set_mode([WIDTH, HEIGHT])

RUNNiNG = True

current_time = pygame.time.get_ticks()

game = Game(WIDTH, HEIGHT, screen, STEP, RADIUS, UPDATE_INTERVAL)

while RUNNiNG:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNiNG = False

    game.handle_events()
    if pygame.time.get_ticks() - current_time >= game.get_update_interval():
        game.update()
        game.draw()
        current_time = pygame.time.get_ticks()
    pygame.display.flip()

pygame.quit()

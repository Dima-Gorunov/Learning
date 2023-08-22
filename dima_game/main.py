import pygame

from game.game import Game
from test_screen import TestScreen


def main():
    pygame.init()
    pygame.display.set_caption("My Game")

    # Примечание:
    # Нужно чтобы высота и штрина экрана ровно и четно делилаcь на STEP(шаг змейки)

    STEP = 10

    WIDTH = 540
    HEIGHT = 180

    RADIUS = 5
    UPDATE_INTERVAL = 400

    screen = pygame.display.set_mode([WIDTH, HEIGHT])

    RUNNiNG = True

    current_time = pygame.time.get_ticks()

    game = Game(screen, STEP, RADIUS, UPDATE_INTERVAL)

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


if __name__ == '__main__':
    main()

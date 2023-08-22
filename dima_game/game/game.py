import pygame
from game.snake import Snake
from game.fruit import Fruit

from helpers.helpers import print_game_over


class Game:
    def __init__(self, screenVar=None, step=5, radius=2, update_interval=300):

        self.multiplier = 1
        self.shift = False
        self.start_update_interval = update_interval
        self.step = step
        self.radius = radius
        self.screen = screenVar
        self.snake = Snake(self.screen, self.step, self.radius)
        self.fruit = Fruit(self.screen, self.step, self.radius)
        self.update_interval = update_interval*self.multiplier

    def handle_events(self):
        keys = pygame.key.get_pressed()
        self.snake.change_direction(keys)
        self.change_shift(keys)

    def update(self):
        if self.snake.get_crash():
            return
        self.check_shift()
        self.snake.add_coordinates()
        self.snake.delete_back_side()
        if (self.snake.get_current_coordinates() == self.fruit.get_coordinates()):
            self.snake.add_length()
            self.fruit.generate_fruit(self.snake.get_segments())
        self.snake.check_out()
        self.snake.check_crush()

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.snake.print_snake(self.screen)
        self.fruit.print_fruit(self.screen)
        if self.snake.get_crash():
            print_game_over(self.screen)
            self.restart_game()

    def get_update_interval(self):
        return self.update_interval

    def set_update_interval(self, value):
        self.update_interval = int(value)

    def set_multiplier(self, value=1):
        self.multiplier = value

    def get_multiplier(self):
        return self.multiplier

    def restart_game(self):
        self.snake = Snake(self.screen, self.step, self.radius)
        self.fruit = Fruit(self.screen, self.step, self.radius)
        self.set_update_interval(self.start_update_interval)

    def set_shift(self, value):
        self.shift = value

    def get_shift(self):
        return self.shift

    def change_shift(self, keys):

        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            self.set_shift(True)
        else:
            self.set_shift(False)

    def check_shift(self):
        if self.get_shift():
            self.set_update_interval(self.start_update_interval*0.1)
        else:
            self.set_update_interval(self.start_update_interval)

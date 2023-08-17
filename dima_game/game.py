import pygame
from snake import Snake
from fruit import Fruit

from helpers import print_game_over


class Game:
    def __init__(self, width=800, height=600, screenVar=None, step=5, radius=2, update_interval=300):
        self.start_update_interval = update_interval
        self.step = step
        self.multiplier = 0.98
        self.radius = radius
        self.screen = screenVar
        self.width = width
        self.height = height
        self.snake = Snake(self.width, self.height, self.step, self.radius)
        self.fruit = Fruit(self.width, self.height, self.step, self.radius)
        self.update_interval = update_interval

    def handle_events(self):
        keys = pygame.key.get_pressed()
        self.snake.change_direction(keys)

    def update(self):
        if self.snake.get_crash():
            return
        self.snake.add_coordinates()
        self.snake.delete_back_side()
        if (self.snake.get_current_coordinates() == self.fruit.get_coordinates()):
            self.snake.add_length()
            self.fruit.generate_fruit(self.snake.get_segments())
            self.change_update_interval()
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
        self.update_interval = value

    def change_update_interval(self):
        self.update_interval *= self.multiplier

    def restart_game(self):
        self.snake = Snake(self.width, self.height, self.step, self.radius)
        self.fruit = Fruit(self.width, self.height, self.step, self.radius)
        self.set_update_interval(self.start_update_interval)

import pygame
from helpers.helpers import create_coordinate
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..'))


class Snake:
    def __init__(self, screen, step=5, radius=2):
        self.crash = False
        self.length = 1
        self.radius = radius
        self.fruit_needed = False
        self.step = step
        self.screen = screen
        self.direction = "down"
        self.last_direction = "down"
        self.current_coordinates = create_coordinate(
            self.screen.get_width()//2, self.screen.get_height()//2, radius)
        self.segments = [create_coordinate(
            self.screen.get_width()//2, self.screen.get_height()//2, radius)]

    def add_coordinates(self):
        if self.direction == "left":
            self.current_coordinates["coordinates"]["x"] -= self.step
        elif self.direction == "right":
            self.current_coordinates["coordinates"]["x"] += self.step
        elif self.direction == "up":
            self.current_coordinates["coordinates"]["y"] -= self.step
        elif self.direction == "down":
            self.current_coordinates["coordinates"]["y"] += self.step

        self.last_direction = self.direction
        new_x = self.current_coordinates["coordinates"]["x"]
        new_y = self.current_coordinates["coordinates"]["y"]
        self.current_coordinates = create_coordinate(new_x, new_y, self.radius)
        self.segments.append(self.current_coordinates)

    def delete_back_side(self):
        if len(self.segments)-1 > self.length:
            self.segments.pop(0)

    def change_direction(self, keys):
        if keys[pygame.K_LEFT] and self.last_direction != "right":
            self.direction = "left"
        elif keys[pygame.K_RIGHT] and self.last_direction != "left":
            self.direction = "right"
        elif keys[pygame.K_UP] and self.last_direction != "down":
            self.direction = "up"
        elif keys[pygame.K_DOWN] and self.last_direction != "up":
            self.direction = "down"

    def print_snake(self, screen):
        for item in self.segments:
            pygame.draw.circle(
                screen, item["color"], (item["coordinates"]["x"], item["coordinates"]["y"]), item["radius"])

    def get_current_coordinates(self):
        return self.current_coordinates["coordinates"]

    def add_length(self):
        self.length += 1

    def check_out(self):
        x, y = self.current_coordinates["coordinates"].values()
        if (x > self.screen.get_width() or x < 0) or (y < 0 or y > self.screen.get_height()):
            self.crash = True

    def check_crush(self):
        new_array = self.segments[:]
        new_array = new_array[:-2]
        if len(self.segments) > 4:
            for items in new_array:
                if items == self.current_coordinates:
                    self.crash = True

    def set_crash(self, value):
        self.crash = value

    def get_crash(self):
        return self.crash

    def get_segments(self):
        return self.segments

import pygame
import random


def create_coordinate(x=0, y=0, r=2, color=(0, 0, 255)):
    return {
        "radius": r,
        "color": color,
        "coordinates": {
            "x": x,
            "y": y
        },
    }


def print_arr(screen, arr):
    for item in arr:
        pygame.draw.circle(
            screen, item["color"], (item["coordinates"]["x"], item["coordinates"]["y"]), item["radius"])


def create_fruit_random_coordinates(screen_width, screen_height, snake_step, snake_segments):

    new_x = random.randint(1, ((screen_width/snake_step)-1))*snake_step
    new_y = random.randint(1, ((screen_height/snake_step)-1))*snake_step
    result = {
        "x": new_x,
        "y": new_y
    }
    for item in snake_segments:
        if (item["coordinates"]==result):
            return create_fruit_random_coordinates(screen_width, screen_height, snake_step, snake_segments) 

    return result


def match_check(coord, array_of_segments):
    for item in array_of_segments:
        if coord == item["coordinates"]:
            return True
    return False


def print_game_over(screen):
    font = pygame.font.Font(None, 36)
    text_surface = font.render("GAME OVER", True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.center = (screen.get_width() // 2, screen.get_height() // 2)
    pygame.draw.rect(screen, (0, 0, 0), text_rect)
    screen.blit(text_surface, text_rect)

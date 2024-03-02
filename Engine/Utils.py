import pygame
from Engine.Shared import Shared


def pos_between(pos_1, pos_2, check_pos) -> bool:
    pos1 = pygame.Vector2(pos_1)
    pos2 = pygame.Vector2(pos_2)
    check = pygame.Vector2(check_pos)
    if pos1.x < check.x < pos2.x and pos1.y < check.y < pos2.y:
        return True
    return False


def format_text(text, color=pygame.Color("white"), size=10, text_type="Times New Roman"):
    """function to generate text surface"""
    pygame.font.init()
    text_formate = pygame.font.SysFont(text_type, size)
    text_surface = text_formate.render(text, True, color)
    return text_surface


def get_size_from_percent(value: tuple) -> tuple:
    width = (Shared.display_resolution[0]/100) * value[0]
    height = (Shared.display_resolution[1]/100) * value[1]
    return (width, height)


def get_center_anchor(value: tuple) -> tuple:
    xpos = (Shared.display_resolution[0] - value[0]) / 2
    ypos = (Shared.display_resolution[1] - value[1]) / 2
    return (xpos, ypos)

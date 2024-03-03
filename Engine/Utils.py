import pygame
from Engine.Shared import Shared

pygame.font.init()


def pos_between(pos_1, pos_2, check_pos) -> bool:
    pos1 = pygame.Vector2(pos_1)
    pos2 = pygame.Vector2(pos_2)
    check = pygame.Vector2(check_pos)
    if pos1.x < check.x < pos2.x and pos1.y < check.y < pos2.y:
        return True
    return False


def get_size_from_percent(value: tuple) -> tuple:
    width = (Shared.display_resolution[0]/100) * value[0]
    height = (Shared.display_resolution[1]/100) * value[1]
    return (width, height)


def get_relative_size(target: tuple, destination: tuple) -> tuple:
    width = (destination[0] / 100) * target[0]
    height = (destination[1] / 100) * target[1]
    return (width, height)


def get_center_anchor_pos(target: pygame.Rect, destination: pygame.Rect) -> tuple:
    xpos = (destination.width/2) + destination.topleft[0]
    ypos = (destination.height/2) + destination.topleft[1]
    return (xpos, ypos)


def get_center_anchor_offset(target: pygame.Rect, destination: pygame.Rect) -> tuple:
    xpos = (destination.width - target.width)/2 + \
        destination.topleft[0]-target.topleft[0]
    ypos = (destination.height - target.height)/2 + \
        destination.topleft[1]-target.topleft[1]
    return (xpos, ypos)


def get_leftcenter_anchor_pos(target: pygame.Rect, destination: pygame.Rect) -> tuple:
    xpos = destination.left + target.width/2
    ypos = destination.center[1]
    return (xpos, ypos)


def get_rightcenter_anchor_pos(target: pygame.Rect, destination: pygame.Rect) -> tuple:
    xpos = destination.right - target.width/2
    ypos = destination.center[1]
    return (xpos, ypos)


def get_topleft_anchor_pos(target: pygame.Rect, destination: pygame.Rect) -> tuple:
    xpos = destination.topleft[0] + target.width/2
    ypos = destination.topleft[1] + target.height/2
    return (xpos, ypos)


def get_topleft_anchor_offset(target: pygame.Rect, destination: pygame.Rect) -> tuple:
    xpos = destination.topleft[0] + target.width/2 - target.topleft[0]
    ypos = destination.topleft[1] + target.height/2 - target.topleft[1]
    return (xpos, ypos)

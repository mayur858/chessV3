import pygame

all_sprites = pygame.sprite.Group()
cursor_pos: pygame.Vector2 = pygame.Vector2(0, 0)


def update_state():
    global cursor_pos

    cursor_pos = pygame.Vector2(pygame.mouse.get_pos())

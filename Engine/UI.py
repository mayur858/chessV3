import pygame
from Engine import Utils


class Panel(pygame.sprite.Sprite):
    def __init__(self, size: tuple = (100, 100), background: pygame.Color = pygame.Color("grey")) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.surface = pygame.Surface(Utils.get_size_from_persent(size))
        self.surface.fill(background)
        self.rect = self.surface.get_rect()
        self.sprites = pygame.sprite.Group()

    def update(self) -> None:
        if len(self.sprites):
            self.sprites.update()
            self.sprites.draw(self.display)


class Button:
    pass

import pygame
from Engine.App import App
from Engine import Utils

pygame.font.init()


def format_text(text, color=pygame.Color("white"), size=10, text_style="Times New Roman") -> pygame.Surface:
    """function to generate text surface"""
    text_formate = pygame.font.SysFont(text_style, size)
    text_surface = text_formate.render(text, False, color)
    return text_surface


class TextBox(pygame.sprite.Sprite):
    def __init__(self, text: str, size: int = 10, color: pygame.Color = pygame.Color("black"), text_style="Times New Roman"):
        pygame.sprite.Sprite.__init__(self)

        self.image = format_text(text, color, size, text_style)
        self.rect = self.image.get_rect()


class Panel(pygame.sprite.Sprite):
    def __init__(self, size: tuple, parent: pygame.Surface, anchor: str = "center", background: pygame.Color = pygame.Color("grey")):
        pygame.sprite.Sprite.__init__(self)

        self.parent = parent

        relative_size = Utils.get_relative_size(size, self.parent.get_size())
        self.image = pygame.Surface(relative_size)
        self.image.fill(background)
        self.rect = self.image.get_rect()
        self.set_anchor(anchor)
        self.sprites = pygame.sprite.Group()

    def set_anchor(self, anchor) -> None:
        if ("leftcenter" in anchor):
            self.rect.center = Utils.get_leftcenter_anchor_pos(
                self.rect, self.parent.get_rect())
        elif ("rightcenter" in anchor):
            self.rect.center = Utils.get_rightcenter_anchor_pos(
                self.rect, self.parent.get_rect())
        else:
            self.rect.center = Utils.get_center_anchor_pos(
                self.rect, self.parent.get_rect())

    def update(self) -> None:
        if len(self.sprites):
            self.sprites.update()
            self.sprites.draw(self.image)

        self.parent.blit(self.image, self.rect)

    def add_child(self, child: pygame.sprite):
        self.sprites.add(child)

    def remove_all_childs(self):
        self.sprites.empty()


class Grid(Panel):
    @classmethod
    def create_grid(cls, dimension: tuple, cellSize: tuple, parent: pygame.Surface):
        size = (dimension[0] * cellSize[0], dimension[1] * cellSize[1])
        self.dimension = dimension
        self.cellSize = cellSize
        self.child = 0
        return Grid(size, parent, "center")


class Button:
    pass

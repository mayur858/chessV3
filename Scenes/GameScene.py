from Engine.SceneManager import *
from Engine.App import App
from Engine.Utils import *
import pygame


class BoardBox(pygame.sprite.Sprite):
    def __init__(self, size=(100, 100), color=pygame.Color("white")):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.color = color

    def update_state(self, state: str):
        if "hover" in state:
            self.image.fill(pygame.Color("Yellow"))
        else:
            self.image.fill(pygame.Color(self.color))

    def update(self):
        if pos_between(self.rect.topleft, self.rect.bottomright, App.cursorPos):
            self.update_state("hover")
        else:
            self.update_state("empty")


class GameScene(Scene):
    def __init__(self):
        super().__init__("game")
        self.init_board()

    def update(self):
        super().update()
        for event in App.inputs:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    SceneManager.change_scene("menu")

    def init_board(self):
        for row in range(0, 8):
            for col in range(0, 8):
                box = BoardBox(color=pygame.Color("black") if (row + col) % 2 == 0 else pygame.Color("white"))
                box.rect.topleft = (col * box.rect.width, row * box.rect.height)
                self.all_sprites.add(box)


GameScene()

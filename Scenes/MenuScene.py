from Engine import Utils
from Engine.SceneManager import *
from Engine.App import App
import pygame


class MenuScene(Scene):
    def __init__(self):
        super().__init__("menu")
        self.hint = Utils.format_text("Press Enter To Start",
                                      pygame.Color("black"), 50)
        self.hintRect = self.hint.get_rect()

        delta = Utils.get_center_anchor(self.hintRect.size)
        self.hintRect = self.hintRect.move(delta)

    def update(self):
        for event in App.inputs:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    SceneManager.change_scene("game")

        self.display.blit(self.hint, self.hintRect)

from Engine.Utils import format_text
from Engine.SceneManager import *
from Engine.App import App
import pygame


class MenuScene(Scene):
    def __init__(self):
        super().__init__("menu")
        self.hint = format_text("Press Enter To Continue",
                                pygame.Color("black"), 50)

    def update(self):
        for event in App.inputs:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    SceneManager.change_scene("game")

        self.display.blit(self.hint, self.hint.get_rect())


MenuScene()

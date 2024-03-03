from Engine import Utils
from Engine.SceneManager import *
from Engine.App import App
from Engine import UI
import pygame


class MenuScene(Scene):
    def __init__(self):
        super().__init__("menu")
        self.panel = UI.Panel((100, 100), self.display,
                              "center")
        self.hint = UI.TextBox("Press Enter To start", 50)
        self.hint.rect.center = Utils.get_center_anchor_pos(
            self.hint.rect, self.panel.rect)
        self.panel.add_child(self.hint)

    def update(self):
        for event in App.inputs:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    SceneManager.change_scene("game")

        self.panel.update()

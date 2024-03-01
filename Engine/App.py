import pygame
from Engine.SceneManager import *


class App:
    display: pygame.Surface = None
    display_resolution: tuple = (500, 500)

    background: pygame.Color = None
    running: bool = False
    cursorPos: pygame.Vector2 = pygame.Vector2(0, 0)

    inputs = None

    def __init__(self, app_name: str, resolution: tuple = (500, 500), background: pygame.Color = pygame.Color("grey")):
        App.display_resolution = resolution
        App.display = pygame.display.set_mode(resolution)
        App.background = background
        pygame.display.set_caption(app_name)

        SceneManager.display = App.display

    def start(self):
        if self.display is None:
            raise Exception("No app created : Create app using App.Create() ")
        else:
            self.running = True
            self.update_loop()

    def update_loop(self):
        while self.running:

            App.cursorPos = pygame.mouse.get_pos()
            App.inputs = pygame.event.get()
            for event in App.inputs:
                if event.type == pygame.QUIT:
                    self.running = False
                    continue

            self.display.fill(self.background)
            SceneManager.update_scene()
            pygame.display.flip()

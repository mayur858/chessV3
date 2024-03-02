import pygame
from Engine.SceneManager import SceneManager
from Engine.Shared import Shared


class App(Shared):
    background: pygame.Color = None

    inputs = None

    def __init__(self, app_name: str, resolution: tuple = (500, 500), background: pygame.Color = pygame.Color("grey")) -> None:
        self.set_display(resolution)
        type(self).background = background
        pygame.display.set_caption(app_name)

    def start(self) -> None:
        if self.display is None:
            raise Exception("No app created : Create app using App.Create() ")
        else:
            self.running = True
            self.update_loop()

    def update_loop(self) -> None:
        while self.running:

            type(self).cursorPos = pygame.mouse.get_pos()
            type(self).inputs = pygame.event.get()
            for event in App.inputs:
                if event.type == pygame.QUIT:
                    self.running = False
                    continue

            self.display.fill(self.background)
            SceneManager.update_scene()
            pygame.display.flip()

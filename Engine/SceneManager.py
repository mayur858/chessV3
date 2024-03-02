import pygame
from Engine.Shared import Shared


class SceneManager(Shared):
    scenes: dict = dict()
    active_scene = None

    @classmethod
    def add_scene(cls, name: str, scene) -> None:
        if name in cls.scenes.keys():
            raise Exception("Scene with name " + name +
                            " already exist in the app")

        cls.scenes.update({name: scene})

    @classmethod
    def change_scene(cls, name: str) -> None:
        if name in cls.scenes.keys():
            if cls.active_scene is not None:
                cls.active_scene.on_unloaded()
            cls.active_scene = cls.scenes[name]
            cls.active_scene.on_loaded()
        else:
            raise Exception("No scene like " + name + " is added in game")

    @classmethod
    def update_scene(cls) -> None:
        if cls.active_scene is not None:
            cls.active_scene.update()


class Scene(Shared):
    def __init__(self, name) -> None:
        self.name = name
        self.sprites = pygame.sprite.Group()
        SceneManager.add_scene(name, self)

    def update(self) -> None:
        if len(self.sprites):
            self.sprites.update()
            self.sprites.draw(self.display)

    def on_loaded(self) -> None:
        print(self.name + " scene loaded")

    def on_unloaded(self):
        print(self.name + " scene unloaded")

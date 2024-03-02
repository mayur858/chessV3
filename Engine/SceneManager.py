import pygame


class SceneManager:
    scenes: dict = dict()
    active_scene = None
    display = None

    @classmethod
    def add_scene(cls, name: str, scene):
        if name in cls.scenes.keys():
            raise Exception("Scene with name " + name + " already exist in the app")
            return

        cls.scenes.update({name: scene})

    @classmethod
    def change_scene(cls, name: str):
        if name in cls.scenes.keys():
            if cls.active_scene is not None:
                cls.active_scene.on_unloaded()
            cls.active_scene = cls.scenes[name]
            cls.active_scene.on_loaded()
        else:
            raise Exception("No scene like " + name + " is added in game")

    @classmethod
    def update_scene(cls):
        if cls.active_scene is not None:
            cls.active_scene.update()


class Scene:
    def __init__(self, name):
        self.name = name
        self.all_sprites = pygame.sprite.Group()
        SceneManager.add_scene(name, self)

    def update(self):
        if len(self.all_sprites):
            self.all_sprites.update()
            self.all_sprites.draw(SceneManager.display)

    def on_loaded(self):
        print(self.name + " scene loaded")

    def on_unloaded(self):
        print(self.name + " scene unloaded")

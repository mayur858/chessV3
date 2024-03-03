from Engine.App import *
from Engine.SceneManager import SceneManager
from Scenes.MenuScene import MenuScene
from Scenes.GameScene import GameScene


def create_scenes():
    MenuScene()
    GameScene()


def run_game():
    game = App("Chess", (1000, 800))
    create_scenes()
    game.start()


run_game()

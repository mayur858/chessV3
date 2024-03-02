from Engine.App import *
from Engine.SceneManager import SceneManager
import Scenes.GameScene
import Scenes.MenuScene


def run_game():
    game = App("Chess", (1000, 800))
    print(game.display, Shared.display)
    SceneManager.change_scene("menu")
    game.start()


run_game()

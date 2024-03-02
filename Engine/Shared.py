import pygame


class Shared:
    display: pygame.Surface = None
    display_resolution: tuple = (500, 500)
    _cursorPos: pygame.Vector2 = pygame.Vector2(0, 0)

    running: bool = False

    def set_display(self, resolution: tuple) -> None:
        Shared.display_resolution = resolution
        Shared.display = pygame.display.set_mode(resolution)

    @property
    def cursorPos(self) -> pygame.Vector2:
        return self._cursorPos

    @cursorPos.setter
    def cursorPos(self, value) -> None:
        if (type(value) is tuple or type(value) is list) and len(value) == 2:
            self._cursorPos = pygame.Vector2(value)
        elif type(value) is pygame.Vector2:
            self._cursorPos = value
        else:
            raise Exception(
                "Value Mismatch : Value type must be tuple or list ot Vector2 not " + type(value))

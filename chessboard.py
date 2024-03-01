import pygame
import common

chess_board = list()


class BoardBox(pygame.sprite.Sprite):
    def __init__(self, size=(100, 100), color=pygame.Color("white")):
        super().__init__()

        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.color = color

    def update_state(self, state: str):
        if "hover" in state:
            self.image.fill(pygame.Color("Yellow"))
        else:
            self.image.fill(pygame.Color(self.color))

    def update(self):
        if self.rect.topleft[0] < common.cursor_pos.x < self.rect.bottomright[0] and self.rect.topleft[
            1] < common.cursor_pos.y < self.rect.bottomright[1]:
            self.update_state("hover")
        else:
            self.update_state("empty")


def init_board():
    global chess_board
    for row in range(0, 8):
        col_list = list()
        for col in range(0, 8):
            box = BoardBox(color=pygame.Color("black") if (row + col) % 2 == 0 else pygame.Color("white"))
            col_list.append(box)
            box.rect.topleft = (col * box.rect.width, row * box.rect.height)

        chess_board.append(col_list)
        common.all_sprites.add(col_list)

import pygame
import common
import chessboard

display = pygame.display.set_mode((1000, 800))
game_on = False


def game_loop():
    global game_on

    game_on = True
    chessboard.init_board()

    while game_on:
        common.update_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False
                return

        display.fill(pygame.Color("grey"))
        common.all_sprites.update()
        common.all_sprites.draw(display)
        pygame.display.flip()


game_loop()

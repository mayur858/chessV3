from Engine.SceneManager import *
from Engine.App import App
from Engine.Utils import *
from Engine import UI
import pygame
import chess

chessPieces: dict = {'b': pygame.transform.scale(pygame.image.load("Assets\\black_bishop.png"), (100, 100)),
                     'k': pygame.transform.scale(pygame.image.load("Assets\\black_king.png"), (100, 100)),
                     'p': pygame.transform.scale(pygame.image.load("Assets\\black_pawn.png"), (100, 100)),
                     'q': pygame.transform.scale(pygame.image.load("Assets\\black_queen.png"), (100, 100)),
                     'r': pygame.transform.scale(pygame.image.load("Assets\\black_rook.png"), (100, 100)),
                     'n': pygame.transform.scale(pygame.image.load("Assets\\black_knight.png"), (100, 100)),
                     'B': pygame.transform.scale(pygame.image.load("Assets\\white_bishop.png"), (100, 100)),
                     'K': pygame.transform.scale(pygame.image.load("Assets\\white_king.png"), (100, 100)),
                     'P': pygame.transform.scale(pygame.image.load("Assets\\white_pawn.png"), (100, 100)),
                     'Q': pygame.transform.scale(pygame.image.load("Assets\\white_queen.png"), (100, 100)),
                     'R': pygame.transform.scale(pygame.image.load("Assets\\white_rook.png"), (100, 100)),
                     'N': pygame.transform.scale(pygame.image.load("Assets\\white_knight.png"), (100, 100))}


class BoardBox(pygame.sprite.Sprite):
    allBoxes: list = list()

    def __init__(self, size=(100, 100), color=pygame.Color("white")):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.color = color
        self.curPiece: str = '.'
        self.boardPos: str = ''
        self.hover: bool = False
        self.selected: bool = False

        type(self).allBoxes.append(self)

    def update_state(self, state: str):
        if "hover" in state:
            self.image.fill(pygame.Color("Yellow"))
        elif "selected" in state:
            self.image.fill(pygame.Color("green"))
        else:
            self.image.fill(pygame.Color(self.color))

    def update(self):
        if self.rect.collidepoint(App.cursorPos):
            self.update_state("hover")
            self.hover = True
        else:
            self.update_state("selected"if self.selected else "empty")
            self.hover = False

        if self.curPiece in chessPieces.keys():
            self.image.blit(chessPieces[self.curPiece], (0, 0, 100, 100))

    @classmethod
    def get_selected(cls):
        for box in cls.allBoxes:
            if box.selected:
                return box
        return None

    @classmethod
    def get_hovering(cls):
        for box in cls.allBoxes:
            if box.hover:
                return box
        return None


class GameScene(Scene):
    def __init__(self):
        super().__init__("game")
        self.board = None
        self.visualBoard = UI.Grid(
            (8, 8), (100, 100), self.display, "leftcenter")

    def on_loaded(self) -> None:
        self.board = chess.Board()
        self.init_board()

    def update(self):
        for event in App.inputs:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    SceneManager.change_scene("menu")
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.on_select_button()

        self.update_board()
        self.visualBoard.update()
        if self.board.is_checkmate():
            print("Check Mate\nWinner Is", end=' ')
            print("BLACK" if self.board.turn else "WHITE")
            SceneManager.change_scene("menu")
            return

    def on_unloaded(self) -> None:
        super().on_unloaded()
        self.board = None
        self.visualBoard.clear()
        BoardBox.allBoxes.clear()

    def init_board(self):
        alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        for row in range(0, 8):
            for col in range(0, 8):
                color = "brown" if (row + col) % 2 == 0 else "white"
                box = BoardBox(color=pygame.Color(color))
                box.boardPos = alpha[col]+str(8-row)
                self.visualBoard.add_child(box)

    def update_board(self) -> None:
        board = list(str(self.board).replace(' ', '').split('\n'))
        for row in range(0, 8):
            for col in range(0, 8):
                self.visualBoard.grid[row][col].curPiece = board[row][col]

    def on_select_button(self) -> bool:
        hoverBox = BoardBox.get_hovering()
        selectedBox = BoardBox.get_selected()

        if hoverBox == selectedBox == None:
            return False

        if selectedBox == None:
            if '.' not in hoverBox.curPiece:
                hoverBox.selected = True
        else:
            if hoverBox == None or selectedBox == hoverBox:
                selectedBox.selected = False
            else:
                if self.player_move(selectedBox.boardPos+hoverBox.boardPos):
                    selectedBox.selected = False
                else:
                    selectedBox.selected = False
                    if '.' not in hoverBox.curPiece:
                        hoverBox.selected = True

        return True

    def player_move(self, move: str) -> bool:
        uci_move = chess.Move.from_uci(move)
        if uci_move in self.board.legal_moves:
            self.board.push_uci(move)
            return True
        return False

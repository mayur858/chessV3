import chess

board = chess.Board()


def game_loop():
    print(board, "\n")
    while True:

        print(board.legal_moves, "\n")
        ch = input("\nEnter Next Move : ").lower()
        if "exit" in ch:
            return

        try:
            board.push_san(ch)
        except ValueError:
            print("Move Is Invalid \n Type a valid Move")

        print("\n")
        print(board, "\n")

        if board.is_checkmate():
            print("\nGAME OVER")
            return

        if board.is_stalemate():
            print("\nGAME DRAW")
            return
        
        if board.is_insufficient_material():
            print('Draw')
            return


game_loop()

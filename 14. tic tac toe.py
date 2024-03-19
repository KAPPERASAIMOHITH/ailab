import numpy as np
import random
from time import sleep

def create_board():
    return np.zeros((3, 3), dtype=int)

def random_place(board, player):
    empty_spots = [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]
    if empty_spots:
        i, j = random.choice(empty_spots)
        board[i][j] = player
    return board

def check_win(board, player):
    return any(np.all(board == player, axis=axis).any() for axis in (0, 1, None)) or \
           np.all(np.diag(board) == player) or \
           np.all(np.diag(np.fliplr(board)) == player)


def play_game():
    board = create_board()
    print(board)
    sleep(2)

    for counter in range(1, 10):
        for player in [1, 2]:
            board = random_place(board, player)
            print(f"Board after {counter} move")
            print(board)
            sleep(2)
            if check_win(board, player):
                return player
    return -1

print("Winner is:", play_game())

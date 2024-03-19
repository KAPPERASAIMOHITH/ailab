def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check if there is a queen in the left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check if there is a queen in the right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 'Q':
            return False

    return True

def solve_queens(board, row):
    if row == len(board):
        # All queens are placed, print the solution
        print_board(board)
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            # Place queen and move to the next row
            board[row][col] = 'Q'
            solve_queens(board, row + 1)
            # Backtrack by removing the queen
            board[row][col] = '.'

if __name__ == "__main__":
    # Initialize an 8x8 chessboard with empty cells
    chessboard = [['.' for _ in range(8)] for _ in range(8)]

    # Start placing queens from the first row
    solve_queens(chessboard, 0)

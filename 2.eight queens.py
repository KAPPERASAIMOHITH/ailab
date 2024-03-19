def under_attack(col, queens):
    left = right = col
    for r, c in reversed(queens):
        left, right = left - 1, right + 1
        if c in (left, col, right):
            return True
    return False

def solve(n):
    if n == 0: return [[]]
    smaller_solutions = solve(n - 1)
    return [solution + [(n, i + 1)] for i in range(BOARD_SIZE) for solution in smaller_solutions if not under_attack(i + 1, solution)]

BOARD_SIZE = 8
solutions = solve(BOARD_SIZE)
for answer in solutions:
    if len(answer) == BOARD_SIZE:
        break

# Print chessboard with queens
for row in range(BOARD_SIZE):
    for col in range(BOARD_SIZE):
        print('Q' if (row + 1, col + 1) in answer else '*', end=' ')
    print()

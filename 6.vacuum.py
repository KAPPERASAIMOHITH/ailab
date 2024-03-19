def clean(floor):
    for i in range(len(floor)):
        for j in range(len(floor[0])):
            if floor[i][j] == 1:
                print_floor(floor, i, j)
                floor[i][j] = 0
                print_floor(floor, i, j)

def print_floor(floor, row, col):
    for r in range(len(floor)):
        for c in range(len(floor[0])):
            print(f" >{floor[r][c]}< " if r == row and c == col else f"  {floor[r][c]}  ", end='')
        print()

def main():
    m = int(input("Enter the No. of Rows: "))
    n = int(input("Enter the No. of Columns: "))
    print("Enter clean status for each cell (1 - dirty, 0 - clean)")
    floor = [list(map(int, input().split())) for _ in range(m)]
    clean(floor)

main()

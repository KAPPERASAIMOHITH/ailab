import heapq

def solve_puzzle(initial):
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    moves = [1, -1, 3, -3]  # Simplified moves considering the flat list
    open_list, closed_set = [(0, initial, [])], set()

    while open_list:
        _, current, path = heapq.heappop(open_list)
        if current == goal:
            return path + [current]
        closed_set.add(current)

        empty = current.index(0)
        for m in moves:
            if 0 <= empty // 3 + m // 3 < 3 and m + empty in range(9):  # Check valid moves considering edges
                neighbor = list(current)
                neighbor[empty], neighbor[empty + m] = neighbor[empty + m], neighbor[empty]
                neighbor_tuple = tuple(neighbor)
                if neighbor_tuple not in closed_set:
                    heapq.heappush(open_list, (len(path) + 1, neighbor_tuple, path + [current]))

    return []

def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print('---')

initial_state = (1, 0, 3, 4, 2, 5, 7, 8, 6)
solution_path = solve_puzzle(initial_state)

if solution_path:
    print("Solution path:")
    for step in solution_path:
        print_state(step)
else:
    print("No solution found.")

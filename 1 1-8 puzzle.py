import heapq

initial_state = (1, 0, 3, 4, 2, 5, 7, 8, 6)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
moves = [1, -1, 3, -3]
open_list, closed_set = [(0, initial_state, [])], set()

while open_list:
    _, current, path = heapq.heappop(open_list)
    if current == goal:
        print("Solution Found:")
        for state in path + [current]:
            print("\n".join(" ".join(map(str, state[i:i+3])) for i in range(0, 9, 3)), "\n")
        break
    closed_set.add(current)
    empty = current.index(0)
    for m in moves:
        next_pos = empty + m
        if 0 <= next_pos < 9 and abs(empty // 3 - next_pos // 3) + abs(empty % 3 - next_pos % 3) == 1:
            neighbor = list(current)
            neighbor[empty], neighbor[next_pos] = neighbor[next_pos], neighbor[empty]
            neighbor_tuple = tuple(neighbor)
            if neighbor_tuple not in closed_set:
                heapq.heappush(open_list, (len(path) + 1, neighbor_tuple, path + [current]))

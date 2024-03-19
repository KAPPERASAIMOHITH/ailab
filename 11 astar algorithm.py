import heapq

def a_star(start, goal, grid_size):
    open_set = [(0, start)]
    came_from = {}
    g_score = {start: 0}
    h = lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1])  # Manhattan distance
    neighbors = lambda x: [(x[0] + dx, x[1] + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)] if 0 <= x[0] + dx < grid_size and 0 <= x[1] + dy < grid_size]

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal: return reconstruct_path(came_from, current)
        for neighbor in neighbors(current):
            tentative_g_score = g_score[current] + 1
            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + h(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))

def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    return path[::-1]

# Usage
grid_size = 5
start, goal = (0, 0), (4, 4)
path = a_star(start, goal, grid_size)
print("Path:", path)

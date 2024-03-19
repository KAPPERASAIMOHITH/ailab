from queue import PriorityQueue

def best_first_search(graph, start, goal, heuristic):
    visited, queue = set(), PriorityQueue()
    queue.put((heuristic[start], start))

    while queue:
        _, current = queue.get()

        if current == goal:
            print("Goal reached!")
            return

        if current not in visited:
            print(current, end=' ')
            visited.add(current)
            for neighbor in graph.get(current, {}):
                if neighbor not in visited:
                    queue.put((heuristic[neighbor], neighbor))

# Simple example usage:
graph = {'A': {'B': 2, 'C': 1}, 'B': {'A': 2, 'D': 3}, 'C': {'A': 1, 'E': 4}, 'D': {'B': 3}, 'E': {'C': 4}}
heuristic = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1}

start, goal = 'A', 'E'

print("Best-First Search path from", start, "to", goal, ":")
best_first_search(graph, start, goal, heuristic)

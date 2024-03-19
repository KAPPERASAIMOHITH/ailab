from queue import PriorityQueue

def best_first_search(graph, start, goal, heuristic):
    visited, queue = set(), PriorityQueue()
    queue.put((heuristic[start], start))

    while queue:
        _, current = queue.get()

        if current in visited:
            continue

        print(current, end=' ')
        visited.add(current)

        if current == goal:
            print("\nGoal reached!")
            return

        for neighbor, _ in graph.get(current, {}).items():
            if neighbor not in visited:
                queue.put((heuristic[neighbor], neighbor))

# Example usage:
graph = {'A': {'B': 4, 'H': 8}, 'B': {'A': 4, 'C': 8, 'H': 11}, 'C': {'B': 8, 'D': 7, 'F': 4, 'I': 2},
         'D': {'C': 7, 'E': 9, 'F': 14}, 'E': {'D': 9, 'F': 10}, 'F': {'C': 4, 'D': 14, 'E': 10, 'G': 2},
         'G': {'F': 2, 'H': 1, 'I': 6}, 'H': {'A': 8, 'B': 11, 'G': 1, 'I': 7}, 'I': {'C': 2, 'G': 6, 'H': 7}}

heuristic = {'A': 12, 'B': 10, 'C': 7, 'D': 6, 'E': 4, 'F': 6, 'G': 4, 'H': 8, 'I': 3}

start, goal = 'A', 'I'

print("Best-First Search path from", start, "to", goal, ":")
best_first_search(graph, start, goal, heuristic)

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=' ')

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example usage:
# Create a sample graph represented as an adjacency list
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2, 3]
}

print("Depth-First Traversal (DFS) starting from vertex 2:")
dfs(graph, 2)

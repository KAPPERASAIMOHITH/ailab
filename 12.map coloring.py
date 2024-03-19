def greedy_coloring(graph):
    colored_nodes = {}

    for node in graph:
        used_colors = {colored_nodes[neighbor] for neighbor in graph[node] if neighbor in colored_nodes}
        colored_nodes[node] = next(color for color in ['Red', 'Green', 'Blue'] if color not in used_colors)

    return colored_nodes

# Example usage:
if __name__ == "__main__":
    map_graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D'],
        'D': ['B', 'C']
    }

    coloring_result = greedy_coloring(map_graph)

    print("Colored Map:")
    for node, color in coloring_result.items():
        print(f"Region {node} is colored {color}")


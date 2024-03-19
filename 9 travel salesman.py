from itertools import permutations

def tsp(cities, distances):
    # Generate all possible city sequences
    all_routes = permutations(range(1, len(cities)))  # Exclude starting city for permutations
    min_route = None
    min_distance = float('inf')
    
    for route in all_routes:
        distance = distances[0][route[0]] + sum(distances[route[i]][route[i+1]] for i in range(len(route)-1)) + distances[route[-1]][0]
        
        if distance < min_distance:
            min_route = route
            min_distance = distance
    
    return [cities[0]] + [cities[i] for i in min_route] + [cities[0]], min_distance

# Example usage
cities = ['A', 'B', 'C', 'D']
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

route, distance = tsp(cities, distances)
print(f"Shortest route: {route} with distance {distance}")

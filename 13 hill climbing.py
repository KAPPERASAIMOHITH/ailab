import random

def hill_climbing(initial_state, goal_state, heuristic, neighbors):
    current_state = initial_state
    
    while True:
        if current_state == goal_state:
            return current_state
        
        next_states = neighbors(current_state)
        next_states.sort(key=lambda state: heuristic(state, goal_state))
        
        if heuristic(next_states[0], goal_state) >= heuristic(current_state, goal_state):
            return current_state
        
        current_state = next_states[0]

# Example usage
def heuristic(state, goal_state):
    return sum(abs(state[i] - goal_state[i]) for i in range(len(state)))

def neighbors(state):
    neighbors = []
    for i in range(len(state)):
        neighbor = list(state)
        neighbor[i] += random.choice([-1, 1])
        neighbors.append(tuple(neighbor))
    return neighbors

initial_state = (0, 0, 0)
goal_state = (5, 5, 5)

result = hill_climbing(initial_state, goal_state, heuristic, neighbors)
print("Result:", result)

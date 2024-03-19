import math, random

def simulated_annealing(cost_func, start_temp, cooling_rate):
    state = current = random.uniform(-10, 10)
    temp = start_temp

    while temp > 0.001:
        new_state = current + random.uniform(-1, 1)
        cost_diff = cost_func(new_state) - cost_func(current)

        if cost_diff < 0 or math.exp(-cost_diff / temp) > random.random():
            state = new_state

        current = new_state
        temp *= cooling_rate

    return state

cost_func = lambda x: (x ** 2) - (10 * math.cos(2 * math.pi * x)) + 10  # Rastrigin function simplified to 1D
start_temp, cooling_rate = 1000, 0.98

print("Optimum:", simulated_annealing(cost_func, start_temp, cooling_rate))

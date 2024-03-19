from collections import deque

def solve(jug1, jug2, target):
    visited = set()
    q = deque([(0, 0)])
    path = []

    while q:
        u = q.popleft()
        if u in visited or u[0] > jug1 or u[1] > jug2 or u[0] < 0 or u[1] < 0:
            continue
        visited.add(u)
        path.append(u)

        if target in u:
            if target == u[0]:
                path.append((u[0], 0))
            else:
                path.append((0, u[1]))
            for step in path:
                print(f"({step[0]}, {step[1]})")
            return

        q.append((jug1, u[1]))  # Fill jug1
        q.append((u[0], jug2))  # Fill jug2
        q.append((0, u[1]))     # Empty jug1
        q.append((u[0], 0))     # Empty jug2

        # Transfer jug1 -> jug2
        transfer = min(u[0], jug2 - u[1])
        q.append((u[0] - transfer, u[1] + transfer))

        # Transfer jug2 -> jug1
        transfer = min(u[1], jug1 - u[0])
        q.append((u[0] + transfer, u[1] - transfer))

    print("Solution not possible")

if __name__ == '__main__':
    jug1, jug2, target = 4, 3, 2
    print("Path from initial state to solution state:")
    solve(jug1, jug2, target)

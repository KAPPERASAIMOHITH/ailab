from collections import deque

jug1, jug2, target = 4, 3, 2
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
        path.append((u[0], 0) if target == u[0] else (0, u[1]))
        [print(f"({step[0]}, {step[1]})") for step in path]
        break

    for v, w in [(jug1, u[1]), (u[0], jug2), (0, u[1]), (u[0], 0),
                 (u[0] - min(u[0], jug2 - u[1]), u[1] + min(u[0], jug2 - u[1])),
                 (u[0] + min(u[1], jug1 - u[0]), u[1] - min(u[1], jug1 - u[0]))]:
        q.append((v, w))
else:
    print("Solution not possible")

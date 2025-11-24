from collections import deque

input = open(0).read().strip().split(",")
walls = set()
r, c = 0, 0
dr, dc = -1, 0
for x in input:
    d, n = x[0], int(x[1:])
    if d == "L":
        dr, dc = -dc, dr
    else:
        dr, dc = dc, -dr
    for _ in range(n):
        r, c = r + dr, c + dc
        walls.add((r, c))

goal = (r, c)
seen = set()
queue = deque([((0, 0), 0)])
while queue:
    pos, steps = queue.popleft()
    if pos == goal:
        print(steps)
        break

    if pos in seen or pos in walls:
        continue
    seen.add(pos)

    r, c = pos
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        queue.append(((r + dr, c + dc), steps + 1))

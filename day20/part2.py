from collections import deque

grid = open(0).read().splitlines()
rows, cols = len(grid), len(grid[0])
start = (rows - 1, cols // 2)

seen = set()
queue = deque([(start, 0)])
while queue:
    pos, steps = queue.popleft()

    r, c = pos
    if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] in ".#":
        continue

    if grid[r][c] == "E":
        print(steps)
        exit()

    if pos in seen:
        continue
    seen.add(pos)

    queue.append(((r, c - 1), steps + 1))
    queue.append(((r, c + 1), steps + 1))
    queue.append(((r - 1, c) if (r + c) % 2 == 0 else (r + 1, c), steps + 1))

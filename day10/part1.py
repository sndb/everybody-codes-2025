from collections import deque

grid = open(0).read().splitlines()
rows, cols = len(grid), len(grid[0])

seen = set()
queue = deque([(0, rows // 2, cols // 2)])
while queue:
    moves, r, c = queue.popleft()
    if (r, c) in seen or moves > 4:
        continue
    seen.add((r, c))

    for nr, nc in [
        [r - 2, c - 1],
        [r - 2, c + 1],
        [r - 1, c - 2],
        [r - 1, c + 2],
        [r + 1, c - 2],
        [r + 1, c + 2],
        [r + 2, c - 1],
        [r + 2, c + 1],
    ]:
        if 0 <= nr < rows and 0 <= nc < cols:
            queue.append((moves + 1, nr, nc))

print(sum(grid[r][c] == "S" for r, c in seen))

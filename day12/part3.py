from collections import deque

grid = open(0).read().splitlines()
rows, cols = len(grid), len(grid[0])

result = set()

for _ in range(3):
    best = set()
    for r in range(rows):
        for c in range(cols):
            seen = {(r, c)}
            queue = deque(seen)
            while queue:
                pr, pc = queue.popleft()
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = pr + dr, pc + dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue

                    if (
                        grid[nr][nc] <= grid[pr][pc]
                        and (nr, nc) not in result
                        and (nr, nc) not in seen
                    ):
                        seen.add((nr, nc))
                        queue.append((nr, nc))

            if len(seen) > len(best):
                best = seen

    result |= best

print(len(result))

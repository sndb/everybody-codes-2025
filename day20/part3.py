from collections import deque

grid = open(0).read().splitlines()
rows, cols = len(grid), len(grid[0])
start = (rows - 1, cols // 2)

def scan_rows(grid):
    new_grid = []
    for i in range(cols):
        r, c = 0, cols - (2 * i) - 1
        dr, dc = 0, -1

        row = ["." * i]
        while 0 <= r < rows and 0 <= c < cols and grid[r][c] != ".":
            row.append(grid[r][c])
            r, c = r + dr, c + dc
            dr, dc = (1, 0) if dr == 0 else (0, -1)
        row += ["." * i]

        if set(row) == {"."}:
            break

        new_grid.append("".join(row))

    return new_grid

grid_r = scan_rows(grid)
grid_rr = scan_rows(grid_r)
grids = [grid, grid_rr, grid_r]

seen = set()
queue = deque([(start, 0, 0)])
while queue:
    pos, rot, steps = queue.popleft()
    curr_grid = grids[rot]
    rot = (rot + 1) % 3

    r, c = pos
    if r < 0 or r >= rows or c < 0 or c >= cols or curr_grid[r][c] in ".#":
        continue

    if curr_grid[r][c] == "E":
        print(steps)
        exit()

    if (rot, pos) in seen:
        continue
    seen.add((rot, pos))

    queue.append(((r, c), rot, steps + 1))
    queue.append(((r, c - 1), rot, steps + 1))
    queue.append(((r, c + 1), rot, steps + 1))
    queue.append(((r - 1, c) if (r + c) % 2 == 0 else (r + 1, c), rot, steps + 1))

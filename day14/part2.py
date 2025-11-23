grid = [list(line) for line in open(0).read().splitlines()]
rows, cols = len(grid), len(grid[0])
result = 0

for _ in range(2025):
    next = [["."] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            count = 0
            for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    count += grid[nr][nc] == "#"

            if grid[r][c] == "#":
                if count % 2 != 0:
                    next[r][c] = "#"
            else:
                if count % 2 == 0:
                    next[r][c] = "#"

    grid = next
    result += sum(c == "#" for row in grid for c in row)

print(result)

grid = open(0).read().splitlines()
rows, cols = len(grid), len(grid[0])

result = 0
for r, row in enumerate(grid):
    for c, x in enumerate(row):
        if x == "T":
            result += c < cols - 1 and row[c + 1] == "T"
            result += (
                r < rows - 1
                and grid[r + 1][c] == "T"
                and (r + c) % 2 != 0
                and (r + 1 + c) % 2 == 0
            )

print(result)

grid = [list(line) for line in open(0).read().splitlines()]

cr, cc = 0, 0
for r, row in enumerate(grid):
    for c, x in enumerate(row):
        if x == "@":
            cr, cc = r, c

radius = 0
destruction = 0
for i in range(len(grid)):
    delta = 0
    for r, row in enumerate(grid):
        for c, x in enumerate(row):
            if x != "@" and abs(r - cr) ** 2 + abs(c - cc) ** 2 <= i * i:
                delta += int(x)
                grid[r][c] = "0"

    if delta > destruction:
        destruction = delta
        radius = i

print(destruction * radius)

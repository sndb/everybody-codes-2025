grid = [list(line) for line in open(0).read().splitlines()]

cr, cc = 0, 0
for r, row in enumerate(grid):
    for c, x in enumerate(row):
        if x == "@":
            cr, cc = r, c

result = 0
for r, row in enumerate(grid):
    for c, x in enumerate(row):
        if x != "@" and abs(r - cr) ** 2 + abs(c - cc) ** 2 <= 100:
            result += int(x)

print(result)

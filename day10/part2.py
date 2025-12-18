grid = open(0).read().splitlines()
rows, cols = len(grid), len(grid[0])

sheep = set()
dragons = set()
for r in range(rows):
    for c in range(cols):
        match grid[r][c]:
            case "S":
                sheep.add((r, c))
            case "D":
                dragons.add((r, c))

def eaten(r, c):
    return r < rows and grid[r][c] != "#" and (r, c) in dragons

result = 0
for _ in range(20):
    next_dragons = set()
    for r, c in dragons:
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
                next_dragons.add((nr, nc))
    dragons = next_dragons

    next_sheep = set()
    for r, c in sheep:
        if not eaten(r, c) and not eaten(r + 1, c):
            next_sheep.add((r + 1, c))
    result += len(sheep) - len(next_sheep)
    sheep = next_sheep

print(result)

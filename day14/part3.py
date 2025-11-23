pattern = [list(line) for line in open(0).read().splitlines()]

size = 34
grid = [["."] * size for _ in range(size)]


def matches_pattern(grid):
    offset = (size - len(pattern)) // 2
    for r in range(offset, offset + len(pattern)):
        for c in range(offset, offset + len(pattern)):
            if grid[r][c] != pattern[r - offset][c - offset]:
                return False
    return True


result = 0
i = 0
cycle = 4095
target = 1000000000
while i < target:
    if i == cycle:
        mult = (target - i) // cycle
        result *= mult
        i *= mult

    next = [["."] * size for _ in range(size)]
    for r in range(size):
        for c in range(size):
            count = 0
            for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < size and 0 <= nc < size:
                    count += grid[nr][nc] == "#"

            if grid[r][c] == "#":
                if count % 2 != 0:
                    next[r][c] = "#"
            else:
                if count % 2 == 0:
                    next[r][c] = "#"

    grid = next
    if matches_pattern(grid):
        result += sum(c == "#" for row in grid for c in row)

    i += 1

print(result)

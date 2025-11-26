from heapq import heappush, heappop
from itertools import product

grid = [list(line) for line in open(0).read().splitlines()]

sr, sc = 0, 0
cr, cc = 0, 0
for r, row in enumerate(grid):
    for c, x in enumerate(row):
        match x:
            case "S":
                sr, sc = r, c
                grid[r][c] = "0"
            case "@":
                cr, cc = r, c
                grid[r][c] = "0"


def dist(start, end, limit, radius):
    seen = set()
    queue = [(0, start)]
    while queue:
        dist, pos = heappop(queue)
        if pos in seen or dist > limit:
            continue
        seen.add(pos)

        if pos == end:
            return dist

        r, c = pos
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                continue
            if abs(nr - cr) ** 2 + abs(nc - cc) ** 2 > radius * radius:
                heappush(queue, (dist + int(grid[nr][nc]), (nr, nc)))


def solve(radius, d1, d2, d3):
    seconds = radius * 30 + 29

    d = radius + 1
    lr, lc = cr, cc - d - d1
    br, bc = cr + d + d2, cc
    rr, rc = cr, cc + d + d3

    route = [
        ((sr, sc), (lr, lc)),
        ((lr, lc), (br, bc)),
        ((br, bc), (rr, rc)),
        ((rr, rc), (sr, sc)),
    ]

    time = 0
    for a, b in route:
        d = dist(a, b, seconds - time, radius)
        if d is None:
            return None
        time += d
    return time * radius


for i in range(len(grid)):
    solutions = []
    for d1, d2, d3 in product(range(3), repeat=3):
        result = solve(i, d1, d2, d3)
        if result is not None:
            solutions.append(result)
    if solutions:
        print(min(solutions))
        break

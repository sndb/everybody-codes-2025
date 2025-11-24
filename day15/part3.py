from collections import deque

input = open(0).read().strip().split(",")

walls = []
good_rows = set([0])
good_cols = set([0])

r, c = 0, 0
dr, dc = -1, 0
for x in input:
    d, n = x[0], int(x[1:])
    if d == "L":
        dr, dc = -dc, dr
    else:
        dr, dc = dc, -dr

    nr, nc = r + dr * n, c + dc * n
    good_rows.update([nr - 1, nr, nr + 1])
    good_cols.update([nc - 1, nc, nc + 1])

    r1, r2 = sorted([r + dr, nr])
    c1, c2 = sorted([c + dc, nc])
    walls.append((r1, c1, r2, c2))

    r, c = nr, nc

good_rows = sorted(good_rows)
good_cols = sorted(good_cols)

r0_index = good_rows.index(0)
c0_index = good_cols.index(0)

goal = (good_rows.index(r) - r0_index, good_cols.index(c) - c0_index)

row_map = {i - r0_index: r for i, r in enumerate(good_rows)}
col_map = {i - c0_index: c for i, c in enumerate(good_cols)}

grid = {}
for r, mr in row_map.items():
    for c, mc in col_map.items():
        for wr1, wc1, wr2, wc2 in walls:
            if wr1 <= mr <= wr2 and wc1 <= mc <= wc2:
                grid[(r, c)] = True
                break
        else:
            grid[(r, c)] = False

seen = set()
queue = deque([((0, 0), 0)])
while queue:
    pos, steps = queue.popleft()
    if pos == goal:
        print(steps)
        break

    if pos in seen or grid[pos]:
        continue
    seen.add(pos)

    r, c = pos
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        adj = (r + dr, c + dc)
        if adj in grid:
            nr, nc = adj
            if r != nr:
                cost = abs(row_map[r] - row_map[nr])
            else:
                cost = abs(col_map[c] - col_map[nc])
            queue.append((adj, steps + cost))

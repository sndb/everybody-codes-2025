from collections import defaultdict
from math import inf

passages = defaultdict(list)
for line in open(0).read().splitlines():
    pos, start, height = map(int, line.split(","))
    passages[pos].append((start, start + height))

last = max(passages.keys())

cache = {}
def solve(pos, height):
    key = (pos, height)
    if key not in cache:
        if ps := passages[pos]:
            if any(start <= height < end for start, end in ps):
                if pos == last:
                    return 0
            else:
                return inf

        flap = 1 + solve(pos + 1, height + 1)
        no_flap = solve(pos + 1, height - 1)
        cache[key] = min(flap, no_flap)

    return cache[key]

print(solve(0, 0))

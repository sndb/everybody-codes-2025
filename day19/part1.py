import functools
from math import inf

data = (map(int, line.split(",")) for line in open(0).read().splitlines())
passages = {pos: (start, start + height) for pos, start, height in data}
last = max(passages.keys())

@functools.cache
def solve(pos, height):
    if pos in passages:
        start, end = passages[pos]
        if start <= height < end:
            if pos == last:
                return 0
        else:
            return inf

    flap = 1 + solve(pos + 1, height + 1)
    no_flap = solve(pos + 1, height - 1)
    return min(flap, no_flap)

print(solve(0, 0))

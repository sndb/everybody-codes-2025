from collections import defaultdict

passages = defaultdict(list)
for line in open(0).read().splitlines():
    pos, start, height = map(int, line.split(","))
    passages[pos].append((start, start + height))

last = max(passages.keys())

def next_passages(pos):
    for p, result in passages.items():
        if p > pos:
            return p, result
    return -1, []

def path_flaps(pos, height, t_pos, t_height):
    dh, dp = t_height - height, t_pos - pos
    if (dp + abs(dh)) % 2 == 0 and abs(dh) <= dp:
        return (dp + dh) // 2

def solve(pos, height, acc):
    t_pos, ps = next_passages(pos)
    for start, end in ps:
        for t_height in range(start, end):
            delta = path_flaps(pos, height, t_pos, t_height)
            if delta is not None:
                if t_pos == last:
                    return acc + delta

                ret = solve(t_pos, t_height, acc + delta)
                if ret is not None:
                    return ret

print(solve(0, 0, 0))
